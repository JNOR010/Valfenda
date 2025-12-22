frase = 'O python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.'

print(frase.count)

i = 0

while i < len(frase):
    letra = frase[i]
    quantidade = frase.count(letra)
    print(f'A letra "{letra}" aparece {quantidade} vezes na frase.')
    i += 1