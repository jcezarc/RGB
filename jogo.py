from tubo import Tubo
from terminal import print_linhas


class Jogo:
    def __init__(self, tamanho: int):
        self.tubos = [
            Tubo(tamanho) for _ in range(tamanho-1)
        ] + [Tubo(tamanho, vazios=tamanho)] # -- o último é vazio

    def continuar(self) -> bool:
        return not all(t.completo() for t in self.tubos)

    def atualiza(self):
        print_linhas(self.tubos)
        opcao = input('Números dos tubos origem-destino: ')
        try:
            t1, t2 = self.par(opcao)
            ok = t1.despeja(t2)
        except:
            ok = False
        if not ok:
            print('\n\t*** Opção inválida ***\n')

    def par(self, expressao: str) -> list:
        i, j = [int(c)-1 for c in expressao if c.isdigit()]
        return self.tubos[i], self.tubos[j]
