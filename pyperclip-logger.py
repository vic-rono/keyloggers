
import pyperclip

import time
List = []

while True:
    if pyperclip.paste() != 'None': #checks if the clipboard is empty
        value = pyperclip.paste()

        if value not in List:
            List.append(value)

        print(List)

        time.sleep(4)#loops after four seconds to give results of copy paste activity

#victorroro@yeehaamail.com
#password6000