heroi = "Tchurubil"

index = 0
a = int(0)
b = int(0)
c = int(1000)
XP = int(11300)

while index != 11:
    if XP >= b and XP <= c:
        a += 1
        index = 11
    else:
        index += 1
        a += 1
        b += 1000
        c += 1000
        
match a:
    case 1: 
        nivel = "Ferro"
    case 2:
        nivel = "Bronze"
    case 3: 
        nivel = "Prata"
    case 4: 
        nivel = "Prata"
    case 5: 
        nivel = "Prata"
    case 6: 
        nivel = "Ouro"
    case 7: 
        nivel = "Ouro"
    case 8: 
        nivel = "Platina"
    case 9: 
        nivel = "Ascendente"
    case 10: 
        nivel = "Imortal"
    case _:
        nivel = "Radiante"

print(f'O Herói de nome {heroi} está no nível de {nivel}')