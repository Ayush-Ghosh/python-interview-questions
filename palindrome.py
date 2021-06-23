palindrome = True
j = -1

word = input("enter the word: ")
for i in range(0,len(word)):
    if word[i] ==  word[j]:
        j = j - 1
    else:
        palindrome = False

print(palindrome)