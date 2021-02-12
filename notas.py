# divisão com casa decimal usa somente uma barra"/"
# sem casa decimal usa duas barras "/"
#
# While True: - executa tudo que está dentro do código para sempre.
#
# input - para o comando e pede para de digite na tela
#
# eval - executa a variável como se fosse código
#
# print - mostra o código na tela
print("Aspas simples conseguem enrar dentro de aspas duplas tp `assim` oq vir primeiro e a que conta")
print("Quando eu usar numeors com virgula eu usarei `float` antes")
print("5 + A n tem como mas se eu colocar aspas no numero ele consegue juntar nao somar e sim juntar mas se eu colocar asapas em 2 numeros eu juntaria 2 numeros sem somar apenas juntando")
print("Um exemplo de juntar numeros sem somar e repetilos como funcao abaixo")
print('-5.55'*20)
print("Que e bem diferente de")
print(-5.55*20)
print("Print com P maiusculo N EXISTEEEEEEEEEEEEE")
print("VARIAVEIS---------------------------------------------------------------------------")
print('Variaveis tipos:""(string),0(int),<>=(boolean)')
print("so pode usar letras minusculas nas variaveis")
banco = 'next'
cpf = 19283642
o_quanto_vai_investir = 'R$1000'

print('O banco escolhido foi:',banco)
print('O cpf do corretor e:',cpf)
print('O quanto o cliente vai investir e:',o_quanto_vai_investir)
print('C cliente de cpf cujo',cpf ,'escolheu o banco',banco,'para investir',o_quanto_vai_investir)

print('DE OUTRA FORMA SERIA-----------------------')


print('O cliente {pessoa} escolheu {banco} para investir {valor}'.format(pessoa=cpf, banco=banco, valor=o_quanto_vai_investir))

print('DE OUTRA FORMA  MELHOR AINDA SERIA-----------------------')

print(f'O cliente {cpf} escolheu {banco} para invesitr{o_quanto_vai_investir}')

dados_clientes = f'''
O cpf do cliente e {cpf}
O banco dele {banco}
Oivestimentodo cara {o_quanto_vai_investir}'''
print(dados_clientes)

fatura = 500
numero_faturas = "20"

print(f"O total que sera pago",fatura* float(numero_faturas))
print('ENTRADA DE DADOS_______________________________________________________________________________________')

cota = 30
investimento = 200
numeors_cotas = 10
cotas_compradas = investimento/cota
pergunta = input('quantas cotas deseja comprar?')
compar_cota = investimento-int(pergunta)*cota

if investimento < cota:
     print("voce nao tem mais dinheiro para comprar cotas")


elif investimento>cota:
     print("Voce ainda tem dinheiro para comprar cotas")
     print(compar_cota)
print("---------------------------------------------------------------------")
pessoa = 1000
easyinvest = "easyinvest"
rico = "rico"
xp = "xp"
clear = "clear"
rico_valor = 1100
xp_valor = 800
clear_valor = 1200
easyinvest_valor = 900
pergunta_do_banco = input("Qual banco vc deseja investir?")

if pergunta_do_banco == xp and pessoa>=xp_valor:
    print("Voce pode investir nesse banco")
elif pergunta_do_banco == rico and pessoa>=rico_valor:
    print("Voce pode investir nesse banco")
elif pergunta_do_banco == easyinvest and pessoa>=easyinvest_valor:
    print("Voce pode investir nesse banco")
elif pergunta_do_banco == clear and pessoa>=clear_valor:
    print("Voce pode investir nesse banco")
else:
    print(("Voce nao pode investir nesse banco"))

# :s - Texto (strings)
# :d - inteiros (int)
# :f - numero de ponto flutuante (float)
# :.(NUMERO)f - Quantidade de casas decimais(float)
# : (CARACTERE)(> ou < ou ^) (QUANTIDADE)(TIPO - s, d ou f)
# > - esquerda
# < - direita
# ^ - centro
pessoa = 3000
easyinvest = "easyinvest"
rico = "rico"
xp = "xp"
clear = "clear"
pergunta_do_banco = input("Qual banco vc deseja investir?")
quanto_investir = input("quanto deseja aplicar?")
conta = pessoa - int(quanto_investir)

while conta>800:

    print(f"foi investido {quanto_investir}  no banco {pergunta_do_banco}")
    pergunta_2investimento = input(f"Deseja investir em outro banco?se sim qual?sobrou {conta}")
    if pergunta_2investimento == 'nao':
        break
    quanto_2investimento = input("quanto deseja aplicar?")
    conta = pessoa - int(quanto_investir) - int(quanto_2investimento)
    print(f"foi investido {quanto_2investimento}  no banco {pergunta_2investimento}")
else:
    print("Nao se pode investir com menos de 800")

    # listas python--------------------------------------------------------------------------------------------
    # fatiamento
    # append(bota um elemento no final da lista)
    # insert(bota um elemento em qualquer lugar que vc queira)
    # pop(exclui o ultimo elemento)
    # del(exclui o valor escolhido)
    # clear ,extend,+ min, max , range
    # startswith(confere se algum valor da lista comeca  com tal letra)
    # slip(consegue transformar uma string em uma lista)
    # join(consegue juntar uma lista para formar uma string)
    #replace(trocar algo quando existir algo)
idade = input('Qual sua idade?')
if not  idade.isnumeric():
    print("idade so pode ser numero")
else:
    idade = int(idade)
    maior_de_idade = (idade >=18)
    msg = 'pode acessar' if maior_de_idade else 'nao pode acessar'
    print(msg)


 def funcao():
        print('Hey brow')
    funcao()
    funcao()
#list comprehension:----------------------------------------------------------------------------------------
l1 = [1,2,3,4,5,6,7,8,]
l1_comp = [v for v in l1]

