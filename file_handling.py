import os
p = r'c:\Users\root\Desktop\ahishekS_agile1.jpg' # raw string

try:
    if os.path.exists(p):
        print("True")
    else:
        print("False")
        print(p.__str__)
except OSError as e:
    print(f"Error: {e!r}")
    raise
finally:
    print("Yo finally")
