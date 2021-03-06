#SLYTHER
version = '0.0.3'

from colorama import init
init()
from colorama import Fore, Back, Style

from modules import audit
from modules import check

def banner():
    print(Fore.MAGENTA + Style.BRIGHT + f"""
  ______   __            _   __                      
.' ____ \ [  |          / |_[  |                     
| (___ \_| | |   _   __`| |-'| |--.  .---.  _ .--.   
 _.____`.  | |  [ \ [  ]| |  | .-. |/ /__\\[ `/'`\]  
| \____) | | |   \ '/ / | |, | | | || \__., | |      
 \______.'[___][\_:  /  \__/[___]|__]'.__.'[___]     
                \__.'                                     
                                                """ + Style.RESET_ALL + Fore.MAGENTA + f"""
                                                > AWS Security Tool
                                                > Created by @iamavu
                                                > v{version}
                                                """)
    print(Style.RESET_ALL)
    

def slyther():
    banner()
    isAWS = check.check_aws()
    if isAWS:
        audit.audit.main()
    else:
        print(Fore.RED + '[!] aws-cli is not installed!')
        exit()   
    

if __name__ == '__main__':
    try:
        slyther()
    except KeyboardInterrupt:
        print(Fore.RED + '\n[!] Keyboard Interrupt received! Aborted!')
        exit()
