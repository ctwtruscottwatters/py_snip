#!/usr/bin/python3

def main():
    try:
        file_handle = open('scratchpad.cpp')
        for line in file_handle.readlines():
            print(line, end='\n')
    except IOError as e:
        print("Something bad happened: {}".format(e))

if __name__ == "__main__": main()