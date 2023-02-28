def calculate(op):
    print("\nCalcy : What is the First Operand ?\n")
    op1=str(input("Me    : "))
    z1=op1.replace(" ", "")
    if(z1.isalpha() and z1!="stop"):
        op1=convert_to_number(op1)
    print("\nCalcy : What is the Second Operand ?\n")
    op2=str(input("Me    : "))
    z2=op2.replace(" ","")
    if(z2.isalpha() and z2!="stop"):
        op2=convert_to_number(op2)
    if(op=="addition" and (z1!="stop" and z2!="stop")):
        res=float(op1)+float(op2)
        print("\nCalcy : Therefore, Addition of "+str(op1)+" and "+str(op2)+" is : "+str(res)+" .")
    elif(op=="subraction" and (z1!="stop" and z2!="stop")):
        res=float(op1)-float(op2)
        print("\nCalcy : Therefore, Difference of "+str(op1)+" and "+str(op2)+" is : "+str(res)+" .")
    elif(op=="multiplication" and (z1!="stop" and z2!="stop")):
        res=float(op1)*float(op2)
        print("\nCalcy : Therefore, Product of "+str(op1)+" and "+str(op2)+" is : "+str(res)+" .")
    elif(op=="division" and (z1!="stop" and z2!="stop")):
        if(float(op2)==0):
            print("\nCalcy : You have entered wrong operands , A number cant be divided by 0. Plz Re-enter it ...")
            calculate(op)
        else:
            res=float(op1)/float(op2)
            print("\nCalcy : Therefore, Division of "+str(op1)+" by "+str(op2)+" is : "+str(res)+" .")

def convert_to_number(input_str):
    if input_str.isnumeric():
        return int(input_str)
    else:
        word_to_num = {
            "zero": 0,
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "ten": 10,
            "eleven": 11,
            "twelve": 12,
            "thirteen": 13,
            "fourteen": 14,
            "fifteen": 15,
            "sixteen": 16,
            "seventeen": 17,
            "eighteen": 18,
            "nineteen": 19,
            "twenty": 20,
            "thirty": 30,
            "forty": 40,
            "fifty": 50,
            "sixty": 60,
            "seventy": 70,
            "eighty": 80,
            "ninety": 90
        }
        current_num = 0
        total_num = 0
        words = input_str.lower().split()
        n=1
        if(words[0]=="minus"):
            n=-1
        for word in words:
            if word in word_to_num:
                current_num += word_to_num[word]
            elif word == "hundred":
                current_num *= 100
            elif word == "thousand":
                total_num += current_num * 1000
                current_num = 0
            elif word == "million":
                total_num += current_num * 1000000
                current_num = 0
        total_num += current_num
        return total_num*n


user_input=str(input("Me    : "))
if("stop" in user_input.lower()) or ("quit" in user_input.lower()):
    print("\nCalcy : Thank you for engaging with me. See you soon ......")
else:
    print("\nCalcy : Good day! I'm a chatbot designed to perform mathematical calculations. ")
    while(True): 
        print("\nCalcy : How may I assist you with your calculations?\n\n\tI possess the ability to perform operations such as :\n\t\t 1. Addition (+)\n\t\t 2. Subraction (-)\n\t\t 3. Multiplication (×)\n\t\t 4. Division (÷)\n\n\tWhat operation do you want me do ?\n")    
        user_input=str(input("Me    : "))   
        if("add" in user_input.lower() or "sum" in user_input.lower() or "plus" in user_input.lower()):
            op="addition"
            calculate(op)
        elif("sub" in user_input.lower() or "minus" in user_input.lower() or "reduce" in user_input.lower() or "difference" in user_input.lower()):
            op="subraction"
            calculate(op)  
        elif("multi" in user_input.lower() or "product" in user_input.lower() or "times" in user_input.lower() or "into" in user_input.lower()):
            op="multiplication"
            calculate(op)
        elif("divi" in user_input.lower() or "quot" in user_input.lower() or "by" in user_input.lower()):
            op="division"
            calculate(op)
        elif("stop" in user_input.lower() or "quit" in user_input.lower() or  "exit" in user_input.lower()):
            print("\nCalcy : Thank you for engaging with me. See you soon ......")
            break
        else:
            print("\nCalcy : Regretfully, we cannot provide the requested operation or you have entered a wrong comment. Plz try with operation mentioned above.")
        print("\n\n\tDo you require me to perform any other calculations ?\n")
        user_input=str(input("Me    : "))
        if("stop" in user_input.lower()) or ("exit" in user_input.lower()) or ("quit" in user_input.lower())or ("no" in user_input.lower()):
            print("\nCalcy : Thank you for engaging with me. See you soon ......")
            break

        