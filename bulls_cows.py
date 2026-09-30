secret = "1234"
word_given = input("give me a 4 digit number ")
A1 = (0,secret[0])
A2= (1,secret[1])
A3= (2,secret[2])
A4= (3,secret[3])

B1= (0,word_given[0])
B2= (1,word_given[1])
B3= (2,word_given[2])
B4= (3,word_given[3])

list_B= [B1,B2, B3,B4]
list_A = [A1,A2,A3,A4]
bulls=0
cows=0
i=0
while i <= 3:
    if list_A[i]== list_B[i]:
        bulls += 1
    i +=1
for j in word_given:
    if j in secret:
        cows += 1
print(cows)
print(bulls)
