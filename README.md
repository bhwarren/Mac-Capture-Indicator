# OCRStatusBar

A status bar indicator for Optical Character Recognition.  This allows a portion of the screen to be selected, and to be made copyable (Useful for pdfs and other things which you can't copy text with) and works best with black and white typed text. Compiled & tested on Intel 64-bit OSX El-Capitan.

OCRStatusBar  Copyright (C) 2016  Bo Warren </br>
This program comes with ABSOLUTELY NO WARRANTY </br>
Licensed under the GNU GPL. See LICENSE.md or http://www.gnu.org/licenses/gpl.html for details.

This requires the 'tesseract' software be installed.  Directions for a complete installation are below.

## Installing

1) Open Terminal.app and install homebrew (if you haven't previously) by copying and pasting everything after the '$' into the terminal and press enter: </br>
`$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

2) install tesseract the same way: </br>
`$ brew install tesseract`

3) install the indicator: </br>
Download the latest OCRStatusBar.dmg file from the releases here:
https://github.com/bhwarren/OCRStatusBar/releases/download/1.0.1/OCRStatusBar.dmg </br>
Then open it and drag OCRStatusBar.app into the Applications folder

4) allow the app to run in the security settings
open System Preferences, and click on Security and Privacy.  Unlock the lock and enter the password if you need to, then enable apps from 'Anywhere' to be opened.  Re-lock the lock and run the OCRStatusBar app.

## Compile & install instructions
prerequisites: python2 and the 'py2app' and 'pyperclip' packages are installed with pip (also 'pyobjc' if using homebrew python). 'rumps' is also required, but if you use darkmode, then you'll want an updated version than the one available with pip. See https://github.com/chrisidefix/rumps/tree/icon-advance about installing it (yes, the necessary changes are in the icon-advance branch).

1) `$ git clone https://github.com/bhwarren/OCRStatusBar && cd OCRStatusBar` </br>
2) `$ sudo python setup.py py2app --emulate-shell-environment` </br>
3) `$ sudo mv ./dist/OCRStatusBar.app ~/Applications`

## Attribution

The icons used in this software were made by http://www.designmodo.com and were obtained from http://www.flaticon.com. They are licensed under Creative Commons BY 3.0, found at http://creativecommons.org/licenses/by/3.0/, and do not have any affiliation with this project.
