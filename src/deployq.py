#!/usr/bin/env python3

# Coptyright 2016 (c) Brian McKean

'''
    File name: instprobes.py
    Author: Brian McKean
    Date created: 08/31/2016
    Date last modified: 09/02/2016
    Python Version: 3.5


    Gets a list of IPs and dns names for a set of ec2 instances

    input: a string that the program will use to match instance names on aws

    output: probe software is installed on amazon instances
            list of machines & ip addresses where monitor SW is installed
    dependencies:
            uses getHosts.py
            uses aws.py
 
'''
from gethost import getHost
import subprocess
import sys

## parse input for string and keyfile
# fake for now
instance_string = "aws"
key_file = "/Users/brianmckean/.ssh/quevedo-kp1.pem"


## get list of AWS hosts for account
instance_list = []
hosts = getHost()
hosts = hosts.splitlines()
for line in hosts:
    line_elements = line.split()
    print(line, line_elements)
    if '#' in line_elements[0]:
        continue
    instance_list.append(line_elements[0]) 

## from list find instance names matching string


## from this list ssh into machines using IP address
##  Install monitor software

print(instance_list)
## FIXME -- change this bash script to python
cmd =  "yum -y install sysstat"
print(instance_list)
for instance in instance_list:
    # First find package installer -- either yum or apt-get
    # Then find distro
    # Then intsall syststat for the appropriate :w

    print("Installing sar on {}".format(instance))
    cmd_string = "ssh -t -i {} ec2-user@{} {}".format(key_file, instance, cmd)
    cmd_string = ["ssh","-t","-o","StrictHostKeyChecking=no",
                       "-i",key_file,"ec2user@{}".format(instance),
                       "sudo","yum","install","sysstat"]
    print(cmd_string)
    ssh = subprocess.Popen(["ssh","-t","-o","StrictHostKeyChecking=no",
                       "-i",key_file,"ec2-user@{}".format(instance),
                       "sudo","yum","install","sysstat"],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
    result = ssh.stdout.readlines()
    if result == []:
        error = ssh.stderr.readlines()
        print ("ERROR: %s" % error)
    else:
        print (result)
