class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        word_map = set('aeiouAEIOU')
        res = ""
        list_word = sentence.split()
        for i, word in enumerate(list_word):
            if word[0] in word_map:
                word += "ma"
                res += word
            else:
                word = word[1:] + word[0]
                word += "ma"
                res += word
            res += "a" * (i+1)
            res += " "
        return res[:-1]
                