#SLYTHER
version = '0.0.1'

from colorama import init
init()
from colorama import Fore, Back, Style

from modules import audit

def banner():
    print(Fore.CYAN + f"""
  ______   __            _   __                      
.' ____ \ [  |          / |_[  |                     
| (___ \_| | |   _   __`| |-'| |--.  .---.  _ .--.   
 _.____`.  | |  [ \ [  ]| |  | .-. |/ /__\\[ `/'`\]  
| \____) | | |   \ '/ / | |, | | | || \__., | |      
 \______.'[___][\_:  /  \__/[___]|__]'.__.'[___]     
                \__.'                                     
                                                > AWS Security Tool
                                                > Created by @iamavu
                                                > v{version}
                                                """)
    print(Style.RESET_ALL)
    

def slyther():    
    audit.audit()

if __name__ == '__main__':
    try:
        slyther()
    except KeyboardInterrupt:
        print(Fore.RED + '\n[!] Keyboard Interrupt received! Aborted!')
        exit()