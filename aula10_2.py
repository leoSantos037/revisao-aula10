# Crie uma função em Python que verifica se o usuário
# digitou um e-mail válido.
# Deve possuir pelo menos um caracter "@" e um caracter "."
# após o "@"

# def verificador(email):
#     arroba = 0
#     ponto = 0
#     for letras in email:
#         if letras == '@':
#             arroba = 1
#         elif letras == '.':
#             ponto = 1
#         elif arroba == 1 and ponto == 1:
#             return '>> E-mail Válido <<'
#         else:
#             return '>> E-mail Inválido <<'
        
                
# msg = input('Digite um e-mail: ')

# resultado = verificador(msg)

# print(resultado)

def verifica_email(email):
    count_at = 0
    count_dot = 0
    posicao_at = 0
    posicao_dot = 0
    posicao = 0
    for letra in email:
        posicao += 1
        if letra == '@':
            count_at += 1
            posicao_at = posicao            
        if letra == '.':
            count_dot += 1
            posicao_dot = posicao
    if count_at == 1 and count_dot > 0 and posicao_at < posicao_dot:
        return '>> E-mail Válido <<'
    else:
        return '>> E-mail Inválido <<'
    
email_usuario = input('Digita seu e-mail: ')
    
resultado_validacao = verifica_email(email_usuario)
            
print(resultado_validacao)
