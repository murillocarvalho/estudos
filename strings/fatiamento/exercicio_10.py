"""
10. Substrings Alternadas:
    Dada a string s = "abcdefghijklmnop", divida-a ao meio e exiba apenas 
    os caracteres de índice par da primeira metade da string.
"""

s = "abcdefghijklmnop"
parte1 = s[:int(len(s)/2):]

print(parte1)

print(parte1[::2])