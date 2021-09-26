#!/usr/bin/python3


def main():
    d = (1, 2, 3) # tuple
    d = [1, 2, 3] # list
    d.append(0) # class method append for list class object
    d.insert(0, 7) # class method insert for list class object
    print(d, type(d))
    d = 'string' # string assignment
    print(type(d), d[2:4], d) #string splicing

    d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5} #dictionary assingnment of string key to integer value
    d['six'] = 6 #single assignment of a dictionary key to value
    for k in sorted(d.keys()): #sorted(d.keys()) organises key values alphabetically
        print(k, d[k])
    d = dict(
        one = 1,
        two = 2,
        three = 3,
        four = 4,
        five = 5,
        six = 6
        )
    # more convenient dictionary key-value assignment
    d['seven'] = 7 #manual key-value assignment
    for k in d:
        print(type(d), type(d[k]), d[k], k) #k, d[k]

if __name__ == "__main__": main()
