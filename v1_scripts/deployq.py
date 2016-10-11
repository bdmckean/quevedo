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

## parse input for string and keyfile


## get list of AWS hosts for account


## from list find instance names matching string


## from this list ssh into machines using IP address
##  Install monitor software

## FIXME -- change this bash script to python
for i in "${machines[@]}"
do
    ssh root@$i "yum -y install sar"

done