teste = [v * 3 for v in l1]
teste2 =[(v, v2) for v in l1 for v2 in range(3)]

lista = ['luiz','mauro','maria']
teste3 = [v.replace('a','@')for v in lista]
print(teste3)


def dobre_lista(lista):
    return [x*10 for x in lista]
lista = [1,2,3,4,5]
print(dobre_lista(lista))
#classes_++++++++++++++++++++++++++++++++++++++++++++++++++++=----------------------------------------------
from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
       self.nome = nome
       self.idade = idade
       self.comendo = comendo
       self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

p1 = Pessoa('Breno', 17)
p2 = Pessoa('João', 17)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
-----------------------------------------------------------------------------------------------
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto (self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))
#Getter
    @property
    def preco(self):
        return self._preco
#Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('$',''))
        self._preco = valor

p1 = Produto('Camisa', 50)
p1.desconto(10)
print(p1.preco)

p2 = Produto ('Caneca', '$60')
p2.desconto(10)
print(p2.preco)
#__dict____ procura no bruto qual era o numero-------------------------------------------------------------------------------------------------------------------
class alpha:
    def __init__(self, nome, cidade, ):
        self.nome = nome
        self.cidade = cidade
        self.ceu = ""
        self.temp = ""
        self.feels_like = ""
        self.min = ""
        self.max = ""

    def informacoes(self, ceu, temp, feels_like, min, max):
        self.ceu = ceu
        self.temp =  self.conversor(temp)
        self.feels_like = self.conversor(feels_like)
        self.min = self.conversor(min)
        self.max = self.conversor(max)


    def conversor(self, entrada):
        F = entrada
        C = F - 273.15
        return round(C, 2)

        from classes import alpha

    import requests
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Gggg&appid=3ae582d0ed72e41b0e6a53f1590e92f0')
    data = r.json()
    # print(data['main']['temp'])
    print(r.status_code)

    exit()

    obj_alpha = alpha(input("Qual o seu nome?"), input("Qual sua cidade?"))
    print(f'{obj_alpha.nome} {obj_alpha.cidade}')

    pergunta2 = input('Deseja ver o clima da sua cidade?')
    if pergunta2 == "Sim":

        print(f'{obj_alpha.cidade}')

        if obj_alpha.cidade == 'Guapimirim':
            obj_alpha.informacoes("few clouds", 305.83, 305.23, 302.04, 310.15)
            print(f"temp:{obj_alpha.temp}, "
                  f"Ceu:{obj_alpha.ceu}, "
                  f"feels_like:{obj_alpha.feels_like}, "
                  f"min:{obj_alpha.min}, "
                  f"max:{obj_alpha.max}, ")
        elif obj_alpha.cidade == 'Teresopolis':
            obj_alpha.informacoes("few clouds", 302.59, 305.28, 302.59, 302.59)
            print(f"temp:{obj_alpha.temp}, "
                  f"Ceu:{obj_alpha.ceu}, "
                  f"feels_like:{obj_alpha.feels_like}, "
                  f"min:{obj_alpha.min}, "
                  f"max:{obj_alpha.max}, ")
        elif obj_alpha.cidade == 'Guaratiba':
            obj_alpha.informacoes("scattered clouds", 309.79, 308.66, 305.93, 313.15)
            print(f"temp:{obj_alpha.temp}, "
                  f"Ceu:{obj_alpha.ceu}, "
                  f"feels_like:{obj_alpha.feels_like}, "
                  f"min:{obj_alpha.min}, "
                  f"max:{obj_alpha.max}, ")
    else:

        obj_alpha = alpha("usuario sem nome", input("Qual cidadade voce deseja ver o clima?"))

        if obj_alpha.cidade == 'Guapimirim':
            obj_alpha.informacoes("few clouds", 305.83, 305.23, 302.04, 310.15)
            print(f"temp:{obj_alpha.temp}, "
                  f"Ceu:{obj_alpha.ceu}, "
                  f"feels_like:{obj_alpha.feels_like}, "
                  f"min:{obj_alpha.min}, "
                  f"max:{obj_alpha.max}, ")
        elif obj_alpha.cidade == 'Teresopolis':
            obj_alpha.informacoes("few clouds", 302.59, 305.28, 302.59, 302.59)
            print(f"temp:{obj_alpha.temp}, "
                  f"Ceu:{obj_alpha.ceu}, "
                  f"feels_like:{obj_alpha.feels_like}, "
                  f"min:{obj_alpha.min}, "
                  f"max:{obj_alpha.max}, ")
        elif obj_alpha.cidade == 'Guaratiba':
            obj_alpha.informacoes("scattered clouds", 309.79, 308.66, 305.93, 313.15)
            print(f"temp:{obj_alpha.temp}, "
                  f"Ceu:{obj_alpha.ceu}, "
                  f"feels_like:{obj_alpha.feels_like}, "
                  f"min:{obj_alpha.min}, "
                  f"max:{obj_alpha.max}, ")

------------------------------------------------------------------------------------------------------------------
import requests
conversor = - 273.15
while True:
    lugar = input("Qual lugar deseja saber o clima?")
    r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={lugar}&appid=3ae582d0ed72e41b0e6a53f1590e92f0')
    data = r.json()
    if r.status_code != 200:
        print("Nome do pais incorreto escreva denovo")
        continue
    print("opcoes")
    print("1) Temperatura")
    print("2) Sensacao termica")
    print("3) Temperatura minima")
    print("4) Temperatura maxima")
    print("5) Humidade")

    p1 = int(input('O que deseja saber?'))
    menu = [
         "temp", "feels_like", "temp_min", "temp_max", "humidity"
    ]
    print(menu[p1-1])
    print(data['main'](menu[p1-1])
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
------------------------------------------------------------------------------------------------------