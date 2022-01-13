import webbrowser
import easygui

word = easygui.enterbox(msg='Enter a keyword to search:', title='AutoDict', default='')

if word != None:
    webbrowser.open(f'https://en.dict.naver.com/#/search?range=all&query={word}', new=1, autoraise=True)
