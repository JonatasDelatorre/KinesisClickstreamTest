import base64
import boto3
import json
import os

def handler(event, context):

    print(event)

    try:
        topic_arn = os.environ['TOPIC']

        data = event['Records'][0]['kinesis']['data']
        message = base64.b64decode(data).decode("utf-8")
        print(data)
        print(message)
        
        session = boto3.Session()
        sns = session.client('sns')
        
        response = sns.publish(
            TopicArn=topic_arn,
            Message=json.dumps(event),
            Subject='ClickStream',
        )

        # Escrever código para mandar dados para o S3

    except Exception as e:
        print(e)
        raise e