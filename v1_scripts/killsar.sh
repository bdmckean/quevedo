#!/bin/bash
#
# Copyrtight 2016 (c) Brian McKean
#
# This runs on each host and stops the logging process when the 
# under measurement is comlete.

# find the sar processes running and stop them
ps -ef | grep sar | awk '{print $2}' | xargs kill
