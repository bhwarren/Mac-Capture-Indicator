from setuptools import setup

APP = ['recog.py']
DATA_FILES = ['icon-black.png','icon-white.png','tesseract']
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps','pyperclip'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
