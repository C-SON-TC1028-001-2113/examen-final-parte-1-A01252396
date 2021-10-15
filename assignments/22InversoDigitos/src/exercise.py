def main():
    num = int(input("Enter a number: "))
    L=len(str(num))
    if L<=6:
        if num>0:
            num1=int(str(num)[::-1])
            print(num1)
        elif num<0:
            num=num*-1
            num1=int(str(num)[::-1])    
            num2=num1*-1
            print(num2)
    else:
        print('Too long')    
    #escribe tu código abajo de esta línea
if __name__=='__main__':
    main()