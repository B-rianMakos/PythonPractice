


def is_valid_file_name():
    '''()->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name

def clean_word(word):
    '''(str)->str
    Returns a new string which is lowercase version of the given word
    with special characters and digits removed

    The returned word should not have any of the following characters:
    ! . ? : , ' " - _ \ ( ) [ ] { } % 0 1 2 3 4 5 6 7 8 9 tab character and new-line character

    >>> clean_word("co-operate.")
    'cooperate'
    >>> clean_word("Anti-viral drug remdesivir has little to no effect on Covid patients' chances of survival, a study from the World Health Organization (WHO) has found.")
    'antiviral drug remdesivir has little to no effect on covid patients chances of survival a study from the world health organization who has found'
    >>> clean_word("1982")
    ''
    >>> clean_word("born_y1982_m08\n")
    'bornym'

    '''
    y = ""
    for x in word:
        if x in "!.?:,'" or x in '"-_\()[]{}%0123456789' :
            y = y
        else:
            y = y + x

    return(y.lower())
    
def test_letters(w1, w2):
    '''(str,str)->bool
    Given two strings w1 and w2 representing two words,
    the function returns True if w1 and w2 have exactlly the same letters,
    and False otherwise

    >>> test_letters("listen", "enlist")
    True
    >>> test_letters("eekn", "knee")
    True
    >>> test_letters("teen", "need")
    False
    '''

    w1 = sorted(w1)
    w2 = sorted(w2)

    if w1 == w2 :
        return True
    elif w1 != w2 :
        return False

    pass
    
def create_clean_sorted_nodupicates_list(s):
    '''(str)->list of str
    Given a string s representing a text, the function returns the list of words with the following properties:
    - each word in the list is cleaned-up (no special characters nor numbers)
    - there are no duplicated words in the list, and
    - the list is sorted lexicographicaly (you can use python's .sort() list method or sorted() function.)

    This function must call clean_word function.

    You may find it helpful to first call s.split() to get a list version of s split on white space.
    
    >>> create_clean_sorted_nodupicates_list('able "acre bale beyond" binary boat brainy care cat cater crate lawn\nlist race react cat sheet silt slit trace boat cat crate.\n')
    ['able', 'acre', 'bale', 'beyond', 'binary', 'boat', 'brainy', 'care', 'cat', 'cater', 'crate', 'lawn', 'list', 'race', 'react', 'sheet', 'silt', 'slit', 'trace']

    >>> create_clean_sorted_nodupicates_list('Across Europe, infection rates are rising, with Russia reporting a record 14,321 daily cases on Wednesday and a further 239 deaths.')
    ['', 'a', 'across', 'and', 'are', 'cases', 'daily', 'deaths', 'europe', 'further', 'infection', 'on', 'rates', 'record', 'reporting', 'rising', 'russia', 'wednesday', 'with']
    '''
    y = clean_word(s)
    u = y.split()
    
    string = []
    for x in u:
        if x not in string:
            string.append(x)
        else:
            string = string
    
    
    
    return(sorted(string))
    

def word_anagrams(word, wordbook):
    '''(str, list of str) -> list of str
    - a string (representing a word)
    - wordbook is a list of words (with no words duplicated)

    This function should call test_letters function.

    The function returs a (lexicographicaly sorted) list of anagrams of the given word in wordbook
    >>> word_anagrams("listen", wordbook)
    ['enlist', 'silent', 'tinsel']
    >>> word_anagrams("race", wordbook)
    ['acre', 'care']
    >>> word_anagrams("care", wordbook)
    ['acre', 'race']
    >>> word_anagrams("year", wordbook)
    []
    >>> word_anagrams("ear", wordbook)
    ['are', 'era']
    '''
       
def word_anagrams(word, wordbook):
       
    anagram = []

    for x in range(len(wordbook)):
        if test_letters(word,wordbook[x]) == True:
            anagram.append(wordbook[x])
        else:
           anagram = anagram
    if word in anagram:
        anagram.remove(word)
    
    return sorted(anagram)

    
        

def count_anagrams(l, wordbook):
    '''(list of str, list of str) -> list of int

    - l is a list of words (with no words duplicated)
    - wordbook is another list of words (with no words duplicated)

    The function returns a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.
    
    Whenever a word in l is the same as a word in wordbook, that is not counted.

    >>> count_anagrams(["listen","care", "item", "year", "race", "ear"], wordbook)
    [3, 2, 3, 0, 2, 2]

    The above means that "listen" has 3 anagrams in wordbook, that "care" has 2 anagrams in wordbook ...
    Note that wordbook has "care", "race" and "acre" which are all anagrams of each other.
    When we count anagrams of "care" we count "race" and "acre" but not "care" itself.
    '''


    
    
    #YOUR CODE GOES HERE
    newl = []
    

    for word in l:
        y = word_anagrams(word, wordbook)
        count=len(y)
        newl.append(count)
    return newl
    

    #for x in y
        #count += 1
        
        



def k_anagram(l, anagcount, k):
    '''(list of str, list of int, int) -> list of str

    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a  (lexicographicaly sorted) list of all the words
    in l that have exactlly k anagrams (in wordbook as recorded in anagcount)

    k_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2], 2)
    ['care', 'ear', 'race']
    '''
    
    #YOUR CODE GOES HERE
    z = []
    for x in range(len(l)) :
        if anagcount[x] == k :
            z.append(l[x])
    return sorted(z)

def max_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a (lexicographicaly sorted) list of all the words
    in l with maximum number of anagrams (in wordbook as recorded in anagcount)
    
    >>> max_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2])
    ['item', 'listen']
    '''

    z = []
    maximum = 0
    for x in range(len(l)):
        if anagcount[x] > maximum :
            maximum = anagcount[x] 
            
        elif anagcount[x] < maximum :
            maximum = maximum

    for x in range(len(l)):
        if anagcount[x] == maximum:
            z.append(l[x])
    return sorted(z)

    
            
                   
    
    

