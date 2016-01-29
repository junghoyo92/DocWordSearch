#############################
## CSE231 - Section 2
#############################

import string


## This function takes a document in a text file and returns a dictionary
## with its keys as words and values as a set of the document numbers
## the word is in.
## The user can thus utilize this function to search words in a document and find a document with a specific word.

def word_search():
    file_obj = open('ap_docs.txt')
    token = '<NEW DOCUMENT>'
    new_dict = {}
    doc_number = 0 
    for line in file_obj:
        line = line.strip()
        if line == token:
            doc_number += 1
            del line
        else:
            word_list = line.split()
            for word in word_list:
                word = word.lower()
                word = word.strip()
                word = word.strip(string.punctuation)
                if word in new_dict:
                    new_dict[word].add(doc_number)
                elif word not in new_dict:
                    new_dict[word] = {doc_number}
    return new_dict

## This function takes an empty list as a parameter.
## The function reads through a document and creates
## a list of strings with a article in each string.
## The new strings are spotted and created with a
## token.

def article_str(new_list):
    file_obj = open('ap_docs.txt')
    token = '<NEW DOCUMENT>\n'
    new_str = ''
    doc_number = 0
    for line in file_obj:
        if line == token:
            doc_number += 1
            new_list.append(new_str)
            new_str = ''
        elif line not in token:
            new_str += line
        elif line == '\n':
            new_str += '\n'
    new_list.append(new_str)
    return new_list

## This function takes the dictionary from the word_search
## function and a user inputted list of search words as
## parameters.
## It appends the documents numbers the search word exists in
## to a list.
## It intesects each item in the list and returns the
## intersection.

def intersection(search_dict, search_word):
    my_list = []
    sw = search_word.split(' ')
    for word in sw:
        my_list.append(search_dict[word])
    inter = my_list[0]
    for item in my_list:
        inter = item & inter
    return inter

## This function uses the word_search function to create a dictionary of all the
## words with its document number. It contains a boolean function that takes
## an input. If the input is 1, then it finds the intersection and returns the
## document numbers the search words exist in. If the input is 2, then it prompts for the
## document number and returns the document. If the input is 3, then the program
## shuts down.

def main():
    new_list = []
    search_dict = word_search()
    while True:
        q = input("What would you like to do?\n1. Search for Documents\n2. Read Document\n3. Quit Program\n")
        if q=="1":   
            search_word = input('Enter search word: ')
            search_word = search_word.lower()
            search_word = search_word.strip(string.punctuation)
            inter = intersection(search_dict,search_word)
            print('Documents fitting search: ', inter)
            print('----------------------------')
        elif q=="2":  
            doc_num = int(input('Enter document number: '))
            print('----------------------------')
            new_list = article_str(new_list)
            print(new_list[doc_num])
            print('----------------------------')
        elif q=="3":  
            print ('Quiting')
            break

main()
