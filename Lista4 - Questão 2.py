'''
UFRJ - Universidade Federal do Rio de Janeiro

IM - Instituto de Matematica

Pedro Feteira Gueventer - 119.017.382

Lista 4 - Questão 2
'''
def inicial():
    a = []
    for i in range (-discos,0):
        a.append(-i)
    print('\nA posição inicial dos discos é:')
    print('\nA|',a)
    print('B|')
    print('C|\n')

def final():
    a = []
    for i in range (-discos,0):
        a.append(-i)
    print('\nA posição final dos discos é:')
    print('\nA|')
    print('B|')
    print('C|',a)

def hanói(discos, inicial, auxiliar, final):
    global contador
    if discos == 1:
        contador +=1
        print('Mova o disco 1 do pino {} ao pino {}.'.format(inicial, final), contador,'Movimentos')
        return
    hanói(discos - 1, inicial, final, auxiliar)
    contador +=1
    input()
    print('Mova o disco {} do pino {} ao pino {}.'.format(discos, inicial, final),contador,'Movimentos')
    
    input()
    hanói(discos - 1, auxiliar, inicial, final)

def hanói_noenter(discos, inicial, auxiliar, final):
    global contador
    if discos == 1:
        contador +=1
        print('Mova o disco 1 do pino {} ao pino {}.'.format(inicial, final), contador,'Movimentos')
        return
    hanói_noenter(discos - 1, inicial, final, auxiliar)
    contador +=1
    
    print('Mova o disco {} do pino {} ao pino {}.'.format(discos, inicial, final),contador,'Movimentos')
    
    
    hanói_noenter(discos - 1, auxiliar, inicial, final)    
    
n = 1
s = 2
contador = 0
discos = int(input('Quantos discos? '))
inicial()
Enter = input('Deseja apertar Enter para cada passo?("s" para sim e "n" para não)')
if Enter == "s":
    hanói(discos, 'A', 'B', 'C')
if Enter == "n":
    hanói_noenter(discos, 'A', 'B', 'C')
final()
