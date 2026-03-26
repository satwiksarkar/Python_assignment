from collections import Counter

class MyString:
    
    def __init__(self, text):
        self.text = text

    # operator overloading for len()
    def __len__(self):
        words = self.text.split()
        freq = Counter(words)

        repeated_length = 0

        for word, count in freq.items():
            if count > 1:
                repeated_length += len(word) * count

        if repeated_length > 0:
            return repeated_length
        else:
            return len(self.text)

    # function to find most frequent word
    def most_frequent_word(self):
        words = self.text.split()
        freq = Counter(words)
        return freq.most_common(1)

s=input("Enter the string: ")
my_str=MyString(s)
print(len(my_str))
   
