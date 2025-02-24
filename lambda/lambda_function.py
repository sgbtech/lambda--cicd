import json

def lambda_handler(event, context):
  return {
    'statusCode': 200,
    'body': json.dumps('Hello from CICD lambda, last change today the 24.02.2025')
    }
