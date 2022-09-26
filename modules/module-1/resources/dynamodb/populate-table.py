import boto3
import json
import time
import os

#session=boto3.Session(aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'], aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'], aws_session_token=os.environ['AWS_SESSION_TOKEN'])
session=boto3.Session(profile_name='820379311794_AWSAdministratorAccess')

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

time.sleep(5)
table_1 = dynamodb.Table('blog-users')
db_file_json_1 = open('modules/module-1/resources/dynamodb/blog-users.json')
db_file_1 = json.loads(db_file_json_1.read())
for db_item_1 in db_file_1:
    table_1.put_item(Item=db_item_1)

table_2 = dynamodb.Table('blog-posts')
db_file_json_2 = open('modules/module-1/resources/dynamodb/blog-posts.json', encoding='utf8')
db_file_2 = json.loads(db_file_json_2.read())
for db_item_2 in db_file_2:
    table_2.put_item(Item=db_item_2)

print("Items Updated")
