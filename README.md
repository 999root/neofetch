# Neofetch
- A python neofetch tool that works on multiple operating systems.
- Linux, Mac, Windows, etc.
## Installation
- either:
  - Install the exe file and place it in your system32 folder
  - Then run the command neofetch in your cmd.
  ```
   neofetch
  ```
- or:
  - Install the neofetch.py file and the setup.py file and compile it from there and make changes to file if you want
  - Run the setup.py file
  ```
  python setup.py
  ```
  - Which should compile the python file into an exe already or you can compile it yourself by running
  ```
  pyinstaller --onefile neofetch.py
  ```
  - Then you can move the file into the System32 folder which will allow you to run
  ```
  neofetch in cmd
  ```
