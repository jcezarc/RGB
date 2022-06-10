from colorama import init, Fore, Back, Style

CHAR_CORES = {
    'R': Back.RED+Fore.LIGHTMAGENTA_EX+'º',
    'G': Back.GREEN+Fore.LIGHTGREEN_EX+'º',
    'B': Back.BLUE+Fore.CYAN+'º',
    ' ': ' '
}
CORES_NORMAIS = Back.BLACK+Fore.WHITE
SEPARADOR = CORES_NORMAIS + '|  |'


init(autoreset=True)

def print_linhas(tubos: list, tamanho: int = 5):
    for i in range(tamanho):
        linha = []
        for tubo in tubos:
            cor = tubo.cores[i]
            linha.append(CHAR_CORES[cor])
        print(' |{}{}|'.format(
            SEPARADOR.join(linha),
            CORES_NORMAIS,
        ))
    rodape = '+-+  ' * tamanho
    numeros = ' {}   ' * tamanho
    print(' ' + Style.RESET_ALL + rodape)
    print(' ' + numeros.format(*range(1, tamanho+1)))
