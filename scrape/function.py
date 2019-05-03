# coding=utf-8
import os, re, json, boto3

from bs4 import BeautifulSoup
from requests import get

bucket = os.environ['bucket']
key = 'aws-services.json'

s3 = boto3.client('s3')

def lambda_handler(event, context):

  categories = []

  raw = get('https://aws.amazon.com/products/')
  soup = BeautifulSoup(raw.content, 'html.parser')
  
  # Scrape the products page
  for cat_item in soup.select("div.lb-item-wrapper"):
    cat_name = cat_item.find("a").find("span", recursive=False).text.strip()
    category = {"name": cat_name, "children":[]}

    category_services = cat_item.findAll("div", { "class" : "lb-content-item" })
    for category_service in category_services:
      service_name = category_service.find("a").find(text=True, recursive=False).strip()
      service_description = category_service.find("a").find("span", recursive=False).text.strip()
      service_link = "https://aws.amazon.com" + category_service.find('a').attrs['href'].split("?")[0].strip()

      category["children"].append({"name": service_name, "description": service_description, "link": service_link, 'group':cat_name})

    categories.append(category)
  
  response = s3.put_object(
    ACL='public-read',
    ContentType='text/json',
    Body=json.dumps({'name':'AWS', 'children':categories}),
    Bucket=bucket,
    Key=key)
    
  return "s3://%s/%s" % (bucket, key)