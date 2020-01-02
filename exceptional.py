import sys
from math import log

def string_log():
    v = 0
    try:
        v = v/0
    except (ZeroDivisionError, ValueError ) as e:
        # print("Cannot divide by zero", e.__str__)
        print(f"{e!r}", file=sys.stderr)
        raise

string_log()


