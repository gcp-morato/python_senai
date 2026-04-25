#  Escrever em arquivos

'''
Comando para Ler e Escrever Arquivos

with open(file="caminho do arquivo", mode='Modo de Leitura ou Escrita', 
    encoding='decodificado') as apelido:
        bloco de código
'''

'''
O Modo de Escrita - W
O Modo de Leitura - R
O Modo de Acréscimo - A
'''
nome_do_arquivo = "pepsico.txt"

with open(file=nome_do_arquivo, mode="w", encoding='utf8') as arquivo:
    print(f'''Em 1992, nas Filipinas, ocorreu o Incidente 349, uma promoção da Empresa Pepsi, se
          tornou um desastre. Tampinhas premiadas com números diários, resutariam em um 
          grande prêmio. Em 25 maio, o numero 349 foi anunciado como vencedor, mas um erro 
          de programação fezcom que inúmeras tampinhas tivesse esse número ''', file=arquivo)
