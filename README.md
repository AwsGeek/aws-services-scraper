# AWS Services Scraper
Scrape AWS service information from the [AWS products page](https://aws.amazon.com/products/), upload JSON formatted information to an S3 bucket, and notify subscribers of the new JSON file via an SNS message. 


TO BUILD:
```
cd scrape
pip install -r requirements.txt -t .
cd ..

cd publish
pip install -r requirements.txt -t .
cd ..

cd ..
./build.sh <region> lambda-bucket> <stack-name> <bucket> <key>
```

WHERE:
```
  region - is the AWS region you'll deploy this stack to
  lambda-bucket - is used by cloudformation as a staging area for the lambda function
  stack-name - is the name you'd like to use for the cloudformation stack
```
