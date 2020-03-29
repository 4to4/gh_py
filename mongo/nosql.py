from pymongo import MongoClient
from pprint import pprint
import json as js
from random import randint
import sys
import logging


# connect to mongo db

def get_dbo(dbh, db):
    try:
        return MongoClient(dbh).db
    except Exception as e:
        print(f"Could not connect to {dbh} due to [{e!r}]")
        return None

    # dbh = MongoClient('localhost:27017')
    # dbo = dbh.business
    # serverStatusResult = dbo.command("serverStatus")
    # pprint(serverStatusResult)


def main():
    # set logging level
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)

    #global config
    dbh='localhost:27017'
    db='business'
    dbo = get_dbo(db=db, dbh=dbh)
    assert dbo is None, "Exiting"
    pprint(dbo.command("serverStatus"))


if __name__ == "__main__":
    main()
