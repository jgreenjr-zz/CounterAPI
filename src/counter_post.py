import json
import boto3
import io


def handler(event, context):
  body = json.loads(event['body'])
  dynamodb = boto3.resource('dynamodb')
  
  table = dynamodb.Table('MyTable')
                                              
  table.put_item({
    'UserName': body['UserName']
  })
  
  responseBody = {"message":"Created {0}".format(body['UserName'])}

  return  {
    'statusCode':201,
    'headers':{},
    'body':json.dumps(responseBody)
  }