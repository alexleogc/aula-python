def soma(a,b):
    return a+b

# Para compilar arquivo: python nome-do-programa.py

def main():

    print('Primeiro programa: \n')

    a = float(input('Valor de a: '))
    b = float(input('Valor de b: '))

    print(soma(a,b))
    
if  __name__ == "__main__":
    main()