# -------------------------------------------------------------------------
# SCRIPT DE AUTOMAÇÃO E RASPAGEM DE DADOS (WEB SCRAPING)
# OBJETIVO: Coletar títulos e preços, aplicando limpeza de dados (strip)
# -------------------------------------------------------------------------

# IMPORTAÇÕES: Trazendo as ferramentas necessárias para o projeto
from selenium import webdriver # O controle principal do navegador
from selenium.webdriver.chrome.service import Service # Gerencia o serviço do driver no Windows
from webdriver_manager.chrome import ChromeDriverManager # Faz o download automático do Driver correto
from selenium.webdriver.common.by import By # Permite localizar elementos por ID, Classe ou XPATH
import time # Usado para criar pausas e respeitar o carregamento da página

# ESTRUTURA TRY: Tenta executar o bloco de código abaixo
try:
    print("Iniciando o sistema e verificando versão do navegador...")
    
    # Configuração automática: O Service baixa e instala o driver compatível sozinho
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)

    # Define um tempo de espera padrão (se a internet estiver lenta, ele aguarda até 10s)
    navegador.implicitly_wait(10)

    # ACESSO: Comando para o navegador abrir o site alvo
    print("Acessando o site alvo...")
    navegador.get("http://books.toscrape.com/")
    
    # Pausa de 2 segundos para garantir que o layout carregou (importante em Alumínio)
    time.sleep(2)

    # CAPTURA: Localiza todos os blocos de livros (tag <article>) na página
    print("Localizando informações na tela...")
    livros = navegador.find_elements(By.TAG_NAME, "article")

    # LOOP: Repete o processo para cada livro encontrado na lista
    for livro in livros:
        
        # BUSCA DO TÍTULO: Entra na tag h3, depois no link <a> e pega o atributo 'title'
        # .strip() -> REMOVE espaços inúteis no início e fim (Correção do erro do Pandas!)
        titulo_bruto = livro.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")
        titulo_limpo = titulo_bruto.strip()

        # BUSCA DO PREÇO: Procura pela classe CSS 'price_color'
        # .replace() -> Troca o símbolo da moeda por nada, deixando só o valor
        preco_bruto = livro.find_element(By.CLASS_NAME, "price_color").text
        preco_limpo = preco_bruto.replace('£', '').strip()

        # EXIBIÇÃO: Mostra os dados já tratados no terminal
        print(f"LIVRO: {titulo_limpo} | VALOR: {preco_limpo}")

# ESTRUTURA EXCEPT: Se o código der qualquer erro, ele cai aqui em vez de "fechar sozinho"
except Exception as erro:
    print(f"ALERTA DE SISTEMA: Ocorreu um erro durante a execução -> {erro}")

# ESTRUTURA FINALLY: Este bloco sempre será executado ao final, dando erro ou não
finally:
    print("\n---------------------------------------------------------")
    print("OPERAÇÃO FINALIZADA!")
    print("Pressione ENTER para encerrar o navegador e o script.")
    print("---------------------------------------------------------")
    input() # Mantém a janela aberta para o aluno ver o resultado final
    navegador.quit() # Encerra o processo do navegador no Gerenciador de Tarefas