
def palindrome_checker(string):
    string = string.lower()
    for x in range(len(string)//2):
        if string[x] != string[len(string)-1-x]:
            print(string + " is not a palindrome")
            return False
    print(string + " is a palindrome")
    return True
        