read = open("changed-2019-08-01-2226.txt", 'r', encoding='utf-8-sig', errors="ignore").read().splitlines()
word = input("Word: ")
count = 0
for word in read:
    count +=1 # we're increasing words here
    
print(count)
