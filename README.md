# This project does an analysis of the resource usage of the nodes on AWS cluster

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

