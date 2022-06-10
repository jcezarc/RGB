from tubo import Tubo


class Jogo:
    def __init__(self, tamanho: int, interface):
        self.tubos = [
            Tubo(tamanho) for _ in range(tamanho-1)
        ] + [Tubo(tamanho, vazios=tamanho)] # -- o último é vazio
        self.interface = interface

    def continuar(self) -> bool:
        return not all(t.completo() for t in self.tubos)

    def atualiza(self):
        opcao = self.interface.menu(self.tubos)
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

    def finaliza(self):
        self.interface.menu(self.tubos, perguntar=False)
