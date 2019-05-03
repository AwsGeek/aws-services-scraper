#!/bin/bash
region=$1
lambdabucket=$2
stackname=$3

aws --region $region cloudformation package --template-file template.yaml --s3-bucket $lambdabucket --output-template-file package.yaml
aws --region $region cloudformation deploy --template-file package.yaml --stack-name $stackname --capabilities CAPABILITY_IAM