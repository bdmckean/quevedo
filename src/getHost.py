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

from ec2rest import ec2RestSend
import pprint
import xmltodict

e = ec2RestSend()
ans = e.sendEc2Rest('DescribeInstances')

if (ans):
    ans_dict = xmltodict.parse(ans)
    pprint.pprint(ans_dict)
    #print("len=: ",len(ans_dict["DescribeInstancesResponse"])) 
    #print("len=: ",len(ans_dict["DescribeInstancesResponse"]["reservationSet"])) 
    #print("len=: ",len(ans_dict["DescribeInstancesResponse"]["reservationSet"]["item"])) 
    #print("len=: ",len(ans_dict["DescribeInstancesResponse"]["reservationSet"]["item"][0])) 
    #print("len=: ",len(ans_dict["DescribeInstancesResponse"]["reservationSet"]["item"][0]["instancesSet"])) 
    for key, value in ans_dict["DescribeInstancesResponse"]["reservationSet"]["item"][0]["instancesSet"]["item"].items() :
        print ("key: ",key, "\n", "value: ", value, "\n")
    for key, value in ans_dict["DescribeInstancesResponse"]["reservationSet"]["item"][1]["instancesSet"]["item"].items() :
        print ("key: ",key, "\n", "value: ", value, "\n")
    #pprint.pprint(ans_dict["DescribeInstancesResponse"]["reservationSet"])
    ret = "# Set of instances in AWS \n"
    for i in range(len(ans_dict["DescribeInstancesResponse"]["reservationSet"]["item"])):
        dns = ans_dict["DescribeInstancesResponse"]["reservationSet"]["item"][i]["instancesSet"]["item"]["dnsName"]
        ipAddr = ans_dict["DescribeInstancesResponse"]["reservationSet"]["item"][i]["instancesSet"]["item"]["ipAddress"]
        instanceName = ans_dict["DescribeInstancesResponse"]["reservationSet"]["item"][i]["instancesSet"]["item"]["tagSet"]["item"]["value"]
        ret += ipAddr + "\t" + dns + "\t" + "# " + instanceName + "\n"
    print ("##----------------------------------------------------##")
    print (ret)
else:
    print("Got no response")


