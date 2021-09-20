# MiBand_automationTool 🏡⌚

<strong> Este projeto tem como objetivo realizar pequenas automações voltadas ao conceito de "Smart Home" utilizando a Smart Band Mi Band.</strong>

### Como funciona?

A aplicação consiste na elaboração de um servidor em Flask, que envia comandos ao computador com base no Webhook ativado. Para que seja posśivel ativar os Webhooks
diretamente da Mi Band, é necessário o uso do app (para Android) "Notify for Mi Band". 

Com o app instalado, é necessário mapear os botões da Mi Band para a função de HTTP Request (método GET) utilizando a URL com o seguinte exemplo `IP_DA_MAQUINA:PORTA/COMANDO_DESEJADO`.
Assim, quando a ação for realizada, o comando configurado em `app.py` será executado.

Caso ache desconfortável a necessidade do computador para rodar o script, você pode instalar o servidor no seu Smartphone utilizando o Termux (emulador de terminal para Android) juntamente
com outro app de automação, como Macrodroid ou Automate, por exemplo.

### Sinta-se a vontade para modificar como quiser
 
Para meu uso pessoal, me senti mais confortável em utilizar o programa juntament com shell-scripts, mas você pode executar os comandos diretamente pelo script em Python.
Portanto, estes shell-scripts são opcionais e você deve modificar o `app.py` de forma que seja mais coerente para o seu uso e para o sistema operacional que está usando.

No meu caso, a automação foi feita no Ubuntu 20.04 LTS. 
