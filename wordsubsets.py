from collections import Counter

def word_subsets(words1, words2):
    
    universal_words = []

    def subset(string1, string2):
        string2 = Counter(string2)
        for ch in string2:
            if ch not in string1 or string1[ch] < string2[ch]:
                return False
        return True

    def universal(string, words):
        for word in words:
            if subset(string, word) == False:
                return False
        return True

    for word in words1:
        counter_form = Counter(word)
        if universal(counter_form, words2):
            universal_words.append(word)
    print(universal_words)
    return universal_words

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]
word_subsets(words1, words2)

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["l","e"]
word_subsets(words1, words2)
        
        
        
        

