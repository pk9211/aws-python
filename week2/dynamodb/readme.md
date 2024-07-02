# dynamodb


```
$  python3 -m venv path/to/venv

$  source path/to/venv/bin/activate

(venv) $ pip3 install -r requirements.txt
Collecting boto3==1.34.86 (from -r requirements.txt (line 1))
  Using cached boto3-1.34.86-py3-none-any.whl.metadata (6.6 kB)
Collecting botocore<1.35.0,>=1.34.86 (from boto3==1.34.86->-r requirements.txt (line 1))
  Using cached botocore-1.34.87-py3-none-any.whl.metadata (5.7 kB)
Collecting jmespath<2.0.0,>=0.7.1 (from boto3==1.34.86->-r requirements.txt (line 1))
  Using cached jmespath-1.0.1-py3-none-any.whl.metadata (7.6 kB)
Collecting s3transfer<0.11.0,>=0.10.0 (from boto3==1.34.86->-r requirements.txt (line 1))
  Using cached s3transfer-0.10.1-py3-none-any.whl.metadata (1.7 kB)
Collecting python-dateutil<3.0.0,>=2.1 (from botocore<1.35.0,>=1.34.86->boto3==1.34.86->-r requirements.txt (line 1))
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting urllib3!=2.2.0,<3,>=1.25.4 (from botocore<1.35.0,>=1.34.86->boto3==1.34.86->-r requirements.txt (line 1))
  Using cached urllib3-2.2.1-py3-none-any.whl.metadata (6.4 kB)
Collecting six>=1.5 (from python-dateutil<3.0.0,>=2.1->botocore<1.35.0,>=1.34.86->boto3==1.34.86->-r requirements.txt (line 1))
  Using cached six-1.16.0-py2.py3-none-any.whl.metadata (1.8 kB)
Using cached boto3-1.34.86-py3-none-any.whl (139 kB)
Using cached botocore-1.34.87-py3-none-any.whl (12.2 MB)
Using cached jmespath-1.0.1-py3-none-any.whl (20 kB)
Using cached s3transfer-0.10.1-py3-none-any.whl (82 kB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached urllib3-2.2.1-py3-none-any.whl (121 kB)
Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: urllib3, six, jmespath, python-dateutil, botocore, s3transfer, boto3
Successfully installed boto3-1.34.86 botocore-1.34.87 jmespath-1.0.1 python-dateutil-2.9.0.post0 s3transfer-0.10.1 six-1.16.0 urllib3-2.2.1

(venv) $ python3 main.py
{'Items': [], 'Count': 0, 'ScannedCount': 0, 'ResponseMetadata': {'RequestId': 'DJQ5482KAPDE18QMTNTB07ETPVVV4KQNSO5AEMVJF66Q9ASUAAJG', 'HTTPStatusCode': 200, 'HTTPHeaders': {'server': 'Server', 'date': 'Thu, 18 Apr 2024 23:32:32 GMT', 'content-type': 'application/x-amz-json-1.0', 'content-length': '39', 'connection': 'keep-alive', 'x-amzn-requestid': 'DJQ5482KAPDE18QMTNTB07ETPVVV4KQNSO5AEMVJF66Q9ASUAAJG', 'x-amz-crc32': '3413411624'}, 'RetryAttempts': 0}}
```
