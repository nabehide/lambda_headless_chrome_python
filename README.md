# Lambda Headless Chrome
- This is the sample code to run headless chrome on AWS Lambda by Python.
- [Japanese document]()

# How to run
- At first, Create a role which has "AWSLambdaFullAccess" policy.

```
# fetch source code
$ git clone https://github.com/nabehide/lambda_headless_chrome_sample.git
$ cd lambda_headless_chrome_sample

# download headless chrome binary
$ mkdir -p bin/
$ curl -SL https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-37/stable-headless-chromium-amazonlinux-2017-03.zip > headless-chromium.zip
$ unzip headless-chromium.zip -d bin/
$ rm headless-chromium.zip

# download headless chrome driver
$ curl -SL https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip > chromedriver.zip
$ unzip chromedriver.zip -d bin/
$ rm chromedriver.zip

# build docker image
$ docker build -t lambda_headless_chrome_python .

# build package
$ docker run -v "${PWD}":/var/task lambda_headless_chrome_python

# upload package to AWS S3
$ aws s3 cp deploy_package.zip s3://(your_bucket_name)

# create lambda function
$ aws lambda create-function --region ap-northeast-1 --function-name lambda_headless_chrome_python --runtime python3.6 --role $(role_name) --code S3Bucket=$(bucket_name),S3Key=deploy_package.zip --handler lambda_function.lambda_handler --memory-size 512 --timeout 300
```
