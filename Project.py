def is_palindrome(word):
    """
    Narrative of the function: checks if a word is a palindrome
    :param word:
    :return:
    """
    word=make_alpha(word)
    for n in range(len(word)):
        if word[n]!= word[-n-1]:
            return False
    return True


def make_alpha (word):
    new_word=""
    for letter in word:
       if letter.isalpha():
          new_word=new_word+letter
    return new_word
make_alpha("Apple")
print(make_alpha("Apple"))


