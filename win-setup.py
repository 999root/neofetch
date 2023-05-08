import os
from time import sleep
import shutil

def install():
  print('\ninstalling modules\n')
  os.system('pip install pyinstaller')
  os.system('pip install shutil')
  print('\ninstall finished\n')
  sleep(1)
  print('\ncompiling\n')
  os.system('pyinstall --onefile neofetch.py')
  print('\ncompiling finished\n')
  src_path = f"{os.getcwd()}\neofetch.py"
  dist_path = 'C:\Windows\System32'
  shutil.move(src_path, dist_path)

if __name__ == "__main__":
  install()
