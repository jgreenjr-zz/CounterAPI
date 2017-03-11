def handler(event, context):
   message = 'Hello'
   context.done(None, {
     'message' : message
   })