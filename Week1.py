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

print(EndOfSentence("The sun will rise again. Formula 1 starts tomorrow! I think McLaren will win it again this year"))


