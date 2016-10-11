#!/usr/bin/env python3

# Coptyright 2016 (c) Brian McKean

'''
    File name: getHost.py
    Author: Brian McKean
    Date created: 08/31/2016
    Date last modified: 09/02/2016
    Python Version: 3.5


    Gets a list of IPs and dns names for a set of ec2 instances

    input: None = gets all hoste
           names = gets a list of hosts that match the name qualifier

    output: stdout list of hosts by
            ip_address  dns_name    # host_name
 
'''    

from ec2restsend import ec2RestSend
import xmltodict
import re
import sys

def getHost(match_string=None):
    e = ec2RestSend()
    ans = e.sendEc2Rest('DescribeInstances')
    if (match_string):
        m = re.compile(match_string)


    if (ans):
        match = False
        ans_dict = xmltodict.parse(ans)
        ret = "# Set of instances in AWS \n"
        for i in range(len(ans_dict["DescribeInstancesResponse"]["reservationSet"]["item"])):
            dns = ans_dict["DescribeInstancesResponse"]["reservationSet"]["item"][i]["instancesSet"]["item"]["dnsName"]
            ipAddr = ans_dict["DescribeInstancesResponse"]["reservationSet"]["item"][i]["instancesSet"]["item"]["ipAddress"]
            instanceName = ans_dict["DescribeInstancesResponse"]["reservationSet"]["item"][i]["instancesSet"]["item"]["tagSet"]["item"]["value"]
            if (match_string is None):
                match = True
                ret += ipAddr + "\t" + dns + "\t" + "# " + instanceName + "\n"
            else:
                if (m.search(instanceName)):
                    match = True
                    ret += ipAddr + "\t" + dns + "\t" + "# " + instanceName + "\n"
        
        if (match == False):
            if match_string is None:
                ret += "No instances were returned\n"
            else:
                ret += "No instances matching "+match_string+" were found\n"
        return "##----------------------------------------------------##\n"+ret
    else:
        return "Got no response\n"



############
if __name__ == "__main__":
    ans = "Error processing getHost.py"
    if (len(sys.argv) > 2):
        ans = "usage: getHost.py [match_string]"
    elif (len(sys.argv) == 2):   
        match_string = sys.argv[1]
        ans = getHost(match_string)
    else:
        ans = getHost()

        
    print(ans)
