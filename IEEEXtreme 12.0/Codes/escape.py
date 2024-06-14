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

for x in range(int(input())):
    length = int(input())
    guess = ["0"] * length
    
    num_correct = query(guess)
    answered = False
    
    for i in range(0, length, 3):
        if num_correct == length:
            answer(guess)
            answered = True
            break
        else:
            if i == 99:
                break
            guess[i] = "1"
            guess[i + 1] = "1"
            guess[i + 2] = "1"
            
            new_num_correct = query(guess)
            
            if new_num_correct == length:
                answer(guess)
                answered = True
                break
            if new_num_correct == (num_correct + 3): # All are ones
                num_correct = new_num_correct
                continue
            elif new_num_correct == (num_correct - 3): # All are zeroes
                guess[i] = "0"
                guess[i + 1] = "0"
                guess[i + 2] = "0"
                continue
            elif new_num_correct == num_correct - 1: # One is a one, two are zeroes
                num_correct = new_num_correct
                guess[i] = "1"
                guess[i + 1] = "0"
                guess[i + 2] = "0"
                new_num_correct = query(guess)
                
                if new_num_correct == num_correct + 2: # It was 100
                    num_correct = new_num_correct
                    continue
                
                # It wasn't 100
                num_correct = new_num_correct
                guess[i] = "0"
                guess[i + 1] = "1"
                guess[i + 2] = "0"
                new_num_correct = query(guess)
                
                if new_num_correct == num_correct + 2: # It was 010
                    num_correct = new_num_correct
                    continue
                
                guess[i] = "0"
                guess[i + 1] = "0"
                guess[i + 2] = "1"
                num_correct = new_num_correct + 2
                continue
        
            elif new_num_correct == num_correct + 1: # Two are ones, one is a zero.
                num_correct = new_num_correct
                guess[i] = "1"
                guess[i + 1] = "1"
                guess[i + 2] = "0"
                new_num_correct = query(guess)
                if new_num_correct == num_correct + 1: # It was 110
                    num_correct = new_num_correct
                    continue
                
                # It must be either 101 or 011
                num_correct = new_num_correct
                guess[i] = "1"
                guess[i + 1] = "0"
                guess[i + 2] = "1"
                new_num_correct = query(guess)
                if new_num_correct == num_correct + 2: # It was 101
                    num_correct = new_num_correct
                    continue
                
                # It must be 011
                guess[i] = "0"
                guess[i + 1] = "1"
                guess[i + 2] = "1"
                num_correct = new_num_correct + 2
                continue
    
    # This part is bit hard to understand.
    if answered == False:
        if length == 6:
            answer(guess)
        else:
            guess[99] = "1"
            num_correct = query(guess)
            if num_correct == length:
                answer(guess)