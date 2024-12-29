from diagrams import Diagram
from diagrams.aws.compute import Lambda, EC2, ElasticBeanstalk
from diagrams.aws.storage import S3, EFS
from diagrams.aws.database import RDS, Dynamodb, ElastiCache
from diagrams.aws.network import VPC, Route53, CloudFront
from diagrams.aws.security import IAM, WAF, Shield
from diagrams.aws.analytics import Athena, Redshift
from diagrams.aws.management import Cloudwatch

with Diagram("Complex AWS Architecture", show=False):
    vpc = VPC("VPC")
    route53 = Route53("Route 53")
    cloudfront = CloudFront("CloudFront")
    waf = WAF("WAF")
    shield = Shield("Shield")
    
    lambda_function = Lambda("Lambda Function")
    ec2_instance = EC2("EC2 Instance")
    beanstalk = ElasticBeanstalk("Elastic Beanstalk")
    
    s3_bucket = S3("S3 Bucket")
    efs = EFS("EFS")

    rds = RDS("RDS Database")
    dynamodb = Dynamodb("DynamoDB")
    elasticache = ElastiCache("ElastiCache")

    athena = Athena("Athena")
    redshift = Redshift("Redshift")

    cloudwatch = Cloudwatch("CloudWatch")

    iam = IAM("IAM Roles")

    route53 >> cloudfront >> vpc
    vpc >> lambda_function >> dynamodb
    vpc >> ec2_instance >> rds
    s3_bucket >> lambda_function
    dynamodb >> elasticache
    athena >> s3_bucket
    redshift >> dynamodb
    cloudwatch >> [ec2_instance, lambda_function, rds, dynamodb, s3_bucket]
    iam >> [lambda_function, ec2_instance]
    waf >> cloudfront
    shield >> cloudfront
    elasticache >> dynamodb
    efs >> ec2_instance
