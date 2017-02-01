#!/usr/bin/env python3

# Coptyright 2016 (c) Brian McKean

'''
    File name: set_host_os.py
    Author: Brian McKean
    Date created: 10/16/2016
    Python Version: 3.5


    input: a list of ip addresses, string
    input: a keyfile for accessing AWS

    output: string modified to instance:OS pair

dependencies:
            uses getHosts.py
 
'''
from gethost import getHost
import subprocess
import sys
import argparse


## parse input for string and keyfile
parser = argparse.ArgumentParser(description="probes servers at ip addresses to get linux distro")
parser.add_argument('-i',type=string, action='store', dest='keyfile', help="-i keyfile")
parser.add_argument("server_list", type=string,
                            help="list of ip addresses to probe")


## Take list of servers and try each type of login
# unbuntu is for ubuntu
# ec2-user RHEL5 & Fedora & SUSE
# root for RHEL5 & SUSE
# 
# From AWS web site
# Use the ssh command to connect to the instance. 
# You'll specify the private key (.pem) file and user_name@public_dns_name. 
# For Amazon Linux, the user name is ec2-user. 
# For RHEL5, the user name is either root or ec2-user. 
# For Ubuntu, the user name is ubuntu. 
# For Fedora, the user name is either fedora or ec2-user. 
# For SUSE Linux, the user name is either root or ec2-user. 
# Otherwise, if ec2-user and root don't work, check with your AMI provider.



print(keyfile, serverlist)

## For now need to specify user id for ssh
## Need to specify command for packacge install


## get list of AWS hosts for account
#instance_list = []
#hosts = getHost()
#hosts = hosts.splitlines()
#for line in hosts:
#    line_elements = line.split()
#    #print(line, line_elements)
#    if '#' in line_elements[0]:
#        continue
#    instance_list.append(line_elements[0]) 
#
#
#
### from list find instance names matching string
##print(instance_list)
#cmd =  package_mgr+"install sysstat"
#for instance in instance_list:
#    ## from this list ssh into machines using IP address
#    ##  Install monitor software
#    print("Installing sar on {}".format(instance))
#    cmd_string = "ssh -t -i {} {}@{} {}".format(key_file, login, instance, cmd)
#    cmd_string = ["ssh","-t","-o","StrictHostKeyChecking=no",
#                       "-i",key_file,"ec2user@{}".format(instance),
#                       "sudo","yum","install","sysstat"]
#    #print(cmd_string)
#    ssh = subprocess.Popen(["ssh","-t","-o","StrictHostKeyChecking=no",
#                       "-i",key_file,"ec2-user@{}".format(instance),
#                       "sudo","yum","install","sysstat"],
#                       shell=False,
#                       stdout=subprocess.PIPE,
#                       stderr=subprocess.PIPE)
#    result = ssh.stdout.readlines()
#    if result == []:
#        error = ssh.stderr.readlines()
#        print ("ERROR: %s" % error)
#    else:
#        print (result)
