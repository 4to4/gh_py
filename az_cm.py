"""
from azure.cosmosdb.table import TableService

the_connection_string = "DefaultEndpointsProtocol=https;AccountName=devrite;AccountKey=luOiUUGRBDQtNpKWMnujP2inlKJ5TtUqmlIjVUnzIK9S5LuKKwRTXW6hxtFvJvjE0vOtZ7Qcij36CmuTyB4t6g==;TableEndpoint=https://devrite.table.cosmos.azure.com:443/;"
TableService(endpoint_suffix = "table.cosmos.azure.com", connection_string= the_connection_string)

print(the_connection_string)

"""

from math import factorial
from pprint import pprint as prt
import sys

def getc():
    sys.stdin.read(1)



def gen1():
    for i in range(10):
        yield i
    return

for cnt in gen1():
    getc()
    prt(cnt)


