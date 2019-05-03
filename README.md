# AWS Services Scraper
Periodically (daily) scrape AWS service information from the [AWS products page](https://aws.amazon.com/products/), upload the JSON formatted information to an S3 bucket, and then notify subscribers that a new JSON file is available via an SNS message. 

Interesting bits:
* A periodic CloudWatch Event triggers a Lambda function that scrapes information from a web page, then uploads the information to an S3 bucket.
* The S3 bucket triggers a Lambda function that uses SNS not notify subscribers of the updated information.
* A Lambda Layer is used to consolidated shared dependences between multiple Lambda functions.
* The Cloudformation stack has to be built in 2 steps. See NOTE below.

TO BUILD:
```
cd scrape
pip install -r requirements.txt -t .
cd ..

cd shared
pip install -r requirements.txt -t .
cd ..

cd ..
./build.sh <region> lambda-bucket> <stack-name> (see NOTE below)
```

WHERE:
```
  region - is the AWS region you'll deploy this stack to
  lambda-bucket - is used by cloudformation as a staging area for the lambda function
  stack-name - is the name you'd like to use for the cloudformation stack
```

NOTE: Because of circular dependencies between the S3 bucket, IAM permissions, and the Lambda function, the stack needs to be built in 2 steps. In step 1, remove the S3 bucket trigger from the bucket definition in template.yaml and build. In step 2, replace the S3 bucket trigger and rebuild.
