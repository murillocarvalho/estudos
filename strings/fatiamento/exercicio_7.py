"""
7. Domínio do E-mail:
   Dada a string email = "usuario@empresa.com", sabendo que o símbolo '@' 
   está no índice 7, faça um fatiamento que extraia apenas o domínio 
   "empresa.com".
"""

email = "usuario@empresa.com"
inicio = email.index('@')
print(email[inicio + 1:])