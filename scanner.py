# Made by: Skajp   |   Discord: Skajpik#3232
# Github: https://github.com/SkajpCZ/PscanPy
# Version: 1
import os
def port_scanner():
    import socket, time, threading, concurrent.futures
    print_lock = threading.Lock()
    ips = input('\033[1;93m' + "\n Enter IPs \033[1;90m(split by \033[0;93m,\033[1;90m)" + '\033[1;90m' + " > " + '\033[0;37m' +f"")
    ports = int(input('\033[1;93m' + " Scan To Port \033[1;90m(\033[0;93m0\033[1;90m for all ports)" + '\033[1;90m' + " > " + '\033[0;37m' +f""))
    work = 100
    if ports == 0:
        ports = 65535
    if ports >= 32767:
        work = 200
    def scan(ip, port):
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(1)
        try:
            scanner.connect((ip, port))
            scanner.close()
            with print_lock:
                print('\033[1;32m' + "\r Opened" + '\033[0;90m' + " > " + '\033[0;37m' + f"{port}    ")
        except:
            #print('\033[1;31m' + " Closed" + '\033[0;90m' + " > " + '\033[0;37m' + f"{port}", end="\r")
            pass
    if ',' in ips:
        for ip in ips.split(','):
            print('\033[1;93m' + "\n\n Scanning" + '\033[1;90m' + " > " + '\033[0;37m' +f"{ip}")
            try:
                with concurrent.futures.ThreadPoolExecutor(max_workers=work) as executor:
                    for port in range(ports):
                        executor.submit(scan, ip, port)
            except KeyboardInterrupt:
                print('\033[1;31m' + ' Stopping')
                pass
    else:
        print("\n")
        try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=work) as executor:
                for port in range(ports):
                    executor.submit(scan, ips, port)
        except KeyboardInterrupt:
            print('\033[1;31m' + ' Stopping')
            pass
    input('\n\033[1;37m Press \033[1;93m[ Enter ]\033[1;37m to exit')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

print(f"""\033[1;36m
              _____                                 
        ____ / ___/_________ _____  ____  ___  _____
       / __ \\\__ \/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
      / /_/ /__/ / /__/ /_/ / / / / / / /  __/ /    
     / .___/____/\___/\__,_/_/ /_/_/ /_/\___/_/     
    /_/                                             \033[1;37mby \033[1;90mSkajp
                                                    \033[1;37mVersion: \033[1;90m1
""")

port_scanner()
