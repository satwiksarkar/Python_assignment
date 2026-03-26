import re

# basic number words
ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
         "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

# function to convert numbers < 100
def two_digit(n):
    if n < 10:
        return ones[n]
    elif 10 <= n < 20:
        return teens[n - 10]
    else:
        return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")

# function to convert up to 4-digit numbers
def number_to_words(n):
    if n < 100:
        return two_digit(n)
    
    elif n < 1000:
        return ones[n // 100] + " hundred" + \
               (" and " + two_digit(n % 100) if n % 100 != 0 else "")
    
    elif n < 10000:
        first = n // 100
        second = n % 100
        d4= n // 1000
        d3 = (n % 1000) // 100
        words=""
        print(first, second)
        if(d3!=0):
            words = two_digit(first) + " hundred"
        else: 
            words= two_digit(d4) +" thousand "   
        if second != 0:
            words += " and " + two_digit(second)
        return words

    else:
        return str(n)  # for larger numbers (not handled)

filename = input("Enter file name: ")

with open(filename, "r") as file:
    text = file.read()

numbers = re.findall(r'\d+', text)

print("Converted Numbers:")

for num in numbers:
    n = int(num)
    print(num, "→", number_to_words(n))
