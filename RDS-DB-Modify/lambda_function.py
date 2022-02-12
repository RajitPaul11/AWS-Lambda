import boto3 
def lambda_handler(event, context): 
    boto3.client('rds', region_name='ap-south-1').modify_db_instance(DBInstanceIdentifier='terraform-20220212060025260400000001', DBInstanceClass='db.t3.large', ApplyImmediately=True) 
