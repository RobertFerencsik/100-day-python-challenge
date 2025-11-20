def calculate_love_score(name1, name2):
    names = [name1, name2]
    words = ["true", "love"]
    lambda x: names[x].tolower()
    
    sum_of_matching_chars = 0
    for name in names:
        for word in words:
            sum_of_matching_chars += calculate_matching_chars(name, word)
    print(sum_of_matching_chars)
    
def calculate_matching_chars(name, word):
    sum = 0
    for char in name:
        if char in word:
           sum += 1 
    return sum
    
calculate_love_score("Kanye West", "Kim Kardashian")