file = open('ex7.txt','r')
content = file.readlines()
file.close()
for i in range(len(content)):
    content[i] = content[i].strip()

line1 = content[0].split()
n = int(line1[0])
c1 = int(line1[1])
c2 = int(line1[2])
#print(n,c1,c2)

A = [int(i) for i in content[1:]]
A.sort()
#print(A)

ansc1 = []
for i in A:
    for j in A:
        if i+j == c1:
            ansc1.append((i,j))
#print(ansc1) #(x1,x2)

ansc2 = []
for i in A:
    for j in A:
        if i-j == c2:
            ansc2.append((i,j))
#print(ansc2) #(x8,x6)

ansx1 = []
for i in ansc1:
    for j in A:
        for k in A:
            if i[0] == j-k:
                ansx1.append((i[0],i[1],k,j))
#print(ansx1) #(x1,x2,x3,x4)

ansx6 = []
for i in ansc2:
    for j in A:
        for k in A:
            if i[1] == j-k:
                ansx6.append((k,i[1],j,i[0]))
#print(ansx6) #(x5,x6,x7,x8)

pos_ans = []
for i in ansx1:
    temp = list(i)
    for j in ansx6:
        temp2 = temp+list(j)
        stemp2 = set(temp2)
        if len(temp2) == len(stemp2):
            pos_ans.append(tuple(temp2))

for i in pos_ans[0]:
    print(i)