#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
1- This code block analyzes IP addresses and port informations in a file:

1.1- File contains data like below
    
    127.0.0.1
    22
    80
    445
    192.168.1.1
    80
    443
    445
    8080

2- After execute, script creates an output file that contains the IP:Port like below.

    127.0.0.1:22
    127.0.0.1:80
    127.0.0.1:445
    192.168.1.1:80
    192.168.1.1:443
    192.168.1.1:445
    192.168.1.1:8080

# https://github.com/koparmalbaris
"""

ip_list = []
current_ip = ""

file_path = input("Enter the file location and name: ")

with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        if line.count(".") == 3:
            current_ip = line
        else:
            ip_list.append(f"{current_ip}:{line}")

output_file_path = file_path.replace(".txt", "_parsed.txt")

with open(output_file_path, "w") as output_file:
    for ip in ip_list:
        output_file.write(ip + "\n")
        print(ip)

print("Parsed outputs saved successfully:", output_file_path)