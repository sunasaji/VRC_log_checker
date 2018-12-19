#!/usr/bin/env python
# License: These codes are licensed under CC0.
import os
import sys
import re
from os.path import dirname, exists

def main():
    path = sys.argv[1] 
    if not exists(path):
        print('{} is not found'.format(path))
        return 
	
    output_file = open("VRChat_usrlog.txt", mode='a', encoding='utf-8', errors='ignore', buffering=1)

    with open(path, mode='r' , encoding='utf-8',errors='ignore') as input_file:

        for line in input_file:
            match=re.search('([0-9\.]+ [0-9:]+).+Joining or Creating Room: (.+)',line)
            if match != None:
                output_file.write(match.group(1) + " World: " + match.group(2) + "\n")
            match=re.search('([0-9\.]+ [0-9:]+).+OnPlayerJoined (.+)',line)
            if match != None:
                output_file.write(match.group(1) + "  User: " + match.group(2) + "\n")

    output_file.close()

if __name__ == '__main__':
    main()

