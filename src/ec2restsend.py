#!/usr/bin/env python3

# Coptyright 2016 (c) Brian McKean

'''
    File name: ex2restsend.py
    Author: Brian McKean
    Date created: 08/31/2016
    Date last modified: 09/02/2016
    Python Version: 3.5
 
'''
# TODO:
# 1) Unit test framework
#   create instance
#   get instance stats
#   delete instance
#   verify isntance deleted
# 2) more options on input
# -- region, commands
# 3) pass through on unrecognized message with warning
#
# imports
import os
import datetime
import logging
import pprint

import hmac
import hashlib

import requests
import xmltodict

# code 


class ec2RestSend(object):
    def __init__(self):
        self.service = 'ec2'
        self.host = 'ec2.amazonaws.com'
        self.region = 'us-east-1'
        self.dest = 'https://ec2.amazonaws.com'
        self.request = None
        self.method = None

    def sign(self, key, msg):
        return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

    def getSignatureKey(self, key, dateStamp ):
        kDate = self.sign(('AWS4' + key).encode('utf-8'), dateStamp)
        kRegion = self.sign(kDate, self.region)
        kService = self.sign(kRegion, self.service)
        kSigning = self.sign(kService, 'aws4_request')
        return kSigning

    def sendEc2Rest(self, op):
        if op == 'DescribeInstances':
            self.request = 'Action=DescribeInstances&Version=2013-10-15'
        else:   
            logging.warnings('Unsupported Request =',str(op))
            return None 
        
        self.method = 'GET'
        # Read AWS access key from env. variables or configuration file. Best practice is NOT
        # to embed credentials in code.
        access_key = os.environ.get('AWS_ACCESS_KEY_ID')
        secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
        if access_key is None or secret_key is None:
            logging.warnings('No access key is available.')
            return None

        # Create a date for headers and the credential string
        t = datetime.datetime.utcnow()
        amzdate = t.strftime('%Y%m%dT%H%M%SZ')
        datestamp = t.strftime('%Y%m%d') # Date w/o time, used in credential scope
        
        # Request
        # Not sure why but this fails without 2 newlines after amzdate
        myRequest = self.method + '\n'                        \
                + '/' + '\n'                                  \
                + self.request + '\n'                       \
                + 'host:' + self.host + '\n'                \
                + 'x-amz-date:' + amzdate + '\n'  + '\n'    \
                + 'host;x-amz-date' + '\n'                  \
                + hashlib.sha256(''.encode('utf-8')).hexdigest()

         
        #  CREATE THE STRING TO SIGN*************
        algorithm = 'AWS4-HMAC-SHA256'
        credential_scope = datestamp + '/' + self.region + '/' + self.service + '/' + 'aws4_request'
        string_to_sign = algorithm + '\n'                   \
                        +  amzdate + '\n'                   \
                        +  credential_scope + '\n'          \
                        +  hashlib.sha256(myRequest.encode('utf-8')).hexdigest()


        # Signe the string
        signing_key = self.getSignatureKey(secret_key, datestamp)
        signature = hmac.new(signing_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()

        # Create authorization header and add to request headers
        signed_headers = 'host;x-amz-date'
        authorization_header = algorithm + ' '                                              \
                            + 'Credential=' + access_key + '/' + credential_scope + ', '    \
                            + 'SignedHeaders=' + signed_headers + ', '                      \
                            + 'Signature=' + signature  

        headers = {'x-amz-date':amzdate, 'Authorization':authorization_header}

        #print(authorization_header)
        request_url = self.dest + '?' + self.request
        #print("Request URL=",request_url)
        #print(request_url, "headers=",headers)
        ans = requests.get(request_url, headers=headers)

        #print(ans.text)

        return ans.text

######
# Unit test code
# Fixmw: Add unit test framework
if __name__ == "__main__":
    e = ec2RestIf()
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
    
