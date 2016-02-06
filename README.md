# StatusBar-OCR

StatusBar-OCR  Copyright (C) 2016  Bo Warren </br>
This program comes with ABSOLUTELY NO WARRANTY </br>
Licensed under the GNU GPL. See LICENSE.md or http://www.gnu.org/licenses/gpl.html for details.

A status bar indicator for Optical Character Recognition.  This allows a portion of the screen to be selected, and to be made copyable (Useful for pdfs and other things which you can't copy text with) and works best with black and white typed text. Compiled & tested on Intel 64-bit OSX El-Capitan.

This requires the 'tesseract' software be installed.  Directions for a complete installation are below.

## Installing
1) install homebrew (directions found at http://brew.sh): </br>
`$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

2) install tesseract: </br>
`$ brew install tesseract`

3a) install the indicator: </br>
`$ wget https://github.com/bhwarren/StatusBar-OCR/dist/StatusBar-OCR.app
$ mv StatusBar-OCR.app ~/Applications/`

## Compile instructions
prerequisites: the 'py2app' 'rumps' and 'pyperclip' packages are installed with pip

1) `$ git clone https://github.com/bhwarren/StatusBar-OCR && cd StatusBar-OCR` </br>
2) `$ sudo python setup.py py2app` </br>
3) `$ sudo mv ./dist/StatusBar-OCR.app ~/Applications`

## Attribution

The icons used in this software were made by http://www.designmodo.com and were obtained from http://www.flaticon.com. They are licensed under Creative Commons BY 3.0, found at http://creativecommons.org/licenses/by/3.0/, and do not have any affiliation with this project.
