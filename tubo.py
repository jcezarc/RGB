from random import choice


class Tubo:
    def __init__(self, tamanho: int, vazios: int=1):
        self.cores = [' ']*vazios
        while len(self.cores) < tamanho:
            self.cores.append(
                choice(['R', 'G', 'B'])
            )

    def todas_cores(self) -> list:
        return [c for c in self.cores if c != ' ']

    def primeira_cor(self) -> str:
        return next(iter(self.todas_cores()), '')

    def despeja(self, tubo):
        p1, p2 = [t.primeira_cor() for t in (self, tubo)]
        if p2 != '' and p2 != p1:
            return False
        if ' ' not in tubo.cores:
            return False
        i = ''.join(tubo.cores).rindex(' ')
        tubo.cores[i] = p1
        i = self.cores.index(p1)
        self.cores[i] = ' '
        return True

    def completo(self) -> bool:
        primeira = self.primeira_cor()
        return all(c == primeira for c in self.todas_cores())
