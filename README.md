# This project does an analysis of the resource usage of the nodes on AWS cluster
## Project Goals
This project is a collection of scripts and tools to monitor the resource usage in the data nodes and name nodes in a hadoop cluster while running a map reduce job. In addition there are scripts for automated extraction and collation of reports.  Once the entire deployment, intrumentation, extraction and collation process is complete I will add an automated analysis of the results so that for a given tyoe of workload the optimal cluster configuration in terms of type of nodes and number of nodes can be recommended.

## Project Origins
### Hadoop cluster testing with 2, 5 and 10 nodes against standard benchmarks

In this project report I instrumented and examined individual server resource usage in a haddop cluster with 2,5 and 10 nodes. I gathered data on how resources where used and analyzes optimal cluster configuration for each job.

This was a project I did for a graduate course in distributed computing I took at the University of Colorado
[a relative link](other_file.md)

The results showed an optimal price / performance occuring at five nodes.


### Project Status

The adding of the instrumenation software to the cluster was a time consumeing task in the original project. The first part of this project is to develop software to automate the process. I have some of the initial scripts working but this project is on hold at the moment.

## Project work not yet started

We will require some type of machine learning process to look at results from test runs to be able to recommend an opimal setup.  We will also require many more test runs with various configurations.



# General outline of current project exeuction steps

## Load spark on aws using 
https://github.com/amplab/spark-ec2

(Note that this also sets up hadoop under spark -- and looks like the easiest way to set up a hadoop cluster in AWS)

### spin up spark cluster
export AWS_SECRET_ACCESS_KEY=...

export AWS_ACCESS_KEY_ID=.....

./spark-ec2 --key-pair=awskey --identity-file=awskey.pem --region=us-west-1 --zone=us-west-1a launch my-spark-cluster

### Delpoy scripts to cluster


### Start monitor and job


### When job finishes extract stats

