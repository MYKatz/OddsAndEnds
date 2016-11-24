print("".join(sorted(input().lower())).strip("!@#$%^&*().>,</?;:'|{}[]-_+= " + '"') == "".join(sorted(input().lower())).strip("!@#$%^&*().>,</?;:'| " + '"'))

# This checks if words or phrases are anagrams of each other.  
#Try "anagram" and "nagaram" or "A decimal point." and "I'm a dot in place"
