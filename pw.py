#! python3
#passwordmanager

passwords = {'fb':'ef47xc67hn','blog':'7o94pp6se','email':'sef45d7e','github' : 'ebj37dyhyd'}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('Usage: Win-R: pw.py [account name] - copies account password')
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' +account+' copied to clipboard. ')
	
else:
    print('There is no account named ' +account)
