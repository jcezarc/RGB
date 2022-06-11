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
        c1, c2 = [t.primeira_cor() for t in (self, tubo)]
        if c2 != '' and c2 != c1:
            return 0
        i = self.cores.index(c1)
        while self.cores[i] == c1 and ' ' in tubo.cores:
            j = ''.join(tubo.cores).rindex(' ')
            tubo.cores[j] = c1            
            self.cores[i] = ' '
            i += 1
        return i

    def completo(self) -> bool:
        primeira = self.primeira_cor()
        return all(c == primeira for c in self.todas_cores())
