"""
8. Espelhamento Parcial:
   Dada a string s = "ABCDEF", exiba os 3 primeiros caracteres ("ABC") 
   seguidos pelos mesmos 3 caracteres invertidos ("CBA"), resultando em "ABCCBA".
"""

s = "ABCDEF"
parte1 = s[:3]
parte2 = s[2::-1]
print(parte1 + parte2)
print(f"{s[:3]}{s[2::-1]}")