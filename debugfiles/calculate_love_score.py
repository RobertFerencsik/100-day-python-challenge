def calculate_love_score(name1, name2):
    """
    Calculates the “love score” between two names 
    by counting how many letters appear in the word "true" in the names
    then does the same for the word "love". The score is then calculated 
    by concatenating the two numbers and converting to int.

    Args:
        name1 (str): The first name to calculate the love score for.
        name2 (str): The second name to calculate the love score for.
    Returns:
        int: The love score between the two names.
    """
def calculate_love_score(name1, name2):
    names = [name1, name2]
    words = ["true", "love"]
    lambda x: names[x].tolower()
    concat_nums = ""
    
    for word in words:
        sum_of_matching_chars = 0
        for name in names:
            sum_of_matching_chars += calculate_matching_chars(name, word)
        concat_nums += str(sum_of_matching_chars)
    #print(sum_of_matching_chars)
    return concat_nums
    
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