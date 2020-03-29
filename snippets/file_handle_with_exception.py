import os
import sys

try:
    with open(r"D:\dev\large_dataset\titanic.csv",'r',encoding='utf-8',buffering=10) as f:
        for line in f:
            print(f"Line {line}")
            sys.stdin.read(1)
except OSError as e:
    print(f"Error is {e!r}")
except Exception as e:
    print(f"Err : {sys.exc_info()[1]}")




