from os import system
from time import sleep
import sys
neofetchbool = False
NeoRun = False

platform = sys.platform
if platform == "linux" or platform == "linux2" or platform == "darwin":
    clearcmd = "clear"
elif platform == "win32" or platform == "win64":
    clearcmd = "cls"

def clear():
    system(clearcmd)

def neofetch(var):
    if var == True:
        print('''
       .---.     root@arch
       |---|     
       |---|     ---------
       |---|    
   .---^ - ^---. OS: Backrooms Linux 1.0.0
   :___________:
      |  |//|    Host: Backport rf1171-x
      |  |//|   
      |  |//|    Kernel: 5.12.13-arch1-2
      |  |//|   
      |  |//|    Uptime: 4 minutes, 20 seconds
      |  |//|   
      |  |.-|    Packages: 7 (pacman)
      |.-'**|   
       \***/     Shell: Python 3.9.6
        \*/     
         V       Resolution: 1920x1080
''')

def arch_start():
    global neofetchbool, NeoRun
    clear()
    print("\033[0;37;40mWelcome to \033[1;36;40mBackroom Linux (arch-based)!\033[0;37;40m")
    while NeoRun == False:
        cmd = input("[\033[1;31;40mroot\033[0;37;40m@arch]# ")
        if cmd.startswith("pacman"):
            if cmd.startswith("pacman -S"):
                if cmd.startswith("pacman -S neofetch"):
                    index = -1
                    while index != 23:
                        index = index + 1
                        time = str(int(index/6))
                        clear()
                        print("neofetch 7.1.0.2-any  83.1KiB  22.0KiB/s  00:0" + time + "  " + "[" + (index * "#") + ((23 - index) * "-") + "]")
                        sleep(0.17)
                    neofetchbool = True
                else:
                    print("\033[0;31;40merror:\033[0;37;40m package not found: " + cmd[9:])
            else:
                print("\033[0;31;40merror:\033[0;37;40m unknown operand: -S to install")
        elif cmd == "help":
            print("The only command you need for this task is 'pacman'.")
        elif cmd == "neofetch" and neofetchbool == True:
            NeoRun = True
            neofetch(neofetchbool)
        else:
            print("\033[0;31;40merror:\033[0;37;40m unknown command" + cmd + ": try 'help'.")