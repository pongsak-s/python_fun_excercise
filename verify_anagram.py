
from string import ascii_lowercase as lchars


def checkAnagram(words, anagram):

    # setup
    dictLchars = {x_i: 0 for x_i in lchars}
    dictLchars_ana = {x_i: 0 for x_i in lchars}
    words = words.lower().replace(" ", "")
    anagram = anagram.lower().replace(" ", "")

    # get it in dict
    for char in words: dictLchars[char] += 1
    for char_ana in anagram: dictLchars_ana[char_ana] += 1

    # compare
    return True if dictLchars == dictLchars_ana else False

if __name__ == '__main__':
    assert(checkAnagram("Programming", "Gram Ring Mop") == True)
    print("all test passed")
