token_dict = {}
current_id = 1   # start from 1 (0 reserved for padding)

lines_tokens = []

with open('test.txt', "r") as file:
    for line in file:
        words = line.strip().split()
        lines_tokens.append(words)
        
        for word in words:
            if word not in token_dict:
                token_dict[word] = current_id
                current_id += 1
max_len = max(len(tokens) for tokens in lines_tokens)            
for i in range(len(lines_tokens)):
   # print(i)
    for j in range(max_len-len(lines_tokens[i])):
        lines_tokens[i].append("<PAD>")
print(lines_tokens)
