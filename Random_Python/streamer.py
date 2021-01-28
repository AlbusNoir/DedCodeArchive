'''
Idk I got bored and decided to just make a thing to open streaming sites from python
It's nothing special
'''

import webbrowser

'''
By default webbrowser will use the default browser of the system
You can edit that with these vars:
# MacOS
chrome = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
# chrome = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# Linux
# chrome = '/usr/bin/google-chrome %s'


Pretty sure on Linux you can actually just use like 'google-chrome' or 'firefox' or something
'''

print('''Welcome to PyStreamer v1.0
Please select an option:
1) Netflix
2) Hulu
3) Amazon Prime Video
4) HBO Max
5) Disney+
6) YouTube''')


# you'll need to change this if you have chrome elsewhere
chrome = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

choice = input('> ')

if choice == '1':
    webbrowser.get(chrome).open('netflix.com')
elif choice == '2':
    webbrowser.get(chrome).open('hulu.com')
elif choice == '3':
    webbrowser.get(chrome).open('https://www.amazon.com/gp/video/storefront')
    # why can't amazon have nice links...
elif choice == '4':
    webbrowser.get(chrome).open('hbomax.com')
elif choice == ' 5':
    webbrowser.get(chrome).open('disneyplus.com')
elif choice == '6':
    webbrowser.get(chrome).open('youtube.com')
else:
    print(f'{choice} is not an option. Please pick an option that exists')

# TODO:
# probably add like a while loop or something idk
# probably make this a gui
# idk what else
# make os agnostic? so this is prob done without specifying the browser...
