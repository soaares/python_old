# Desafio 96

sonic = {'x_position':25,'y_position':0,'speed':'slow'}
print("A posição original Sonic em X é: " + str(sonic['x_position']))
if sonic['speed'] == 'slow':
    acrescimo = 2
elif sonic['speed'] == 'medium':
    acrescimo = 1
elif sonic['speed'] == 'fast':
    acrescimo = 0
sonic['x_position'] = sonic['x_position'] + acrescimo
print("O Sonic se moveu e agora a posição dele em X é: " + str(sonic['x_position']))

# Crio um dicionário chamado 'sonic' e defino sua posição em x, y e sua velocidade.
# Em seguida fazemos os testes condicionais, se a velocidade for 'slow' crio uma
# variável e defino o valor como '2', no elif, caso a velocidade seja 'medium'
# a variável terá o valor de '1' e no segundo elif, caso a velocidade seja 'fast'
# a variável vale '0', depois defino que o valor de sonic['x_position'] será
# igual a seu valor atual + o valor da variavel criada nos testes condicionais
# por fim, imprimo a msg com a atual posição de Sonic em X. 