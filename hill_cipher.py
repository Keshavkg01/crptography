k=list(map(int,input("enter key matrix elements:").split()))
k=[k[:2],k[2:]]
print("\nkey matrix is:")
for i in k:
    print(i)

p = "".join(input("enter plaintext:").split()) + "x"
i = 0
l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
     "x", "y", "z"]

while (i < len(p) - 1):
    if p[i] == p[i + 1]:
        p = p[:i + 1] + "x" + p[1 + i:]
    i += 2
if len(p) % 2 == 1:
    p = p[:-1]
print("plaintext after grouping:", p)
pn=[]
for i in p:
    pn.append(l.index(i))
print(pn)
i=0
c=""
cyphern=[]
cypherc=[]
while i<len(pn):
    p1=[pn[i],pn[i+1]]
    print("plaintext pair: ", p1,[p[i],p[i+1]])
    c1n=[ ( (p1[0] * k[0][0]) + (p1[1] * k[1][0]) )%26,  ( (p1[0] * k[0][1]) + (p1[1] * k[1][1]) )%26]
    cyphern.append(c1n)
    c1c=[ l[c1n[0]],l[c1n[1]] ]
    cypherc.append(c1c)
    print("cypher pair:",c1n,c1c )
    c+=c1c[0]+c1c[1]
    i+=2
print()
print("cypher text after encryption: ",c)

print("\n\n**finding k-inverse**")
ki=[[k[1][1],-k[0][1]],[-k[1][0],k[0][0]]]
print("adjoint of k is:\n"+str(ki[0])+"\n"+str(ki[1]))
dk=k[0][0]*k[1][1]-(k[0][1]*k[1][0])
print("determinant of k is",dk)
print("\n k inverse= 1/"+str(dk)+str(ki[0])+"\n\t\t\t\t"+str(ki[1]))
ki=[[ki[0][0]%26,ki[0][1]%26],[ki[1][0]%26,ki[1][1]%26]]
print("\n-------applying mod 26 to matrix--------")
print("\n k inverse= 1/"+str(dk)+str(ki[0])+"\n\t\t\t\t"+str(ki[1]))
i=0
while(True):
    i+=1
    if (i*dk)%26 == 1:
        break
dk=int(i)
print("\n\t\t\t="+str(dk)+str(ki[0])+"\n\t\t\t\t"+str(ki[1]))
ki=[[ki[0][0]*dk,ki[0][1]*dk],[ki[1][0]*dk,ki[1][1]*dk]]
print("\n\t\t\t="+str(ki[0])+"\n\t\t\t"+str(ki[1]))
print("\n------applying mod 26 to matrix--------")
ki=[[ki[0][0]%26,ki[0][1]%26],[ki[1][0]%26,ki[1][1]%26]]
print("\n\t\t\t="+str(ki[0])+"\n\t\t\t"+str(ki[1]))

print("\n--------decryption---------")
print("cyphertext= ",c)
p=""
for i in range(len(cyphern)):
    print("cypher pair is:",cyphern[i],cypherc[i])
    p1n=[(cyphern[i][0]*ki[0][0])+(cyphern[i][1]*ki[1][0]),(cyphern[i][0]*ki[0][1])+(cyphern[i][1]*ki[1][1])]
    p1n=[p1n[0]%26,p1n[1]%26]
    p1c=[l[p1n[0]],l[p1n[1]]]
    p+=p1c[0]+p1c[1]
    print("plain pair is:",p1n,p1c)
print("\nplaintext after decryption is : ",p)
