from setuptools import setup

APP = ['StatusBar-OCR.py']
DATA_FILES = ['icon-black.png']
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps','pyperclip'],
    'iconfile':'icon-black.icns'
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    name='StatusBar-OCR',
    description='A status bar indicator for Optical Character Recognition',
    author='Bo Warren',
    url='https://github.com/bhwarren/StatusBar-OCR',
    license='GPL License',
)
