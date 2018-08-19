####################################################################
######################## E X E R C I S E 1 #########################
####################################################################

def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """    
    return (len(zip_code) == 5) and (zip_code.isdigit() == True)

q1.check()

####################################################################
######################## E X E R C I S E 2 #########################
####################################################################
def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """    
    indexs = []
    for doc in range(len(doc_list)):
        for word in doc_list[doc].upper().split():
            if (word.strip(',').strip('.') == keyword.upper()):
                indexs.append(doc)
    return indexs
                
    #return [index for index, value in doc_list if doc_list[index].upper().find(keyword) != -1]


q2.check()


####################################################################
######################## E X E R C I S E 3 #########################
####################################################################

def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    dic = {}
    for word in keywords:
        dic[word] = word_search(doc_list, word)
    return dic

q3.check()