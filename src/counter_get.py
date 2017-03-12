import json
import boto3
import io


def handler(event, context):
  dynamodb = boto3.resource('dynamodb')
  
  table = dynamodb.Table('MyTable')
                                              
  results = table.scan()
  
  responseBody = results["Items"]

  return  {
    'statusCode':200,
    'headers':{},
    'body':json.dumps(responseBody)
  }
