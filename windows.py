"""keypress - detect a keypress"""

try:
    import msvcrt
    def getkey():
        print(msvcrt.getch())
except ImportError:
    import sys
    import tty
    import termios

    def getkey():
        fd = sys.stdin.fileno()
        try:
            print(fd)
            ch = sys.stdin.read(1)
        finally:
            print("Caught the char key stroke")
        return ch
         


if __name__ == "__main__":
    getkey()