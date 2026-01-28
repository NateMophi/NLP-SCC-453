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

import re
def SentiAnalysis(text):
    score = 3
    text = text.lower().strip()
    
    # Word Bank
    pos_words = {'great', 'easy', 'helpful', 'fast', 'good', 'pretty', 'nice', 'happy', 'love', 'amazing'}
    neg_words = {'terrible', 'broken', 'fail', 'slow', 'expensive', 'bad', 'poor', 'hate', 'disaster', 'waste'}
    negators = {'not', 'wasnt', 'shouldnt', 'didnt', 'never', 'wont', 'cant'}

    words =  re.findall(r"\b\w+\b", text)
    has_exclamation = "!" in text

    # Keyword Detection + Negation Checking
    for i, word in enumerate(words):
        if word in pos_words:
            if i>0 and words[i-1] in negators:
                score-=1
            else:
                score+=1

        if word in neg_words:
            if i>0 and words[i-1] in negators:
                score+=1
            else:
                score-=1

    if has_exclamation:
        if score < 3:
            score+=1
        elif score > 3:
            score +=1

    return max(1, min(5, score))

test_sentences = [
    "The service was okay and the food arrived on time.",
    "I absolutely love GitHub, it is the best!",
    "She is very pretty!",
    "The MoYu WrM is a great 3x3 Cube"
]

print(f"{'Sentence':<50} | {'Score'}")
print("-" * 60)
for s in test_sentences:
    print(f"{s:<50} | {SentiAnalysis(s)}")