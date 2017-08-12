_author_  = "Mikus"

address = int(input(" Please put your address:"))
print("Your address is :{}".format(address))
if address >= 0:
    print("You are living on the north side")

    if address <=0:
        print("You are living on the south side")

     if address >=7200:
         print("You are suburban")
         if address <=-9900:
             print("You are a gangsta")