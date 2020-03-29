#!/bin/python

import math
import os
import random
import re
import sys


# loading data #

""" Usual data transformations:
Understand and conver data
Aggregate Data
Normalize Data
Transform Data
"""

import pandas as pd

data = pd.read_csv(r"D:\dev\large_dataset\cleaning-data-python-data-playbook\artwork_data.csv", )
data.head()


data = pd.read_json(r"D:\dev\large_dataset\simple_json.json", orient='columns' )
print(data)

data = pd.read_clipboard()

data = pd.read_parquet(r"D:\download\userdata1.parquet")
print(data)