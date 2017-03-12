from cfnresponse import send, SUCCESS

def handler(event, context):
   message = 'Hello'
   send(event, context, SUCCESS,  {
     'message' : message
   }) 
   