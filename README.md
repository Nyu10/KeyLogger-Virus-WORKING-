# KeyLogger Virus (WORKING!)

I wrote a Keylogger Virus that actually works and looks like the game Valorant

**WARNING! ANTIVIRUS PROGRAMS (such as AVAST FREE ANTIVIRUS) WILL FLAG VALORANT.EXE as a VIRUS.**
**THIS PROJECT WAS FOR EDUCATIONAL PURPOSES. DO NOT TRY TO USE A KEYLOGGER AS A LEGITIMATE VIRUS BECAUSE IT IS 100% ILLEGAL IN MOST CASES AND FINES, ARRESTS, AND JAIL TIME COULD BE WARRANTED**
## General (Three Versions of Keylogger)
- keylogger.py - saves your keyboard log files into a text.txt
- keylogger2.py - sends your keyboard log files to my email
- Valorant.exe - sends your keyboard log files to my email, but it is an Windows Application Executable disguised as the popular game, VALORANT


## Getting Started and Installing
```
git clone https://github.com/Nyu10/KeyLogger-Virus-WORKING-.git
cd to KeyLogger-Virus-Working
```

**keylogger.py**
```
python keylogger.py 
```
Begin typing anywhere and your keyboard strokes will be recorded in the file text.txt.
Click ESC key to end process.

**keylogger2.py**
```
python keylogger2.py 
```
Begin typing anywhere and your keyboard strokes will be sent in an email to the email listed in the program file (stuyhackerdemo@gmail.com).
Click ESC key to end process.

To send the email logs to your own email, you need to change the email and password in your code. Also, [Turn Allow less secure apps to ON.](https://myaccount.google.com/lesssecureapps) Be aware that this makes it easier for others to gain access to your account.

**Valorant.exe**
```
./Valorant.exe in command prompt or double click on icon like a normal application
```
Begin typing anywhere and your keyboard strokes will be sent in an email to the email listed in the program file (stuyhackerdemo@gmail.com).
Click ESC key to end process.

[Note: It will pop up a Valorant.exe window that says "YOU HAVE BEEN HACKED". We could have made the program run in the background, but chose not too because we don't actaully want to hack all the stuff you type.]
## Dependencies
* [pynput] = Only version 1.6.8 works with our program, not the newest version 1.7.2. (The project files keylogger.py and keylogger2.py will automate the process of instally pynput so no further installation is needed by the user)
## Known Issues

- Antivirus programs (such as Avast Free Antivirus and Microsoft Defender) will flag Valorant.exe as a virus
```
tell your antivirus application that the files are good, such as "restore" and "retrieve" "not a threat"
```
- The ASCII Art (the "YOU HAVE BEEN HACKED") causes an error on my GitBash, but no error on my VSCODE Git Terminal.


This is the error.


*UnicodeEncodeError: 'charmap' codec can't encode characters in position 4-6: character maps to <undefined>* 
  To Solve: 
```
simply delete the YOU HAVE BEEN HACKED print statement from the code. 
```


## Resources Used

* [pynput](https://pypi.org/project/pynput/) - The python module used to track keystrokes
* [smtplib](https://realpython.com/python-send-email/) - used smtplib module to set up email sending logs to email
* [auto-py-to-exe](https://nitratine.net/blog/post/issues-when-using-auto-py-to-exe/) - Converts Python to Exe


## Authors

* **Nehemiah Yu** - (https://github.com/Nyu10)
* **Johnny Wong** - (https://github.com/jwong0123)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

