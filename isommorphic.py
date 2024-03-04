s = input("Enter the first string required: ")
t = input("Enter the second string required: ")

if len(s) != len(t):
    print("The given strings are not isomorphic.")
else:
    mapping_s_t = {}
    mapping_t_s = {}
    
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]
        if char_s in mapping_s_t:
            if mapping_s_t[char_s] != char_t:
                print("The given strings are not isomorphic.")
                break
        else:
            mapping_s_t[char_s] = char_t
        
        if char_t in mapping_t_s:
            if mapping_t_s[char_t] != char_s:
                print("The given strings are not isomorphic.")
                break
        else:
            mapping_t_s[char_t] = char_s
    else:
        print("The given strings are isomorphic.")
