def countVowels(str1):
    str1 = str1.lower()
    split1 = list(str1)
    vowels = []

    for i in range(len(split1)):
        if(split1[i]== 'a' or split1[i]== 'e' or split1[i]== 'i' or split1[i]== 'o' or split1[i]== 'u'):
            vowels.append(split1[i])

    #print(vowels)
    if len(vowels)==0:
        return("No vowels found.")
        
    if len(vowels)>0:
        freq = dict((x,vowels.count(x)) for x in set(vowels))
        return freq


#  Driver Code Starts

if __name__ == '__main__': 
    str1=input() 
    print(countVowels(str1))

# } Driver Code Ends

