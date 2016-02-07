import subprocess
import os
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
    command = "tesseract " + picture + " stdout -psm 1 2>/dev/null"#" stdout 2>/dev/null"
    output, err = osExec(command)
    return output.strip().decode('utf-8')

def addToClipboard(text):
    pyperclip.copy(text)

def osExec(command):
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, env=envCopy)
    return proc.communicate()


if __name__ == '__main__':
    CaptureApp().run()
