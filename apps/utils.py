# coding: utf8
from datetime import datetime
from uuid import uuid4


def create_id(identifier):
    id_base = "{}_{}{}"
    now = datetime.utcnow()
    date_string = now.strftime("%Y%m%d%H%M%S")
    id_base = id_base.format(
        identifier,
        date_string,
        str(uuid4())[:8]
    )
    return id_base
