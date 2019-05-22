'''
UFRJ - Universidade Federal do Rio de Janeiro

IM - Instituto de Matematica

Pedro Feteira Gueventer - 119.017.382

Lista 4 - Questão 1
'''

def main():

    try:
        file = input('Qual o nome do arquivo?')
        arq = open(f'{file}','r')
        a=[]
        for line in arq.readlines():
            
            a.append( [ float(x) for x in line.split(',')] )
        for i in range(len(a[1])):
            if len(a[i]) != len(a[i+1]):
                raise IndexError
        print(f'{len(a),len(a[1])}')
        for l in range(0, len(a)):
            for c in range(0,len(a[1])):
                print(f'{a[l][c]}', end = ' ')
            print()
            
    except FileNotFoundError:
        print('\nArquivo não encontrado, tente novamente.\n')
        main()
    except IndexError:
        print('Linhas de tamanhos')
main()    
    
        

