#!/usr/bin/env python3

# Coptyright 2016 (c) Brian McKean

'''
    File name: delpoy.py
    Author: Brian McKean
    Date created: 10/12/2016
    Date last modified: 10/12/20166
    Python Version: 3.5


    input: a string that the program will use to match instance names on aws
    input: a keyfile for accessing AWS

    output: probe software is installed on amazon instances
            list of machines & ip addresses where monitor SW is installed

dependencies:
            uses getHosts.py
 
'''
from gethost import getHost
import subprocess
import sys

## parse input for string and keyfile
# fake for now
instance_string = "aws"
key_file = "/Users/brianmckean/.ssh/quevedo-kp1.pem"
## FOr now need to specify user id for ssh
## Need to specify command for packacge install
login = "ubuntu"
package_mgr = "apt-get"


## get list of AWS hosts for account
instance_list = []
hosts = getHost()
hosts = hosts.splitlines()
for line in hosts:
    line_elements = line.split()
    #print(line, line_elements)
    if '#' in line_elements[0]:
        continue
    instance_list.append(line_elements[0]) 



## from list find instance names matching string
#print(instance_list)
cmd =  package_mgr+"install sysstat"
for instance in instance_list:
    ## from this list ssh into machines using IP address
    ##  Install monitor software
    print("Installing sar on {}".format(instance))
    cmd_string = "ssh -t -i {} {}@{} {}".format(key_file, login, instance, cmd)
    cmd_string = ["ssh","-t","-o","StrictHostKeyChecking=no",
                       "-i",key_file,"ec2user@{}".format(instance),
                       "sudo","yum","install","sysstat"]
    #print(cmd_string)
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
