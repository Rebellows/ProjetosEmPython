from collections import Counter
import pandas as pd
palavra = str(input('Qual é a palavra de Deus, irmão? ')).lower()
letra = 0
counter = Counter(palavra)
for caracter in counter:
    if caracter in 'abcdefghijklmonpqrstuvwxyzç':
        letra = letra + 1
        resultado = 1
        for n in range(1, letra + 1):
            resultado *= n
        my_df = pd.DataFrame(counter)
        sum(my_df.abcdefghijklmonpqrstuvwxyzç > 1)
        if sum is True:
            print(resultado)