#!/usr/bin/python3

class AnimalActions():
    def quack(self): return self.strings['quack']
    def feathers(self): return self.strings['feathers']
    def bark(self): return self.strings['bark']
    def fur(self): return self.strings['fur']

class Duck(AnimalActions):
    strings = dict(
        quack = "The duck goes quack",
        feathers = "The duck has grey feathers",
        bark = "The duck does not bark",
        fur = "The duck loves to rustle fur"
        )

def main():
    donald = Duck()
    print(donald.quack())
    print(donald.bark())
    print(donald.fur())

if __name__ == "__main__": main()