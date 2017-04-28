
import os

class Bad(Exception):
    pass

def doomed():
    raise Bad();


def main():
    try:
        doomed();
    except Bad:
        print("Catch Bad")


if __name__ == "__main__":
    main();
