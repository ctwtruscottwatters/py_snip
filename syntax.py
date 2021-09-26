#!/usr/bin/python3

class Egg:
    def __init__(self, kind = "fried"):
        self.kind = kind
    def what_kind(self):
        return self.kind

def main():
    fried = Egg()
    print(fried.what_kind())
    scrambled = Egg(kind='scrambled')
    print(scrambled.what_kind())

if __name__ == "__main__": main()
