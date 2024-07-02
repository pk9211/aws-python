# aws-python

**Course**: https://www.coursera.org/learn/integrate-aws-sdk/home/info

## Useful Python Dependencies

1. Pillow: https://pillow.readthedocs.io/en/stable/index.html
2. Boto3: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

## Useful AWS Links:

1. https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html

## Useful AWS Commands

```
aws sts get-caller-identity --query Account --output text
```

## API Gateway Test

```
curl -XGET 'https://5mo1fe1lq3.execute-api.us-east-1.amazonaws.com/hello-world'
Hello World
```

1. JWT authorizor: OIDC (Amazon Cognito)

2. Lambda authorizor: custom authentication code in a lambda function. When an endpoint from API Gateway is invoked, the API Gateway invokes the lambda function and uses the response to determine whether or not to allow the request.

3. IAM authorizor: use signature version 4 to sign requests# aws-python
