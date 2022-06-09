# Importa bibliotecas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import secrets

# Aciona webdriver
s = Service(executable_path=r"C:\Users\****\Desktop\Python\BotFaturaClaro\chromedriver.exe")
navegador = webdriver.Chrome(service=s)
# Maximiza janela do site
navegador.maximize_window()
# Abre navegador no site da Claro
navegador.get("https://www.claro.com.br/atendimento/2-via-de-conta")
# Habilita ações de mouse
mouse = ActionChains(navegador)

################################################## INICIO #####################################################

# Clica no botão "Minha Claro"
navegador.find_element(By.XPATH, '//*[@id="cms-Header"]/div/div/nav/div[2]/ul/li[3]/div/button').click()
# Clica no botão "Minha Claro Residencial"
navegador.find_element(By.XPATH,'//*[@id="cms-Header"]/div[2]/div/nav/div[2]/ul/li[3]/div[2]/div/ul/li/div/ul/li[2]/a/p').click()

############################################## MUDANÇA DE JANELA ##############################################

# Aguarda até que a janela de login esteja visivel 
wait_tela_login = WebDriverWait(navegador, 30).until(EC.presence_of_element_located(By.ID, "labelLogin"))

# Digita o CPF da conta
navegador.find_element(By.XPATH,'//*[@id="login"]').send_keys(secrets.cpf)
# Digita a senha da conta
navegador.find_element(By.XPATH,'//*[@id="password"]').send_keys(secrets.senha)
# Clica no botão "Acessar"
navegador.find_element(By.XPATH,'//*[@id="loginForm"]/fieldset/div[5]/button[1]').click()

############################################## MUDANÇA DE JANELA ##############################################

# Aguarda até que a conta da cidade de Londrina esteja visivel 
wait_conta_londrina = WebDriverWait(navegador, 30).until(EC.presence_of_element_located((By.ID, "mcr-list-radio-001575173")))

# Verifica se a conta de Londrina está na primeira ou na segunda posição para selecionar
conta_1 = navegador.find_element(By.CSS_SELECTOR, '#app > article > div > div.mcr-contentColumn.mdn-Col-xs-12.mdn-Col-lg > div > div.mcr-select-contract-list-scroller > div:nth-child(1) > div > div > label.mdn-Radio-text.mcr-select-contract-list-items-radio-infos > p.mdn-Text.address').get_attribute('innerHTML')
if conta_1 == "Rua****, n° da residência***, Londrina - Pr":
    conta_londrina = navegador.find_element(By.XPATH,'//*[@id="mcr-list-radio-374246885"]')
    mouse.move_to_element(conta_londrina).click().perform()
else:
    conta_londrina = navegador.find_element(By.XPATH,'//*[@id="mcr-list-radio-001575173"]')
    mouse.move_to_element(conta_londrina).click().perform()

# Clica no botão "Continuar"
botao_continuar = navegador.find_element(By.XPATH,'//*[@id="app"]/article/div/div[2]/div/div[3]/button')
mouse.move_to_element(botao_continuar).click().perform()

# Caso a "Janela de pesquisa" exista, ela é fechada
try:
 campo_pesquisa = WebDriverWait(navegador, 30).until(EC.presence_of_element_located((By.ID, "dont-accept-912461b7-b4fe-4b1c-be33-4b6298b8bda8")))
 navegador.find_element(By.XPATH,'//*[@id="consentimento-lgpd"]/div/div/div[1]/button').click()
 navegador.find_element(By.XPATH,'//*[@id="consentimento-lgpd"]/div/div/div[1]/button').click()
finally:
 print("Campo pesquisa não existe")

# Clica no botão "2° via de fatura"
_2_via_fatura = navegador.find_element(By.XPATH,'/html/body/main/div[1]/section/div[1]/div[2]/div[2]/div[2]/div[2]')
mouse.move_to_element(_2_via_fatura).click().perform()

############################################## MUDANÇA DE JANELA ##############################################

# Tenta clicar no botão "Fazer Download da fatura", caso haja algum erro, o clique é realizdo novamente
try:
 sleep(10)
 gerar_2_via = navegador.find_element(By.XPATH,'//*[@id="app-wrapper"]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/a[2]/p')
 mouse.move_to_element(gerar_2_via).click().perform()
except:
 sleep(10)
 gerar_2_via = navegador.find_element(By.XPATH,'//*[@id="app-wrapper"]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/a[2]/p')
 mouse.move_to_element(gerar_2_via).click().perform()



