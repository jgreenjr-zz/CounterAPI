import json
import boto3
import io


def handler(event, context):
  dynamodb = boto3.resource('dynamodb')
  
  table = dynamodb.Table('MyTable')
                                              
  table.put_item({
    'UserName': event['UserName']
  })
  
  responseBody = {"message":"success"}

  return  {
    'statusCode':201,
    'headers':{},
    'body':json.dumps(responseBody)
  }