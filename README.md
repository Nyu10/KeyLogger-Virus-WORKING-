# KeyLogger Virus (WORKING!)

I wrote a Keylogger Virus that actually works and looks like the game Valorant

**WARNING! ANTIVIRUS PROGRAMS (such as AVAST FREE ANTIVIRUS) WILL FLAG VALORANT.EXE as a VIRUS**
**THIS PROJECT WAS FOR EDUCATIONAL PURPOSES. DO NOT TRY TO USE A KEYLOGGER BECAUSE IT IS 100% ILLEGAL IN MOST CASES AND FINES, ARRESTS, AND JAIL TIME COULD BE WARRANTED**
## General (Three Versions of Keylogger)
- keylogger.py - saves your keyboard log files into a text.txt
- keylogger2.py - sends your keyboard log files to my email
- Valorant.exe - sends your keyboard log files to my email, but it is an Windows Application Executable disgused as the popular game, VALORANT


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


**ANTIVIRUS PROGRAMS (such as AVAST FREE ANTIVIRUS) WILL FLAG VALORANT.EXE**
 **Tell your antivirus that these files are fine**

**Valorant.exe**
```
./Valorant.exe in command prompt or double click on icon like a normal application
```
Begin typing anywhere and your keyboard strokes will be sent in an email to the email listed in the program file (stuyhackerdemo@gmail.com).
Click ESC key to end process.

[Note: It will pop up a Valorant.exe window that says "YOU HAVE BEEN HACKED". We could have made the program run in the background, but chose not too because we don't actaully want to hack all the stuff you type.]
## Dependencies
* [pynput] = Only version 1.6.8 works not the newest 1.7.2 (keylogger.py and keylogger2.py include a subprocess to install the correct module version so no installation is needed by the user)


## Resources Used

* [pynput](https://pypi.org/project/pynput/) - The python module used to track keystrokes
* [smtplib](https://realpython.com/python-send-email/) - used smtplib module to set up email sending logs to email
* [auto-py-to-exe](https://nitratine.net/blog/post/issues-when-using-auto-py-to-exe/) - Converts Python to Exe


## Authors

* **Nehemiah Yu** - (https://github.com/Nyu10)
* **Johnny Wong** - (https://github.com/jwong10)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

