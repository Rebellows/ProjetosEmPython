print('}======================================================================================{')
choice = int(input('Faça sua escolha: \n[1] calculadora trigonométrica \n[2] calculadora de equações de segundo grau \n[3] conversor de moedas \n[4] Calculadora de roldanas \nO que deseja? '))
if choice == 1:
    print('}======================================================================================{')
    print('}=============={BOA NOITE COLEGA, ESSA É A CALCULADORA TRIGONOMÉTRICA!!!}=============={')
    print('}======================================================================================{')
    choice2 = int(input(
        'O que necessitas? \n[1] Cateto adjacente \n[2] Cateto oposto \n[3] Hipotenusa \n[4] Perímetro \n[5] Área \n[6] Razões trigonométricas \nQual sua escolha? '))
    print('}======================================================================================{')
    if choice2 == 1:
        hip = float(input('Valor da hipotenusa: '))
        opt = float(input('Valor do cateto oposto: '))
        adj1 = hip * hip - opt * opt
        adj2 = float(adj1) ** 0.5
        print(f'O cateto adjacente vale {adj2} !')
    if choice2 == 2:
        hip = float(input('Valor da hipotenusa: '))
        adj = float(input('Valor do cateto adjacente: '))
        opt1 = hip * hip - adj * adj
        opt2 = float(opt1) ** 0.5
        print(f'O cateto oposto vale {opt2} !')
    if choice2 == 3:
        adj = float(input('Valor do cateto adjacente: '))
        opt = float(input('Valor do cateto oposto: '))
        hip1 = adj * adj + opt * opt
        hip2 = float(hip1) ** 0.5
        print(f'A hipotenusa vale {hip2} !')
    if choice2 == 4:
        adj = float(input('Valor do cateto adjacente: '))
        opt = float(input('Valor do cateto oposto: '))
        hip = float(input('Valor da hipotenusa: '))
        perimetro = adj + opt + hip
        print(f'O perímetro vale {perimetro} !')
    if choice2 == 5:
        base = float(input('Valor da base: '))
        altura = float(input('Valor da altura: '))
        area = base * altura / 2
        print(f'O valor da área é {area} !')
    if choice2 == 6:
        print('}=================================={TRIGONOMETRIA!!!}=================================={')
        print('}======================================================================================{')
        choice = int(input('O que necessitas? \n[1] Seno \n[2] Cosseno \n[3] Tangente \nQual sua escolha? '))
        print('}======================================================================================{')
        if choice == 1:
            opt = float(input('Valor do cateto oposto: '))
            hip = float(input('Valor da hipotenusa: '))
            seno = opt / hip
            print(f'O valor de seno é {seno} !')
        if choice == 2:
            adj = float(input('Valor do cateto adjacente: '))
            hip = float(input('Valor da hipotenusa: '))
            cosseno = adj / hip
            print(f'O valor de cosseno é {cosseno} !')
        if choice == 3:
            opt = float(input('Valor do cateto oposto: '))
            adj = float(input('Valor do cateto adjacente: '))
            tang = opt / adj
            print(f'O valor da tangente é {tang} !')
        print(
            'Lembrando que: cossecante é o inverso de seno, secante é o inverso de cosseno e \ncotangente é o inverso da tangente.')
        print('}======================================================================================{')
if choice == 2:
    print('}======================================================================================{')
    print('}==========={BOA NOITE COLEGA, ESSA É A CALCULADORA DE FUNÇÃO DE 2º GRAU!!!}==========={')
    print('}======================================================================================{')
    a = int(input('Qual é o valor do A, colega? '))
    b = int(input('Qual é o valor do B, amigão? '))
    c = int(input('Qual é o valor do C, parceiro? '))
    print('}======================================================================================{')
    delta = b * b - 4 * a * c
    x1 = (-b + float(delta) ** 0.5) / (2 * a)
    x2 = (-b - float(delta) ** 0.5) / (2 * a)
    print(f'Paizão, seu delta é {delta}.')
    if delta < 0:
        print('Compadre, infelizmente a equação não possui resultados reais.')
    if delta == 0:
        print(
            f'Camarada, a equação possui apenas um resultado real ou possui dois resultados iguais, sendo eles {x1} e {x2}.')
    if delta > 0:
        print(f'a equação possui dois resultados distintos reais, sendo eles {x1} e {x2}.')
    print('}======================================================================================{')
if choice == 3:
    print('}======================================================================================{')
    print('}================={BOA NOITE COLEGA, ESSA É O CONVERSOR DE MOEDAS !!!}================={')
    print('}======================================================================================{')
    moeda = str(input('Qual a moeda que o senhor quer converter? [REAL / DÓLAR / EURO] ')).upper()
    if moeda == 'REAL':
        real = str(input('Ok amigo, e quer converter para qual moeda? [DÓLAR / EURO]  ')).upper()
        if real == 'DÓLAR' or 'DOLAR':
            quantia = int(input('Anotado patrão, agora me diga, qual a quantia a ser convertida? '))
            resultado = round(quantia / 5.05)
            print(f'Patrão, sua quantia resultou em ${resultado} !')
        if real == 'EURO':
            quantia2 = int(input('Anotado patrão, agora me diga, qual a quantia a ser convertida? '))
            resultado2 = round(quantia2 / 5.50)
            print(f'Patrão, sua quantia resultou em €{resultado2} !')
    if moeda == 'DÓLAR' or 'DOLAR':
        dolar = str(input('Ok amigo, e quer converter para qual moeda? [REAL / EURO]  ')).upper()
        if dolar == 'REAL':
            quantia3 = int(input('Anotado patrão, agora me diga, qual a quantia a ser convertida? '))
            resultado3 = round(quantia3 * 5.05)
            print(f'Patrão, sua quantia resultou em R${resultado3} !')
        if dolar == 'EURO':
            quantia4 = int(input('Anotado patrão, agora me diga, qual a quantia a ser convertida? '))
            resultado4 = round(quantia4 * 0.92)
            print(f'Patrão, sua quantia resultou em €{resultado4} !')
    if moeda == 'EURO':
        real = str(input('Ok amigo, e quer converter para qual moeda? [DÓLAR / REAL]  ')).upper()
        if real == 'DÓLAR' or 'DOLAR':
            quantia5 = int(input('Anotado patrão, agora me diga, qual a quantia a ser convertida? '))
            resultado5 = round(quantia5 * 1.09)
            print(f'Patrão, sua quantia resultou em ${resultado5} !')
        if real == 'REAL':
            quantia6 = int(input('Anotado patrão, agora me diga, qual a quantia a ser convertida? '))
            resultado6 = round(quantia6 * 5.50)
            print(f'Patrão, sua quantia resultou em R${resultado6} !')
    print('}======================================================================================{')
if choice == 4:
    print('}======================================================================================{')
    print('}==============={BOA NOITE COLEGA, ESSA É A CALCULADORA DE ROLDANAS !!!}==============={')
    print('}======================================================================================{')
    peso = int(input('Boa noite compadre, qual o peso que o senhor quer levantar? '))
    roldanas = int(input('Entendo amigo, e a quantidade de roldanas móveis que serão usadas é? '))
    baixo = pow(2, roldanas)
    fn = peso / baixo
    print(f'Interessante comparsa, o peso a ser levantado deduzindo as roldanas será  {fn} !')
    print('Lembre-se, roldanas móveis dividem o peso pela metade, enquanto roldanas fixas mantém \no mesmo peso.')
    print('}======================================================================================{')
