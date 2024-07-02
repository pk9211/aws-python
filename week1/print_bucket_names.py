#!/usr/bin/env python

import boto3

##############
# Resource API
##############

resource = boto3.resource("s3")
buckets = resource.buckets.all()
for bucket in buckets:
	print(bucket.name)
