try:
    import json
    import json
    import boto3
    import base64
    import os
    import datetime
    import uuid
    from datetime import datetime

    from model import OnConnect, OnDisconnect, ActiveConnections
except Exception as e:
    print("Error : {} ".format(e))


def connect_handler(event, context):

    connection_id = event.get("requestContext", {}).get("connectionId")
    if connection_id is None:
        return {"statusCode": 400, "body": "Bad Request"}

    OnConnect(
        pk=f"onconnect#{connection_id.__str__()}",
        sk=f"onconnect#{connection_id.__str__()}",
        connection_object=event,
        connection_date_time=datetime.now().__str__()
    ).save()

    ActiveConnections(
        pk=f"Active#{connection_id.__str__()}",
        sk=f"Active#{connection_id.__str__()}",
        connection_object=event,
        connection_date_time=datetime.now().__str__()
    ).save()

    return {"statusCode": 200, "body": "ok"}


def disconnect_handler(event, context):

    connection_id = event.get("requestContext", {}).get("connectionId")

    if connection_id is None:
        return {"statusCode": 400, "body": "Bad Request"}

    OnDisconnect(
        pk=f"onDisconnect#{connection_id.__str__()}",
        sk=f"onDisconnect#{connection_id.__str__()}",
        connection_object=event,
        connection_date_time=datetime.now().__str__()
    ).save()

    id = f"Active#{connection_id.__str__()}"

    for item in ActiveConnections.query(str(id)):
        item.delete()

    return {"statusCode": 200, "body": "ok"}


def get_live_users():
    count = 0
    for item in ActiveConnections.scan():
        count = count + 1
    return count

def get_active_live_users():
    data = []

    for item in ActiveConnections.scan():
        data.append(
            {
                "pk":item.pk,
                "sk":item.sk
            }
        )
    return data

def get_live_users_handler(event, context):

    print("event", event)
    body  =  json.loads(event.get("body"))
    action = body.get("action")
    message =  body.get("message")

    connection_id = event.get("requestContext", {}).get("connectionId")
    if connection_id is None:
        return {"statusCode": 400, "body": "Bad Request"}

    if action.strip().lower() == "onGetLiveUsers".lower():
        count = get_live_users()
        return {"statusCode": 200, "body": json.dumps({
            "total_live_users":str(count),
            "event":"onGetLiveUsers"
        }) }

    if action.strip().lower() == "onGetActiveUsers".lower():
        data = get_active_live_users()
        return {"statusCode": 200, "body": json.dumps({
            "users":data,
            "event":"onGetActiveUsers"
        })}

    return {"statusCode": 400, "body": "Bad Request"}



