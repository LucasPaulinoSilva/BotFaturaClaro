
# **AUTOMATIZAÇÃO - EXTRAÇÃO FATURA DE INTERNET CLARO** <h1>

</br>

Neste processo foi usada a biblioteca **Selenium**, no qual é comumente utilizada para realizar automações web. <h2>

<div align="center">
<img src = "images/seleniumimage.PNG" alt="Image" height="80" width="220">
</div>


## **COMANDOS UTILIZADOS** <h3>  

</br>

- **Habilita ações de mouse**    
ActionChains(navegador)

</br>

- **Realiza o click**  
navegador.find_element(By.XPATH, '**Inserir XPATH**').click()

</br>

- **Aguarda até que um elemento apareça na página**  
WebDriverWait(navegador, **Inserir tempo limite de aguardo**).until(EC.presence_of_element_located((By.ID, "**Inserir ID**")))

</br>

- **Insere texto em um campo**  
navegador.find_element(By.XPATH,'**Inserir XPATH**').send_keys(**Inserir texto a ser escrito**)

</br>

- **Obtem texto**  
navegador.find_element(By.CSS_SELECTOR, '**Inserir elemento CSS**').get_attribute('innerHTML')

</br>

- **Realiza o click levando o cursor do mouse até o objeto**  
mouse.move_to_element(**Passar variável do caminho XPATH****).click().perform()

</br>

## **RESUMO DO PROCESSO** <h4> 

</br>

Inicialmente é realizado os cliques na tela principal do site da Claro para acessar a tela de conta de internet fixa:

<div align="center">
<img src = "images/PagePrincipal.PNG">
</div>

<div align="center">
<img src = "images/CodePagePrincipal.PNG">
</div>

</br>

Após chegar na tela de login, o usuário e a senha são inseridos:

<div align="center">
<img src = "images/TelaLogin.PNG">
</div>

<div align="center">
<img src = "images/CodeTelaLogin.PNG">
</div>

</br>

Após realizar o login o robô verifica qual é a conta da cidade de Londrina e seleciona:

<div align="center">
<img src = "images/SelecaoConta.PNG">
</div>

<div align="center">
<img src = "images/CodeSelecaoConta.PNG">
</div>

</br>

Após selecionar a conta da cidade correta, o robô verifica se irá aparecer uma janela de enquete, e caso apareça ela é fechada, e logo em seguida o clique no botão para acessar a página de download de fatura é efetuado:

<div align="center">
<img src = "images/TelaPesquisa.PNG">
</div>

<div align="center">
<img src = "images/2ViaFatura.PNG">
</div>

<div align="center">
<img src = "images/CodeAguardaJanela2Via.PNG">
</div>

</br>

Em seguida, o clique para realizar o download da fatura é feito aguardando um intervalo de 10 segundos, caso surja algum erro, o clique é feito novamente, então a conta em formato pdf é finalmente baixada:

<div align="center">
<img src = "images/DownloadFatura.PNG">
</div>

<div align="center">
<img src = "images/CodeDownloadFatura.PNG">
</div>








