from setuptools import setup

APP = ['OCRStatusBar.py']
DATA_FILES = ['icon-black.png','LICENSE.md']
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
    name='OCRStatusBar',
    version='1.0.0',
    description='A status bar indicator for Optical Character Recognition',
    author='Bo Warren',
    url='https://github.com/bhwarren/OCRStatusBar',
    license='GPL License',
)
