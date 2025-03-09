import json

def fuction_one(event, context):
    body = {
            "id": 203,
            "make": "Toyota",
            "model": "Corolla",
            "year": 2021,
            "color": "Blue",
            "mileage": 25000,
            "engineType": "Hybrid",
            "owner": {
                "firstName": "Robert",
                "lastName": "Smith",
                "phone": "+1-555-9876"
            },
            "lastServiceDate": "2024-09-10",
            "isUnderWarranty": False
            }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def fuction_two(event, context):
    body = {
            "id": 305,
            "model": "Bell 407",
            "manufacturer": "Bell Helicopter",
            "year": 2018,
            "maxPassengers": 6
            }


    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
