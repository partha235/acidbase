import random as r
i=["acid","base"]
j=r.choice(i)
che=input("enter an formula of {}".format(j))
if j=="acid":
    if che[0]=="H":
        print("correct")
    else:
        print("Wrong")
if j=="base":
    if "OH" in che:
        print("correct")
    else:
        print("Wrong")