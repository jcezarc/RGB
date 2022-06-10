from colorama import init, Fore, Back, Style

CHAR_CORES = {
    'R': Back.RED+Fore.LIGHTMAGENTA_EX+'º',
    'G': Back.GREEN+Fore.LIGHTGREEN_EX+'º',
    'B': Back.BLUE+Fore.CYAN+'º',
    ' ': ' '
}
CORES_NORMAIS = Back.BLACK+Fore.WHITE
SEPARADOR = CORES_NORMAIS + '|  |'

class CLI:
    def __init__(self):
        init(autoreset=True)

    def menu(self, tubos: list, perguntar: bool = True):
        for linha in map(list, zip(*[t.cores for t in tubos])):
            print(' |{}{}|'.format(
                SEPARADOR.join(CHAR_CORES[c] for c in linha),
                CORES_NORMAIS,
            ))
        tamanho = len(tubos)
        numeros = ' {}   ' * tamanho
        print(' {}{}\n {}'.format(
            Style.RESET_ALL, '+-+  ' * tamanho,
            numeros.format(*range(1, tamanho+1))
        ))
        if perguntar:
            return input('Números dos tubos origem-destino: ')
