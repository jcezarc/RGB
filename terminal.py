from colorama import init, Fore, Style

CHAR_CORES = {
    'R': Fore.RED+'*',
    'G': Fore.GREEN+'*',
    'B': Fore.BLUE+'*',
    ' ': ' '
}


init(autoreset=True)

def print_linhas(tubos: list, tamanho: int = 5):
    for i in range(tamanho):
        linha = []
        for tubo in tubos:
            cor = tubo.cores[i]
            linha.append(CHAR_CORES[cor])
        print(' |{}|'.format(
            '|  |'.join(linha)
        ))
    rodape = '+-+  ' * tamanho
    numeros = ' {}   ' * tamanho
    print(' ' + Style.RESET_ALL + rodape)
    print(' ' + numeros.format(*range(1, tamanho+1)))
