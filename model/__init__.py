import os
from pynamodb.models import Model
from pynamodb.attributes import *


class OnConnect(Model):
    class Meta:
        table_name = os.getenv("TABLE_NAME_ON_CONNECT")
        aws_access_key_id = os.getenv("DEV_AWS_ACCESS_KEY")
        aws_secret_access_key = os.getenv("DEV_AWS_SECRET_KEY")

    pk = UnicodeAttribute(hash_key=True,)
    sk = UnicodeAttribute(range_key=True)
    connection_object = MapAttribute(null=True)
    connection_date_time = UnicodeAttribute(null=True)

class OnDisconnect(Model):
    class Meta:
        table_name = os.getenv("TABLE_NAME_ON_DISCONNECT")
        aws_access_key_id = os.getenv("DEV_AWS_ACCESS_KEY")
        aws_secret_access_key = os.getenv("DEV_AWS_SECRET_KEY")

    pk = UnicodeAttribute(hash_key=True,)
    sk = UnicodeAttribute(range_key=True)
    connection_object = MapAttribute(null=True)
    connection_date_time = UnicodeAttribute(null=True)

class ActiveConnections(Model):
    class Meta:
        table_name = os.getenv("TABLE_NAME_ACTIVE_CONNECTION")
        aws_access_key_id = os.getenv("DEV_AWS_ACCESS_KEY")
        aws_secret_access_key = os.getenv("DEV_AWS_SECRET_KEY")

    pk = UnicodeAttribute(hash_key=True,)
    sk = UnicodeAttribute(range_key=True)
    connection_object = MapAttribute(null=True)
    connection_date_time = UnicodeAttribute(null=True)


