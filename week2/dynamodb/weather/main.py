#!/usr/bin/env python3

import boto3

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

print(result)
