import sys
import os
import subprocess
import re


def subdomains(domain):
    file_object_1 = open('outputs/subdomains.txt', 'a')
    try:
        output = subprocess.check_output("python3 Sublist3r/sublist3r.py -d "+domain, shell=True).decode("utf-8") 
        print('Domain:{0} \n\n SubDomain: {1}'.format(domain, output))
        file_object_1.write('Domain:{0} \n\n SubDomain: {1}'.format(domain, output))
    except:
        print(domain+" not resolvable")
    file_object_1.close()

def ipcollector(files):
    file_object_2 = open('outputs/ip.txt', 'a')
    print('________________________________________________________Collecting IP________________________________________________________')
    try:
        with open(files) as file:
            for line in file:
                try:
                    output = subprocess.check_output("nslookup "+line, shell=True).decode("utf-8") 
                    ip=re. search(r'Address: (.*?)\n', str(output)). group(1)
                    print('Domain:{0}  ip:{1}'.format(line,ip))
                    file_object_2.write('Domain:{0} ip: {1}'.format(line, ip))

                except:
                    print(line+" not resolvable")
    except:
        print("file not found")

    file_object_2.close()


def techstack(files):
    file_object_3 = open('outputs/techstack.txt', 'a')
    print("____________________________________________________Collecting TechStack____________________________________________________")
    try:
        with open(files) as file:
            for line in file:
                try:
                    output = subprocess.check_output("python3 wappalyzer-cli/build/scripts-3.10/wappy -u"+line, timeout=10,shell=True).decode("utf-8") 
                    print('Domain:{0} TechStack: {1}'.format(line, output))
                    file_object_3.write('Domain:{0} TechStack: {1}'.format(line, output))
                except:
                    print(line+" not resolvable")
    except:
        print("file not found")
    file_object_3.close()



if __name__=="__main__":
    for i in sys.argv:
        if(i=='-h'):
            print('''
 _       _   _____          _____       _    ___       
/ |_ __ | |_|___ / _ __ ___|___ / _ __ | |_ / _ \ _ __ 
| | '_ \| __| |_ \| '__/ __| |_ \| '_ \| __| | | | '__|
| | | | | |_ ___) | | | (__ ___) | |_) | |_| |_| | |   
|_|_| |_|\__|____/|_|  \___|____/| .__/ \__|\___/|_|   
                                 |_|                   
            ''')
            print('''usage : -ip for finding ip address of domain list eg: `python3 main.py -ip domains.txt` \nusage : -tech for finding techstack of domain list eg: `python3 main.py -tech domains.txt`\nusage : -d for finding subdomains eg: `python3 main.py -d domain.com` \n''')
        if(i=='-ip'):
            ipcollector(sys.argv[-1])
        if(i=='-tech'):
            techstack(sys.argv[-1])
        if(i=='-d'):
            subdomains(sys.argv[-1])
