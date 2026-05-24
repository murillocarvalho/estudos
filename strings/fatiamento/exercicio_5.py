"""
5. Extração Central:
   Dada a string s = "TextoInutil[PROJETO-X]TextoInutil", utilize o fatiamento 
   para extrair apenas o trecho "[PROJETO-X]". Dica: conte os índices 
   ou use índices negativos para facilitar.
"""

'''
toda essa função abaixo pode ser substituida pelo comando s.index()
'''
def localizarChar(palavra:str) -> list:
   ref = []
   for cont, letra in enumerate(palavra):
      if letra == "[" or letra == "]":
         ref.append(cont)
   return ref

s = "TextoInutil[PROJETO-X]TextoInutil"
inicio, fim = localizarChar(s)
inicio2 = s.index('[')
fim2 = s.index(']')
print(s[inicio:fim + 1])
print(s[inicio2:fim2 + 1])