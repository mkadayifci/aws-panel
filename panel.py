import boto3

print 'Starting RDS'



client = boto3.client('rds', region_name='eu-central-1')

response = client.start_db_instance(
    DBInstanceIdentifier='log2up'
)


print 'RDS started'
