me = "Tornike Karelidze"
xmovnebi = 0

for i in range(0,len(me)):
    char = (me[i])
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        xmovnebi += 1
print(xmovnebi)