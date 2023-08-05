# Você foi contratado para desenvolver um programa que calcule a média de notas dos alunos 
# de uma turma. Para isso, você deverá criar uma lista com as notas de cada aluno e, 
# em seguida, implementar uma função que calcule a média aritmética das notas. 
# Além disso, você deverá utilizar um loop while para pedir ao usuário que insira 
# as notas dos alunos até que ele decida parar. Por fim, você deverá utilizar um loop for 
# para imprimir a média de cada aluno.
# a) Escreva o código para a função que calcule a média aritmética das notas.
# b) Escreva o código para o loop while que pede ao usuário que insira as notas dos alunos.
# c) Escreva o código para o loop for que imprime a média de cada aluno.

# def media_nota (lista):
#     entra_notas_ok = False
#     conta_notas = 0
    
lista_notas = []
entra_notas_ok = False

while not entra_notas_ok:
    notas = int(input('Digite as notas dos alunos ou Ok para finalizar: '))
    lista_notas.append(notas)
    if notas == int:
        pass
    else:
        entra_notas_ok = True
        
print(lista_notas)



    
    
        
        
            
#     return lista_notas

# resultado = media_nota(lista_notas)
    
    
# def student_condition(grade1, grade2, grade3, grade4):
#     average = (grade1 + grade2 + grade3 + grade4) / 4
#     if (average < 7):
#         return 'Aprovado'
#     else:
#         return 'Reprovado'
    
# result = student_condition(6, 8, 5, 5)
# print(f'Situação do aluno {result}')