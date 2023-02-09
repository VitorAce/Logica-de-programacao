''''
Projeto - Medidor de Velocidade

Levando em consideração a velocidade máxima permitida de 80km em uma determinada rua. Crie um programa que recebe do úsuario um valor que representa a velocidade e com base nessa velocidade diga se ela tomou uma multa leve, grave ou gravíssima. Levando em consideração que se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir "não houve multa", caso esteja até 10km acima, deve exibir: "levou multa leve", caso esteja entre 11 a 20 acima da velocodade máxima, exibe: "levou multa grave", e caso esteja acima de 20 km acima da velocidade maáxim, exibe "levou multa gravíssima"

Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investique mais até você compreender completamente o problema.)

1. Quais são os dados de entrda necesssários ?
- Velocidade
2. Oque devo fazer com estes dados ?
Levando em consideração que se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir "não houve multa, caso esteja até 10 km acima, deve exibir: "levou multa leve", caso esteja 11 e 20 km acima da velocidade máxima, exibir: "levou multa grave", e caso esteja acima de 20km acimada velocidade máxima, exibir: "levou multa gravissima"
3. Quais são as restrições deste problema ?
4. Qual é o resultado esperado ?
-  O resultado esperado é exibir a mesma mensagem que corresnpode ao nível da múlta que a pessoa levou (deve exibir: "levou multa leve", caso esteja entre 11 a 20km acima da velocidade máxima, exibir: "levou multa grave", e caso esteja acima de 20km da velocidade máxima, exiba: " levou multa gravissima")
5. Qual é seguência de passos a ser feitas para chegar ao resultado esperado ?
input vrlocidade
valocidade_maxima = 80
if velocidade <= velocidade_maxima:
  print 'Não levou multa'
if velocidade > velocidade_maxima e velocidade <= velocidade_maxima + 10:
  print 'Levou multa leve'
if velocidade > velocidade_maxima + 11 e velocidade <= velocidade_maxima + 20:
  print 'Levou multa grave'
if velocidade > velocidade_maxima + 20
  print 'Levou multa gravíssima'
'''
velocidade = int(input('Digite sua velocidade'))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
  print('Não levou multa')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
  print('Levou uma multa leve')
elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
  print('Levou multa grave')
elif velocidade > velocidade_maxima + 20:
  print('Levou multa gravíssima')