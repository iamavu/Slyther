from colorama import init
init()
from colorama import Fore, Back, Style
from modules.bucket import parser

import requests
import urllib3
import subprocess
import os

def audit():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    bucket = parser()
    bucket = bucket.b
    print(Fore.YELLOW + f'[*] Checking bucket "{bucket}" for public access...')
    try:
        response = requests.get(f'https://{bucket}.s3.amazonaws.com', verify=False)
        if response.status_code == 404:
            print(Fore.RED + f'\n[-] Bucket "{bucket}" doesn\'t exist!')
            print(Fore.RED + f'\n[-] Exiting...')
            exit()
        else:
            print(Fore.BLUE + f'\n[+] Bucket "{bucket}" gave the response code {response.status_code}')        
    except requests.exceptions.ConnectionError:
        print(Fore.RED + '[!] Connection Error!')
    
    region = response.headers['x-amz-bucket-region']
    print(Fore.BLUE + f'\n[+] Bucket "{bucket}" is in region "{region}"')
    
    print(Fore.YELLOW + f'\n[*] Checking read access of bucket "{bucket}"...')
    try:
        output = subprocess.check_output(f'aws s3 ls s3://{bucket} --recursive --region {region} --no-sign-request', shell=True, stderr=subprocess.STDOUT)
        
        output = output.decode('utf-8')
        print(Fore.GREEN + f'\n[+] Contents can be listed on bucket "{bucket}"')
        print(Fore.BLUE + f'\n[+] Contents: \n')
        print(Style.RESET_ALL + output)
    except subprocess.CalledProcessError:
        print(Fore.RED + f'\n[-] Bucket "{bucket}" doesn\'t have public access to read contents!')
        
    print(Fore.YELLOW + f'\n[*] Checking write access of bucket "{bucket}"...')
    cwd = os.getcwd()
    try:
        output = subprocess.check_output(f'aws --region {region} s3 cp {cwd}/1337.txt s3://{bucket}/1337.txt', shell=True, stderr=subprocess.STDOUT)
        output = output.decode('utf-8')
        if 'upload' in output:
            print(Fore.GREEN + f'\n[+] Contents can be written to bucket "{bucket}"')
    except:
        print(Fore.RED + f'\n[-] Bucket "{bucket}" doesn\'t have public access to write contents!')
    
    print(Fore.YELLOW + f'\n[*] Checking delete access of bucket "{bucket}"...')
    try:
        output = subprocess.check_output(f'aws --region {region} s3 rm s3://{bucket}/1337.txt', shell=True, stderr=subprocess.STDOUT)
        output = output.decode('utf-8')
        if 'upload' in output:
           print(Fore.GREEN + f'\n[+] Contents on {bucket} can be deleted!')
    except subprocess.CalledProcessError:
        print(Fore.RED + f'\n[-] Bucket "{bucket}" doesn\'t have public access to delete contents!')