'''
UFRJ - Universidade Federal do Rio de Janeiro

IM - Instituto de Matematica

Pedro Feteira Gueventer - 119.017.382
'''
#Código que representa um preenchimento como o do paint
#mas que apenas substitui 1 por 0

import sys
mat1 = input('Qual o nome do arquivo?\n')

print('Esse é o original\n')

arq = open(f'{mat1}','r')
texto = arq.read()



lines = texto.strip().split('\n')
assert ['largura ruim' for x in lines if len(x) != len(lines[0])] == [], "É preciso que seja retangular"

def Lista(texto):
    Largura = len(texto.strip().split('\n')[0])
    altura = len(texto.strip().split('\n'))

    texto = texto.strip().split('\n')

    mat = []
    for i in range(Largura):
        mat.append([''] * altura)
    for x in range(Largura):
        for y in range(altura):
            mat[x][y] = texto[y][x]
    return mat


def printMat(mat):
    Largura = len(mat)
    altura = len(mat[0])

    for y in range(altura):
        for x in range(Largura):
            sys.stdout.write(mat[x][y])
        sys.stdout.write('\n')


def floodFill(mat, x, y):

    Largura = len(mat)
    altura = len(mat[0])

    if mat[x][y] != '1':
        return
    mat[x][y] = '0'

    if x > 0: 
        floodFill(mat, x-1, y)

    if y > 0: 
        floodFill(mat, x, y-1)

    if x < Largura-1: 
        floodFill(mat, x+1, y)

    if y < altura-1: 
        floodFill(mat, x, y+1)

def main():
    mat = Lista(texto)
    printMat(mat)
    print()
    print('Uma coordenada (a,b) deve ser escolhida para onde começar o preenchimento')
    print()
    a = int(input("Qual a coordenada 'a'?"))
    b = int(input("Qual a coordenada 'b'?"))
    print('Esse é com o preenchimento')
    print()
            
    floodFill(mat, a, b)
    printMat(mat)
    print()



if __name__ == '__main__':
    main()



    









