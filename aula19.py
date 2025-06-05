"""
Formatação básica de strings
s - string
d - int
f - floa
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou - 
ex: 0>-100, 1.f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'O hexadecimal de 1500 é {1500:08X}')