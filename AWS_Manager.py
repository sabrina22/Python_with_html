import boto3
import json
class AWSManager:
    def __init__(self):
        s3_client = boto3.client('s3')

    def save_to_s3():
        boto3.client('s3').upload_file('demo.html', 'lmtd-class', 'demo.html')

    def load_from_s3():
        boto3.client('s3').download_file('lmtd-class', 'demo.html', 'demo.html')

    def read_from_s3():
        obj = boto3.resources('s3').Object('lmtd-class', 'heyshefan.json')
        print(type(obj))
        data = json.load(obj.get()['body'])
        print(data)

