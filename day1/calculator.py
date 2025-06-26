def calculator(op1,op2,oper):
    result=0
    match oper:
     case '/':
      if op2==0:
        print('undefined')
      result=op1/op2
     case '-':
       result=op1-op2
     case '+':
        result=op1+op2
     case '*':  
        result=op1*op2
     case _ :
        print("invalid operator")
    
    return result

operand1=float(input("enter operand 1:    "))
operand2=float(input("enter operand 2:    "))
operator=input("enter operator:  ")

print("Result" ,calculator(operand1,operand2,operator))