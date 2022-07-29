## Create a AWS security Group Ingress  rule  using boto3.

#### A security group acts as a virtual firewall for your EC2 instances to control incoming and outgoing traffic. Inbound rules control the incoming traffic to your instance, and outbound rules control the outgoing traffic from your instance. An inbound rule permits instances to receive traffic from the specified IPv4 or IPv6 CIDR address range, or from the instances associated with the specified security group. You can follow this [link](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule-1.html) to know more.

-------------

**Files:** 
```
    Security_Group_Ingress_Rule.py
```

## Apply the script

1. First configure the aws credentials using aws-cli.

        aws configure

2. Now, from the current directory run the following command to create  Security Group Ingress Rule.

        python3  Security_Group_Ingress_Rule.py
