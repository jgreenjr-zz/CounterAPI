from cfnresponse import send, SUCCESS

def handler(event, context):
   message = 'Hello'
   return  {
     'message' : message
   }
   