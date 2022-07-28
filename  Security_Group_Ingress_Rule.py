# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError
import json

AWS_REGION = input("Please enter the AWS_REGION")

# this is the configration for the logger
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

vpc_client = boto3.client("ec2", region_name=AWS_REGION)


def ingress_rule(security_group_id):

    try:
        response = vpc_client.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[{
                'IpProtocol': 'tcp',
                'FromPort': 80,
                'ToPort': 80,
                'IpRanges': [{
                    'CidrIp': '0.0.0.0/0'
                }]
            }, {
                'IpProtocol': 'tcp',
                'FromPort': 22,
                'ToPort': 22,
                'IpRanges': [{
                    'CidrIp': '0.0.0.0/0'
                }]
            }])

    except ClientError:
        logger.exception('It can not be create ingress security group rule.')
        raise
    else:
        return response


if __name__ == '__main__':
    SECURITY_GROUP_ID = input('Enter the Security Group ID')
    logger.info(f'Creating a security group ingress rule...')
    rule = ingress_rule(SECURITY_GROUP_ID)
    logger.info(
        f'Wow!! Your Security group ingress rule has been created: \n{json.dumps(rule, indent=4)}')