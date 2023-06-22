#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
This code block represents a program that analyzes a user-specified .gnmap file and extracts the IP addresses and their corresponding port information like below and saving them to an output file. 

    127.0.0.1:22
    127.0.0.1:80
    127.0.0.1:445
    192.168.1.1:80
    192.168.1.1:443

Example nmap scan command for to get .gnmap file

    $ nmap -p22,23,445,80 --open portquiz.net bariskoparmal.com -oA scanOutput

# https://github.com/koparmalbaris
"""

import re

filename = input("Enter the .gnmap file location and name: ")
output_filename = f"{filename}_parsed.txt"

with open(filename, "r") as file:
    gnmap_output = file.read()

ip_port_pattern = r"Host: (\d+\.\d+\.\d+\.\d+).*Ports: ([\d\/\w\/\w\/\w\/\w, ]+)"
matches = re.findall(ip_port_pattern, gnmap_output)

with open(output_filename, "w") as output_file:
    for match in matches:
        ip = match[0]
        ports = match[1].split(", ")
        for port in ports:
            port_info = port.split("/")
            port_number = port_info[0]
            protocol = port_info[2]
            service = port_info[3]
            output_line = f"{ip}:{port_number}\n"
            print(output_line, end="")
            output_file.write(output_line)

print(".gnmap parsed Outputs saved successfully:", output_filename)