# AWS Services Scraper
Scrape AWS service information from the [AWS products page](https://aws.amazon.com/products/), upload JSON formatted information to an S3 bucket, and notify subscribers of the new JSON file via an SNS message. 


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
