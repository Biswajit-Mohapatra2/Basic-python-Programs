import boto3

s3 = boto3.resource('s3')
ec2 = boto3.resource('ec2')

for bucket in s3.buckets.all():
    print(bucket)

for instance in ec2.instance.all():
    print(instance)

s3.Bucket("#your bucket name".download_file("#filename", "#which name you want to save in your system" )) #For Downloading file from AWS S3 Bucket