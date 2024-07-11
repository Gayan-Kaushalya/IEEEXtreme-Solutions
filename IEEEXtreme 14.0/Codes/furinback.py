# I got the solution from IEEE DataPort
for _ in range(int(input())):
    s = input()
    
    a = ord(s[2])
    b = ord(s[1])
    c = ord(s[0])
    
    a = (256 + a - b) % 256
    b = (256 + b - c) % 256
    d = 256 ** 3 + a * 256 ** 2 + b * 256 + c - (255 * 256 ** 2 + 255 * 256 + 255)
    
    # The below part computes the value which is one more than the smallest prime factor of d.
    flag = True
    
    for i in range(2, d // 2 + 1):
        if d % i == 0:
            print(i + 1)
            flag = False
            break
        
    if flag:
        print(d + 1)