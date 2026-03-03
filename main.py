try:
    num1,num2=eval(input("enter two numbers,seperated by a comma:"))
    result=num1/num2
    print("result is",result)
except ZeroDivisionError:
    print("Division by zero is error!")
except SyntaxError:
    print("comma is missing.Enter number seperated by comma like this 1,2")
except:
    print("wronge input")
else:
    print("no Exceptions")
finally:
    print("this will execute no matter what")