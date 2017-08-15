import boto3

client = boto3.client('rds', region_name='eu-central-1')


response = client.describe_db_instances(
    DBInstanceIdentifier='log2up'
)

current_status = response['DBInstances'][0]['DBInstanceStatus']
print 'Current: ' + current_status

if current_status=='stopped':
    print 'Starting...'
    response = client.start_db_instance(
        DBInstanceIdentifier='log2up'
    )
    print 'Started!'

if current_status=='available':
    print 'Stopping...'
    response = client.stop_db_instance(
        DBInstanceIdentifier='log2up'
    )
    print 'Stopped!'
