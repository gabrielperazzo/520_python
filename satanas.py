#!/usr/bin/python3

import random

def soma(a, b):
    return a + b

print(soma(5, 10))

def subtrai(a, b):
    return a - b

print(subtrai(5, 10))

def multiplica(a, b):
    return a * b

print(multiplica(5, 10))

def divide(a, b):
    return a / b

print(divide(5, 10))

def satanas(a):
    return (soma(a[0], a[1]) + subtrai(a[2], a[3]) + multiplica(a[4], a[5]) + divide(a[6], a[7]))

lista = []
for i in range(8):
    lista.append(random.randint(1,100))

print(satanas(lista))

#def textao_do_facebook(nome):
#    textao = '''Nunca é {0} demais lembrar o peso e o significado destes problemas, uma vez que a determinação clara de objetivos talvez venha a ressaltar a relatividade das novas proposições. Percebemos, cada vez mais, que o acompanhamento das preferências de consumo oferece uma interessante oportunidade para verificação das condições inegavelmente apropriadas. Por conseguinte, a adoção de políticas descentralizadoras acarreta um processo de reformulação e modernização das regras de conduta normativas. 
#Não obstante, a estrutura atual da organização assume importantes posições no estabelecimento dos níveis de motivação departamental
#É claro que o novo modelo estrutural aqui preconizado exige a precisão e a definição das direções preferenciais no sentido do progresso. A prática cotidiana prova que o desafiador cenário globalizado auxilia a preparação e a composição de todos os recursos funcionais envolvidos. Pensando mais a longo prazo, a consolidação das estruturas aponta para a melhoria dos modos de operação convencionais.
#As experiências acumuladas demonstram que o fenômeno da Internet causa impacto indireto na reavaliação do impacto na agilidade decisória. Gostaria de enfatizar que a percepção das dificuldades cumpre um papel essencial na formulação dos conhecimentos estratégicos para atingir a excelência. No entanto, não podemos esquecer que o aumento do diálogo entre os diferentes setores produtivos garante a contribuição de um grupo importante na determinação das formas de ação.'''
#    print(textao.format(nome))



#textao_do_facebook('Vanderlei')
#textao_do_facebook('Daniel')
#textao_do_facebook('Eduardo')