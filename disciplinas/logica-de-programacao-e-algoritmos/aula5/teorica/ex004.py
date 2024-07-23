def ordem_cresc(x, y, z):
    if x and y and z:
        if x > y and x > z:
            if y > z:
                print(z, y, x)
            else:
                print(y, z, x)
        if y > x and y > z:
            if x > z:
                print(z, x, y)
            else:
                print(x, z, y)
        if z > x and z > y:
            if y > x:
                print(x, y, z)
            else:
                print(y, x, z)
    print(teste)  
      

x = int(input('Digite o valor 1: '))
y = int(input('Digite o valor 2: '))
z = int(input('Dgiite o valor 3: '))
teste = 'ovos'
ordem_cresc(x, y, z)
