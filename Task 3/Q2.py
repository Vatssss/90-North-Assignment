# AWS Lambda function to upload a document to S3
import boto3
import base64

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'your-bucket-name'
    file_content = base64.b64decode(event['file'])
    file_name = event['filename']
    
    s3.put_object(Body=file_content, Bucket=bucket_name, Key=file_name)
    return {"message": "File uploaded successfully"}
