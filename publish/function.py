# coding=utf-8
import os, json, boto3, botocore

config = boto3.client('s3')._client_config
config.signature_version = botocore.UNSIGNED

s3 = boto3.client('s3', config=config)
sns = boto3.client('sns')

topic = os.environ['topic']

def lambda_handler(event, context):
  print(event);
  
  for record in event['Records']:
      bucket = record['s3']['bucket']['name']
      key = record['s3']['object']['key'] 
  
      url = s3.generate_presigned_url('get_object', ExpiresIn=0, Params={'Bucket': bucket, 'Key': key})
    
      message = {'default':url}
      response = sns.publish(TopicArn=topic, MessageStructure='json', Message=json.dumps(message), Subject='AWS Services Update Notification')

  return "Published AWS Services Update Notification"