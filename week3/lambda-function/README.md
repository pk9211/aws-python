# lambda function

## Terminology

* **gridmaker-image-input**: input_bucket where the input images
* **gridmaker-image-destination**: destination_bucket where image grids will be saved; presigned urls for image grids will be shared as output


## Running the GridMaker

```

# setup virtualenv
python3 -m venv path/to/venv
source path/to/venv/bin/activate

# install dependencies
pip3.11 install -r requirements.txt --target ./package

# add dependencies to lambda-function.zip
cd ./package
zip -r ./../lambda-function.zip .

# add lambda function to lambda-function.zip
cd ..
zip lambda-function.zip lambda_function.py

# create aws lambda function

aws lambda create-function \
--function-name grid-maker \
--runtime python3.8 \
--timeout 30 \
--handler lambda_function.lambda_handler \
--role arn:aws:iam::${AWS_ACCOUNT_NO}:role/GridMakerRole  \
--zip-file fileb://~/CODE/aws-python/week3/lambda-function/lambda-function.zip

aws lambda invoke --payload fileb://event.json \
--function-name grid-maker ./output.txt

# logs
aws logs tail /aws/lambda/grid-maker --follow --format json

# deactivate virtualenv
deactivate

```
