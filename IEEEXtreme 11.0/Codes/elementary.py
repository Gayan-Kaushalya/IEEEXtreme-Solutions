# Simulate the program on a paper and you will understand the logic behind it.
elements = [ 'h', 'he', 'li', 'be', 'b', 'c', 'n', 'o', 'f', 'ne', 'na', 'mg', 'al', 'si', 'p', 's', 'cl', 'ar', 'k', 'ca', 'sc', 'ti', 'v', 'cr', 'mn', 'fe', 
             'co', 'ni', 'cu', 'zn', 'ga', 'ge', 'as', 'se', 'br', 'kr', 'rb', 'sr', 'y', 'zr', 'nb', 'mo', 'tc', 'ru', 'rh', 'pd', 'ag', 'cd', 'in', 'sn', 'sb', 'te', 
             'i', 'xe', 'cs', 'ba', 'la', 'ce', 'pr', 'nd', 'pm', 'sm', 'eu', 'gd', 'tb', 'dy', 'ho', 'er', 'tm', 'yb', 'lu', 'hf', 'ta', 'w', 're', 'os', 'ir', 'pt', 
             'au', 'hg', 'tl', 'pb', 'bi', 'po', 'at', 'rn', 'fr', 'ra', 'ac', 'th', 'pa', 'u', 'np', 'pu', 'am', 'cm', 'bk', 'cf', 'es', 'fm', 'md', 'no', 'lr', 'rf', 
             'db', 'sg', 'bh', 'hs', 'mt', 'ds', 'rg', 'cn', 'nh', 'fl', 'mc', 'lv', 'ts']

for i in range(int(input())):
        word = input().lower()
        
        if len(word) == 1:
            print(1 if word in elements else 0)
        else:
            if word[0] not in elements and word[0:2] not in elements:
                print(0)
            else:
                dp = [0] * len(word)
                     
                if word[0] in elements:
                    dp[0] = 1
                    
                if word[1] in elements:
                    dp[1] = dp[0]
                if word[0:2] in elements:
                    dp[1] += 1 
                    
                for i in range(2, len(word)):
                    if word[i] in elements:
                        dp[i] += dp[i - 1]
                        
                    if word[i - 1 : i + 1] in elements:
                        dp[i] += dp[i - 2] 
                        
                print(dp[-1])