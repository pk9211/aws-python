#!/usr/bin/env python

import boto3

# Indicate s3 service
s3 = boto3.client('s3')

# Bucket and file
bucket_name = 'seph0410'
file_name = 'seph.jpeg'

# upload to s3
with open(file_name, "rb") as f:
	s3.upload_fileobj(f, bucket_name, file_name)
