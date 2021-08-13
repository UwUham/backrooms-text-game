from os import system # defining required variables
from time import sleep # defining required variables
import sys # defining required variables
neofetchbool = False  # initialising variables
NeoRun = False # initialising variables

platform = sys.platform # determing the command to be used for the clear function. importing the clear from gamefuntions caused an error so we just replicated it.
if platform == "linux" or platform == "linux2" or platform == "darwin": # determing the command to be used for the clear function. importing the clear from gamefuntions caused an error so we just replicated it.
    clearcmd = "clear" # determing the command to be used for the clear function. importing the clear from gamefuntions caused an error so we just replicated it.
elif platform == "win32" or platform == "win64": # determing the command to be used for the clear function. importing the clear from gamefuntions caused an error so we just replicated it.
    clearcmd = "cls" # determing the command to be used for the clear function. importing the clear from gamefuntions caused an error so we just replicated it.

def clear(): # creating the clear function
    system(clearcmd) # creating the clear function

def neofetch(var): # create the neofetch function (neofetch is a screenfetch tool used across essentially all operating systems as a CLI system information tool. It works across windows, macOS, linux, Android, and even iOS and iPadOS.)
    if var == True: # if the specified variable is true:
        print('''
       .---.     root@arch
       |---|     
       |---|     ---------
       |---|    
   .---^ - ^---. OS: Backrooms Linux 1.0.0
   :___________:
      |  |//|    Host: SYSTEM rf1171-x
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
''') # print the text

def arch_start(): # create the arch_start function, the functoin used to begin the puzzle and throw us into an operating system i created with the sole purpose of running neofetch
    global neofetchbool, NeoRun # assigning variables to global
    clear() # clear the screen
    print("\033[0;37;40mWelcome to \033[1;36;40mBackroom Linux (arch-based)!\033[0;37;40m") # printing coloured text
    while NeoRun == False: # while neofetch has not yet been ran:
        cmd = input("[\033[1;31;40mroot\033[0;37;40m@arch]# ") # have a text window to run commands, as similar to Unix as i could manage
        if cmd.startswith("pacman"): # if the command is "pacman -S neofetch"
            if cmd.startswith("pacman -S"): # if the command is "pacman -S neofetch"
                if cmd.startswith("pacman -S neofetch"): # if the command is "pacman -S neofetch"
                    index = -1  # have a loading screen for the "download" of the function, as Unix package managers do
                    while index != 23: # have a loading screen for the "download" of the function, as Unix package managers do
                        index = index + 1 # have a loading screen for the "download" of the function, as Unix package managers do
                        time = str(int(index/6)) # have a loading screen for the "download" of the function, as Unix package managers do
                        clear() # have a loading screen for the "download" of the function, as Unix package managers do
                        print("neofetch 7.1.0.2-any  83.1KiB  22.0KiB/s  00:0" + time + "  " + "[" + (index * "#") + ((23 - index) * "-") + "]") # have a loading screen for the "download" of the function, as Unix package managers do
                        sleep(0.17) # have a loading screen for the "download" of the function, as Unix package managers do
                    neofetchbool = True # tell the code Neofetch is installed
                if cmd.startswith("pacman -Ss"): # if the command is pacman -Ss
                    print('''
                    neofetch [1.0.0]
                    A command line system information tool''') # print list of packages
                else: # if the command is "pacman -S (anything other than neofetch)":
                    print("\033[0;31;40merror:\033[0;37;40m package not found: " + cmd[9:]) # print error text
            else: # if the command is pacman "(anything other than -S)":
                print("\033[0;31;40merror:\033[0;37;40m unknown operand: -S <package> to install, -Ss to list available packages") # print error text
        elif cmd == "help": # if the user runs the help command:
            print("The only command you need for this task is 'pacman'.") # tell the user about the pacman command
        elif cmd == "neofetch" and neofetchbool == True: # if the user runs neofetch after installing it:
            NeoRun = True # run neofetch and tell the code that neofetch has been run
            neofetch(neofetchbool) # run neofetch and tell the code that neofetch has been run
        else: # if the user types an unknown command:
            print("\033[0;31;40merror:\033[0;37;40m unknown command" + cmd + ": try 'help'.") # tell the user about "help".