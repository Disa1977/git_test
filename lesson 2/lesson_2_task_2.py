sgs0 = input("Год: ")
sgs = int(sgs0)

def is_year_lear():
    for n in sgs: 
        if (n % 4 == 0):
            print(n)    

is_year_lear()
 