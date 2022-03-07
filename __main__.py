from src.main.python.controllers.__init__ import __init__ as controller
from src.main.python.testes.__test__ import __test__ as testeCode

import time


def main():
    controller()


def test():
    testeCode()


if __name__ == '__main__':
    inicio = time.time()
    test()
    main()
    fim = time.time() - inicio
    print('tempo de execução: ', round(fim, 2), ' seg')
