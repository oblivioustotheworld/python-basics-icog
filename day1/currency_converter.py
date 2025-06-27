def converter(opt,amount):
    result=0
    if opt==1:
        result=amount*0.0072
        print('$'+str(result))
    else:
        result=amount*135.25
        print(str(result)+'birr')
    





option=int(input("1.etb to usd  \n2.usd to etb  "))
amount=int(input("Enter amount  "))

converter(option,amount)


