import json

def lambda_handler(event, context):
  return {
    'statusCode': 200,
    'body': json.dumps('Hello from CICD lambda, today is the 24.02.2025')
    }
