#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#Coded by Skajp

import socket, sys, os, time, threading, concurrent.futures
from async_timeout import timeout

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

sys.stdout.write("\x1b]2;|   Port Scanner  |   By: Skajp   |   IP: \x07")
print_lock=threading.Lock()
clear()
result = ("""  ____            _     ____                                  
 |  _ \ ___  _ __| |_  / ___|  ___ __ _ _ __  _ __   ___ _ __ 
 | |_) / _ \| '__| __| \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 |  __/ (_) | |  | |_   ___) | (_| (_| | | | | | | |  __/ |   
 |_|   \___/|_|   \__| |____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                              """)
print('\033[1;37m' + result)
print('\033[0;90m' + " -----------------------------------------------------------------")
print('\033[1;37m' + " Made by" + '\033[0;90m' + " > " + '\033[0;37m' + "DeadSkajp#5906")
print('\033[1;37m' + " Discord" + '\033[0;90m' + " > " + '\033[0;37m' + "discord.gg/gUVF7nNuQ8")
print('\033[1;37m' + " Website" + '\033[0;90m' + " > " + '\033[0;37m' + "https://rezix.tk/\n")
print('\033[1;37m' + " Scanner" + '\033[0;90m' + " > " + '\033[0;37m' + "Type " + '\033[0;93m' + "0" + '\033[0;3m' + " to scan all ports")
print("")
print("")
ip = input('\033[1;37m' + " Enter IP" + '\033[1;90m' + " > " + '\033[0;37m' +f"")
ports = int(input('\033[1;37m' + " Scan To Port" + '\033[1;90m' + " > " + '\033[0;37m' +f""))

work = 100

if ports == 0:
    ports = 65535

if ports >= 10000:
    work = 200

sys.stdout.write(f"\x1b]2;|   Port Scanner  |   By: Skajp   |   IP: {ip}\x07")
print("\n\n")
time.sleep(1)

def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.9)
    try:
        scanner.connect((ip, port))
        scanner.close()
        with print_lock:
            print('\033[1;32m' + "\r Opened" + '\033[0;90m' + " > " + '\033[0;37m' + f"{port}    ")
            
    except:
        l = [f'{port}']
        for i in l+l+l:
            sys.stdout.write('\033[37m\r Scanning \033[0;90m> \x1b[38;2;120;120;120m'+i)
            sys.stdout.flush()

with concurrent.futures.ThreadPoolExecutor(max_workers=work) as executor:
    for port in range(ports):
        executor.submit(scan, ip, port)

continueed = input('\033[1;37m' + "\n\n Scanner" + '\033[1;90m' + " > " + '\033[0;37m' + "Press" + '\033[1;93m' + " Enter " + '\033[0;37m' + "to exit\n")
time.sleep(0.1)
print('\033[0;31m' + " Closing...")
time.sleep(1)     