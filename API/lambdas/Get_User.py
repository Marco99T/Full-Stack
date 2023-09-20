import json
from cognito.get_user import Get_User

def lambda_handler(event, context):
    body = json.loads(event['body'])
    accesstoken = body['token']

    response = Get_User(accesstoken)
    if response != 'Expired':
        return{
            'statusCode': 200,
            'body': json.dumps(response)
        }
    else:
        return{
            'statusCode': 400,
            'body': json.dumps(f'Token invalido: {response}')
        }