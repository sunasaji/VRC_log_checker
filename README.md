# Introduction 
This python script can export world and user name from VRChat log file.

# Getting Started
1. Prepare Python 3.7.1 or use exe file.
2. Find VRChat log file available at:
 C:/Users/(username)/AppData/LocalLow/VRChat/vrchat/output\_log.txt
3. Drag and drop it to the script or exe file.
4. See VRChat\_usrlog.txt at the same directory of the log file.

# Output example
2018.12.19 22:36:07 World: Suna's Playground
2018.12.19 22:36:10  User: sunasaji
...

# Build
In case you want to build the exe by yourself

1. Execute 'pip install pyinstaller'
2. Execute 'pyinstaller vrc\_worldi\_user\_checker.py --onefile --noconsole'
3. Find exe in dist directory

# License

These codes are licensed under CC0.

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

