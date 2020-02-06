import json
import boto3

def lambda_handler(event, context):
    print(event)
    
    bucket = event['Records'][0]['s3']['bucket']
    object = event['Records'][0]['s3']['object']
    
    print("reading resource {}/{}".format(bucket['name'],object['key']))
    s3 = boto3.resource('s3')
    s3file = s3.Object(bucket['name'],object['key'])
    file_content = s3file.get()['Body'].read()
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Function Complete')
    }
