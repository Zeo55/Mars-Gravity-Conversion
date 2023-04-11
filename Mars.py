import sys
while True:
    try:
        OGweight = int(input("Enter your weight: "))
        OGweight = OGweight*.3786
        print ("You entered: ", OGweight)
        break;
    except ValueError:
        print ("You entered a character, clown.")