
```
s3 = boto3.resource("s3")
```

```
buckets = s3.buckets.all()

for bucket in buckets:
	print(bucket.name)
```

```
with open(file_name, "rb") as f:
	s3.upload_fileobj(f, bucket_name, file_name)

response = s3.list_objects_v2(Bucket=source_bucket)
source_images = [obj["Key"] for obj in response["Contents"]]

response = s3.get_object(Bucket=source_bucket, Key=filename)
image_data = response['Body'].read()
```

```
with open(temp_file, 'rb') as data:
	## copy the grid image to a randomly named object in the destination bucket
	s3.put_object(
				Bucket=destination_bucket,
				Key=destination_key,
				Body=data,
				ContentType='image/jpeg'
			)

```

```
presigned_url = s3.generate_presigned_url("get_object", Params={"Bucket": destination_bucket, "Key": destination_key}, ExpiresIn=5*60)
```

```
lambda_function.py
def lambda_handler(event, context):
```

################################################

```
dynamodb = boto3.client("dynamodb")
dynamodb.put_item(TableName = 'Weather',Item = {
	'Zipcode': {'S': '98103'},
	'Date': {'S': '20230420'},
	'Temperature': {'N': '35'},
	'ChanceRain': {'N': '5'},
	"Conditions": {'S': 'Cloudy'}
})

result = dynamodb.query(
	TableName = 'Weather',
	KeyConditionExpression = "Zipcode = :zipcode AND #date BETWEEN :d1 and :d2",
	ExpressionAttributeNames = {"#date": "Date"},
	ExpressionAttributeValues = {
		":zipcode": {"S": "90210"},
		":d1": {"S": "20230420"},
		":d2": {"S": "20230425"}
	}
)
```
```
response = dynamodb.query(
		TableName = table_name,
		KeyConditions = {
			"uniqueGridId": { "AttributeValueList": [{"S": uniqueGridId}], 'ComparisonOperator': 'EQ'}
		}
	)
```