'''Q3'''
def EndOfSentence(sentence):
    terminals = 0
    n = len(sentence)
    for i in range(n-2):
        string = sentence[i]
        next_string = sentence[i+1]
        further_string = sentence[i+2]

        if string in ".?!" and next_string.isspace() and further_string.isupper():
            terminals+=1
    return terminals

# print(EndOfSentence("The sun will rise again. Formula 1 starts tomorrow! I think McLaren will win it again this year"))

'''Q4'''
spaces_count, hyphen_count  = 0, 0 
with open('words.txt', "r") as file:
    for line in file:
        for str in line:
            if str in "-":
                hyphen_count+=1
            if str.isspace():
                spaces_count+=1
print(spaces_count, hyphen_count)


