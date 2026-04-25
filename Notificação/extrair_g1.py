from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# iniciar navegador
driver = webdriver.Chrome()

# abrir site
driver.get("https://g1.globo.com/")

# esperar carregar (simples, depois dá pra melhorar com WebDriverWait)
time.sleep(5)

# pegar manchetes principais
noticias = driver.find_elements(By.CSS_SELECTOR, 'a.feed-post-link')

dados = []

for noticia in noticias:
    titulo = noticia.text
    link = noticia.get_attribute("href")
    
    if titulo:  # evitar vazios
        dados.append([titulo, link])

# salvar em CSV
with open("noticias_g1.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Título", "Link"])
    writer.writerows(dados)

print(f"{len(dados)} notícias salvas!")

# fechar navegador
driver.quit()