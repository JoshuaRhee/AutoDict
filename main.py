import webbrowser
import easygui

word = easygui.enterbox(msg='Enter a keyword to search:', title='AutoDict', default='')

if word != None:
    webbrowser.open(f'https://en.dict.naver.com/#/search?range=all&query={word}', new=1, autoraise=True)

# HOW TO MAKE CODE TO EXE:
# pyinstaller -w -F -n AutoDict --icon=.\icon.ico main.py
# -w : supress console
# -F : package to a single file
# -n : name of the file
# --icon= : set icon image