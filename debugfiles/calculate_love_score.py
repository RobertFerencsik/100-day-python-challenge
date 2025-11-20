def calculate_love_score(name1, name2):
    """
    Calculates the “love score” between two names 
    by counting how many letters from the words “true” and “love” appear in those names.

    Args:
        name1 (str): The first name to calculate the love score for.
        name2 (str): The second name to calculate the love score for.
    Returns:
        int: The love score between the two names.
    """
    names = [name1, name2]
    words = ["true", "love"]
    lambda x: names[x].tolower()
    
    sum_of_matching_chars = 0
    for name in names:
        for word in words:
            sum_of_matching_chars += calculate_matching_chars(name, word)
    #print(sum_of_matching_chars)
    return sum_of_matching_chars
    
def calculate_matching_chars(name, word):
    """
    Calculates the number of matching characters between a name and a word.

    Args:
        name (str): The name to calculate the matching characters for.
        word (str): The word to calculate the matching characters for.
    Returns:
        int: The number of matching characters between the name and the word.
    """
    sum = 0
    for char in name:
        if char in word:
           sum += 1 
    return sum
    
print(calculate_love_score("Kanye West", "Kim Kardashian"))