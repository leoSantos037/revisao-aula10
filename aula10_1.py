def num_of_characters(text):
  total_count = len(text)   #  a quantidde total de caracteres incluindo tudo, inclusive espaços e pontuação
  spaces = 0
  punctuations = 0

  for each_letter in text:
    if each_letter == ' ':
      spaces += 1
    
    if each_letter == '.' or each_letter == ',' or each_letter == '!' or each_letter == '?':
      punctuations += 1
  
  #  de total_count vamos subtrair quantos espaços e quantas pontuações
  letters_count = total_count - spaces - punctuations
  
  #  a funcao retornara 3 valores
  return letters_count, spaces, punctuations

#  vamos pedir ao usuario pra digitar uma mensagem qualquer
msg = input('Digite a mensagem: ')

#  vamos chamar a funcao num_of_caracters e passar pra ela a mensagem digitada pelo usuario
total_characteres = num_of_characters(msg)

print(total_characteres)
