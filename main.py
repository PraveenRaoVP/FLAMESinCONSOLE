name1 = str(input("Enter the name of the first person: "))
name2 = str(input("Enter the name of the second person: "))

uniq_letters = []
for i in [*name1]:
    if(i not in [*name2]):
        uniq_letters.append(i)
for j in [*name2]:
    if(j not in [*name1]):
        uniq_letters.append(j)
print(uniq_letters)


flames = ['F','L','A','M','E','S']

count = len(uniq_letters)

element = 0

while(True):
    if(len(flames)==1):
        break
    if(count>=len(flames)):
        count=count-len(flames)
    flames.pop(count)

desc = {"F": "Friends", "L": "Lovers", "A": "Affection", "M": "Married", "E": "Enemies", "S": "Siblings"}
print(f"{name1} and {name2} will be {desc[flames[0]]}")


