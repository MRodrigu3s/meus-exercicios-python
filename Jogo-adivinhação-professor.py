

numero_secreto = 42
palpite = 0

while palpite != numero_secreto:
    palpite_str = input('coloque um numero: ')
    if palpite_str.isdigit():
        
        palpite = int(palpite_str) 
        
        if palpite > numero_secreto:
            print ('numero maior que o secreto')
        
        elif palpite < numero_secreto:
            print ('numero menor que o secreto')
             
    else:
        print ('numero invalido')
print ('VOCE ACERTOU')