from jogo import Jogo
from terminal import CLI

print('''
    ::::::  R.G.B. ::::::
    Separe as cores nos tubos
    até não ter cores misturadas.

    Como jogar: Digite o número do tubo de origem
    seguido do número do tubo de destino.
    Exemplo: "1 3" ou "1-3" ou "13"
    significa que o tubo 1 deve ser despejado no tubo 3

    Bom jogo!
''')
jogo = Jogo(
    interface=CLI(),
    tamanho=5  # 5 tubos de 5 cores cada
)
while jogo.continuar():
    jogo.atualiza()
print('=' * 50)
print('PARABÉNS!!'.center(50))
print('=' * 50)
jogo.finaliza()
