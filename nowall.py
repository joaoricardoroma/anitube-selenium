import ipdb
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions

chromeOptions = ChromeOptions()
chromeOptions.add_argument("--window-size=1300,1000")
navegador = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chromeOptions)
url = "https://www.anitube.site/"
navegador.get(url)
print(navegador.title)
pesquisa = navegador.find_element_by_name("s")
pesquisa.send_keys(input("Qual anime voce deseja ver?"))
pesquisa.send_keys(Keys.RETURN)
try:
    navegador.find_element_by_class_name("aniItem")
except Exception as e:
    print("anime nao encontrado")
    navegador.quit()
    exit()
body = navegador.find_element_by_tag_name("body")
titulos = body.find_elements_by_class_name("aniItem")

for i, title in enumerate(titulos):
     nome = title.find_element_by_tag_name("a").get_attribute("title")
     print(f' {i} - {nome}')

print(f'Lista de animes achado')
selecao = input("Qual anime deseja ver?")

for i, anime in enumerate(titulos):
    nome = anime.find_element_by_tag_name("a").get_attribute("title")
    link = anime.find_element_by_tag_name("a").get_attribute("href")

    if i == int(selecao):
        print(f'{nome} acesse a pagina dele para assistir{link}')

pergunta_ultimoep = input("Deseja ver o ultimo episodio dele SIM/NAO?").lower()

if pergunta_ultimoep == "sim":
    titulos[int(selecao)].find_element_by_tag_name("a").click()
    container = navegador.find_element_by_class_name("pagAniListaContainer")
    lista_de_ep = container.find_elements_by_tag_name("a")
    ultimo_ep = lista_de_ep[-1]
    ultimo_ep.click()
    navegador.find_element_by_id("video").click()
else:

    print(f"Ent acesse a pagina do anime {link}")
