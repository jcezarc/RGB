from random import choice


class Tubo:
    def __init__(self, tamanho: int):
        self.cores = [' ']
        while len(self.cores) < tamanho:
            self.cores.append(
                choice(['R', 'G', 'B'])
            )

    def primeira_cor(self) -> str:
        return next(
            (cor for cor in self.cores if cor != ' ')
            , ''
        )

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
        return ''.join(self.cores) == self.cores[0] * len(self.cores)
