#calculator
import art
def add(n1,n2):
     return n1+n2
def subtract(n1,n2):
     return n1 -n2
def multiply(n1,n2):
     return n1*n2
def division(n1,n2):
     return n1/n2
operation=({
     "+":add,
     "-":subtract,
     "*":multiply,
     "/":division
})
def calculator():
     print(art.logo)
     should_accumulate=True
     num1= float(input("what is your first number?: "))
     while should_accumulate:
          for symbol in operation:
               print(symbol)
          operation_symbol=input("pick an operation: ")
          num2=float(input("what the next number?: "))
          answer=operation[operation_symbol](num1,num2)
          print(f"{num1} {operation_symbol} {num2}= {answer}")
          choice=input(f" Type 'y' to continue calculating with {answer} or Type 'n' to start new calculation: ")
          if choice=="y":
               num1=answer
          else:
               should_accumulate=False
               print("\n " * 20 )
               calculator()
calculator()





















