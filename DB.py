from boto3 import resource
from boto3.dynamodb.conditions import Attr ,  Key

table = resource('dynamodb').Table('Users')

def insert_user():
    response= table.put_item(

        Item={
            
        "userid":"6"
        ,
        "Address":"sagar",
        "FirstName": "amanishan",
        "flat": ""
        ,
        "FlatVisit": "204"
        ,
        "LastName": "Kumar"
        ,
        "LoginType": "Visitor"
        ,
        "Password": ""
        ,
        "Phone":7000898974
        ,
        "Username": ""
      }

        
    )
    return response


result=insert_user()
print(result)