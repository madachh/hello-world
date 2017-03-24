def is_palindrome(word):
    """
    The function is_palindrome checks if a word is a palindrome
    :param word:an inserted word that is goind to be checked whether it is a palindrome
    :return: the function is going to return a boolean value station
    whether it is true that the inserted word is a palindrome or if
     it is False and the word is not a palindrome
    """
    word=make_alpha(word)
    for n in range(len(word)):
        if word[n]!= word[-n-1]:
            return False
    return True


def make_alpha (word):
    """
    The function make_alpha constructs the new word out of the palindrome word
    :param word:the inserted word that  is going to be made into the new palindrome word
    :return: the function returns the new word made out of the palindrome word
    """
    new_word=""
    for letter in word:
        if letter.isalpha():
            new_word=new_word+letter
    return new_word


def main():
    s=input("Type a word: ")
    result=is_palindrome(s)
    if result==True:
        print("The inserted word is a palindrome")
    else:
        print("The inserted word is not a palindrome")

main()


