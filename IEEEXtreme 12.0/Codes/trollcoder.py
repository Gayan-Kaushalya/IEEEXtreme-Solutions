import sys

def send(prefix, guess):
    query = prefix + " ".join(guess)
    print(query)
    sys.stdout.flush()
    
def answer(guess):
    send("A ", guess)
    
def query(guess):
    send("Q ", guess)
    return int(input())

length = int(input())
guess = ["0"] * length

num_correct = query(guess)

for i in range(length):
    if num_correct == length:
        answer(guess)
        break
    else:
        guess[i] = "1"
        
        if i == length - 1:
            answer(guess)
            break
        else:
            new_num_correct = query(guess)
            
            if new_num_correct > num_correct:
                num_correct = new_num_correct
            else:
                guess[i] = "0"