#PLAY-FAIR CYPHER TO ENCRYPT A PLAINTEXT TO CYPHERTEXT
k = input("enter key to encode: ")
i = 0
flag = 0
m = []
matrix = []
l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
     "x", "y", "z"]
for i in k:
    if i not in m:
        m.append(i)
for i in l:
    if i not in m:
        m.append(i)
m[13] += m[14]
m.remove(m[14])
count = 0
matrix.append(m[:5])
matrix.append(m[5:10])
matrix.append(m[10:15])
matrix.append(m[15:20])
matrix.append(m[20:])
print("the matrix of playfair is:")
for i in matrix:
    print(i)
spam = 1
while (spam == 1):
    cypher = []
    # spam=int(input("enter 1 to continue in playfair\n\tenter 0 to quit:"))
    p = "".join(input("enter plaintext:").split()) + "x"
    i = 0
    while (i < len(p) - 1):
        if p[i] == p[i + 1]:
            flag = 1
            p = p[:i + 1] + "x" + p[1 + i:]
        i += 2
    if len(p) % 2 == 1:
        p = p[:-1]
    if flag == 1:
        print("plaintext after grouping:", p)

    for i in range(0, len(p), 2):
        print("plaintext pair:", p[i], p[i + 1])
        for j in range(5):
            if p[i] in matrix[j]:
                r1 = j
                c1 = matrix[j].index(p[i])
            elif p[i] in matrix[2][3]:
                r1 = 2
                c1 = 3
            if p[i + 1] in matrix[j]:
                r2 = j
                c2 = matrix[j].index(p[i + 1])
            elif p[i + 1] in matrix[2][3]:
                r2 = 2
                c2 = 3
            # print(r1,c1,r2,c2)
        if r1 == r2:
            cypher.append(matrix[r1][(c1 + 1) % 5])
            cypher.append(matrix[r1][(c2 + 1) % 5])
        elif c1 == c2:
            cypher.append(matrix[(r1 + 1) % 5][c1])
            cypher.append(matrix[(r2 + 1) % 5][c1])
        else:
            cypher.append(matrix[r1][c2])
            cypher.append(matrix[r2][c1])
        print("cypher pair:", cypher[-2], cypher[-1])
    print("cypher text is: ")
    for i in cypher:
        if len(i) == 2:
            print(i[0] + "/" + i[1], end=" ")
            continue
        print(i, end=" ")
    print()
    print()
    spam = int(input("enter 1 to continue in playfair\n\tenter 0 to quit:"))