def zero_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a (lexicographicaly sorted) list of all the words
    in l with no anagrams
    (in wordbook as recorded in anagcount)
    
    >>> zero_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2])
    ['year']
    '''
    z = []
    zero = 0

    for x in range(len(l)):
        if anagcount[x] == zero:
            z.append(l[x])
    return sorted(z)

    
            



                
    
##############################
# main
##############################
wordbook=open("english_wordbook.txt").read().lower().split()
list(set(wordbook)).sort()


print("Would you like to:")
print("1. Analize anagrams in a text -- given in a file")
print("2. Get small help for Scrabble game")
print("Enter any character other than 1 or 2 to exit: ")
choice=input()

if choice=='1':
    file_name=get_file_name()
    rawtx = open(file_name).read()
    l=create_clean_sorted_nodupicates_list(rawtx)
    anagcount = count_anagrams(l,wordbook)

    print("\nOf all the words in your file, the following words have the most anagrams:")
    print(max_anagram(l, anagcount))
    print("")
    print("Here are their anagrams:")
    Max = max_anagram(l, anagcount)
    for word in Max:
        print(f"The anagrams of {word} are the following: {word_anagrams(word, wordbook)}")
    print("")
    print("Here are the words from your file that have no anagrams:")
    print(zero_anagram(l, anagcount))
    print("")
    print("If you are interested in knowing the words in your file that have a specific ammount of anagrams, k")
    k = int(input("Please enter a positive integer for k:"))
    print(f"Here are the words in your file with exactly {k} anagrams: \n{k_anagram(l, anagcount, k)}")
    
    
    # when asking for k from the user you may assume that they will enter non-negative integer
    
    
elif choice=='2':

    #YOUR CODE GOES HERE
    word = input("Enter the letters you have one after another with no spaces ")

    while " " in word:
            print("Error, you entered space(s)")
            word = input("Enter the letters you have one after another with no spaces ")
    print("Would you like help forming a word with:")
    print("1. All of these letters")
    print("2. All but one of these letters?")
    

    newchoice = input()
    
    while newchoice != "1" and newchoice != "2":
          print("You must input 1 or 2 ")
          newchoice = input("Please input 1 or 2 ")

    newchoice = int(newchoice)



          
    if newchoice == 1:
        anas = word_anagrams(word, wordbook)
        if  anas == []:
            print("There is no word comprised of exactly these letters")
            
        else:
            if word in wordbook:
                anas.append(word)
            print(f"Here are the words that are comprised of these letters: {sorted(anas)}")

    elif newchoice == 2 :
        print(f"The letters you gave us were: {word}")
        print("Let's see what anagrams we can get if we ommit one of these letters.")
        letters = ""
        for x in range(len(word)):
            part1 = word[:x]
            part2 = word[x+1:]
            letters = part1 + part2
            print("")
            print(f"without the letter in position {x+1} we have the letters: {letters}")
            newword = word_anagrams(letters, wordbook)
            if letters in wordbook:
                newword.append(letters)
            if newword == []:
                print("")
                print(f"There are no possible words with these letters: {letters}")
            else:
                print("")
                print("With these letters we get the words:")
                print(sorted(newword))
            
else:
    print("Good bye")
   
