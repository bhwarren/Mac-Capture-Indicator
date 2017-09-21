import subprocess
import os
import sys
import time
from rumps import *
import pyperclip


basePath = "/".join(os.path.realpath(__file__).split("/")[0:-1])+"/"
envCopy = os.environ.copy()
envCopy["PATH"] += os.pathsep + "/usr/local/bin"

class CaptureApp(rumps.App):
    justClose = 0
    copyToClipboard = 1

    name = "Capture Text"
    indicatorIcon = basePath + "icon-black.png"
    windowIcon = basePath + "icon-black.png"

    def __init__(self):
        #super(AwesomeStatusBarApp, self).__init__("Awesome App")
        super(CaptureApp, self).__init__(self.name)
        #self.menu = []
        self.icon = self.indicatorIcon
        self.template = True
        rumps.debug_mode(False)

        if not tesseractInstalled():
            message = "tesseract not installed, please follow these steps to provide functionality. These steps can be found at https://github.com/bhwarren/OCRStatusBar/blob/master/README.md"

            steps = "1) open terminal and install homebrew if you haven't previously by copying everything after '$' and pressing enter: \n\n $ /usr/bin/ruby -e \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)\" \n\n 2) then install tesseract by again, copying everything after '$' and pressing enter: \n $ brew install tesseract"

            window = Window(message=message, title=self.name, default_text=steps, ok=None)
            window.run()
            sys.exit(0)

    @clicked('Capture Selection')
    def button(self, sender):
        imagePath = getScreenSelection()
        text = getText(imagePath)

        window = Window(message='', title=self.name, default_text=text, ok="Copy to clipboard", cancel="close")
        window.icon = self.windowIcon
        response = window.run()
        if response.clicked == CaptureApp.copyToClipboard:
            addToClipboard(response.text)

    @clicked('About')
    def button(self, sender):
        #show the about page
        message = "OCRStatusBar  Copyright (C) 2016  Bo Warren\
        \n\nThe icons used in this software were made by http://www.designmodo.com and were obtained from http://www.flaticon.com. They are licensed under Creative Commons BY 3.0 (found at http://creativecommons.org/licenses/by/3.0/) and do not have any affiliation with this project.\
        \n\nThis program comes with ABSOLUTELY NO WARRANTY\
        \nLicensed under the GNU GPL. See below or http://www.gnu.org/licenses/gpl.html for details.\
        \n\n GPL License (use arrows to scroll):"
        licenseText = open('./LICENSE.md', 'r').read();
        window = Window(message=message, title=self.name, default_text=licenseText, ok=None)
        window.icon = self.windowIcon
        window.run()



def getScreenSelection():
    #outfile = basePath + timeStamp() + ".jpg"
    #outfile = basePath + "screenshot.jpg"
    outfile = "/tmp/recog-screenshot.jpg"
    out,err = osExec("screencapture -i " + outfile)
    if err:
        err = err.strip().decode('utf-8')
    return outfile

def getText(picture):
    command = "cd /tmp/ && tesseract " + picture + " stdout -psm 1 2>/dev/null"#" stdout 2>/dev/null"
    output, err = osExec(command)
    return output.strip().decode('utf-8')

def addToClipboard(text):
    pyperclip.copy(text)

def osExec(command):
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, env=envCopy)
    return proc.communicate()

def tesseractInstalled():
    def isExecutable(path):
        return os.path.isfile(path) and os.access(path, os.X_OK)

    path, fileName = os.path.split("tesseract")
    if path:
        if isExecutable("tesseract"):
            return True
    else:
        for pathDir in os.environ["PATH"].split(os.pathsep):
            pathDir = pathDir.strip('"')
            executable = os.path.join(pathDir, "tesseract")

            if isExecutable(executable):
                return True

    return False


if __name__ == '__main__':
    CaptureApp().run()
