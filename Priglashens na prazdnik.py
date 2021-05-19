family=[]
odin=[]
surnames= ["Petya Smith","Alexandr Ford", " Sasha Taylor", "Vlad Miller", "Katya Taylor", "Masha Miller", "Dasha Smith"]
while len(surnames)!=0:
    x=surnames.pop(0)
    a=x.split()
    for y in surnames:
        b=y.split()
        if a[1]==b[1]:
            surnames.remove(y)
            a=a.pop(0)
            print(a+" and "+y+"s will come to the festival")
            break
    else:
        print(x+", is coming")
