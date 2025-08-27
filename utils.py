
def palindrome_checker(word):
    word = word.lower()
    for x in range(len(word)//2):
        if word[x] != word[len(word)-1-x]:
            print(word + " is not a palindrome")
            return False
    print(word + " is a palindrome")
    return True
        