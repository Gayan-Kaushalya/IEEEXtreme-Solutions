def find_suffix(string, p, char_helper):
    suffix_counter = 0
    string_idx = len(string) - 1
    for char in p[::-1]:
        char_id = ord(char) - ord('a')
        if string_idx < 0:
            return suffix_counter
        if char_helper[char_id][string_idx] == -1:
            return suffix_counter
        string_idx = char_helper[char_id][string_idx] - 1
        suffix_counter += 1
    return suffix_counter   
    
string = input()

previous_characters = [[-1]*len(string) for _ in range(26)]
for idx, char in enumerate(string):
    for char_id in range(26):
        previous_characters[char_id][idx] = previous_characters[char_id][idx - 1]
    char_id = ord(char) - ord('a')
    previous_characters[char_id][idx] = idx

for i in range(int(input())):
    p = input()
    print(find_suffix(string, p, previous_characters))