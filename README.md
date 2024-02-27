Olá, espero que estejam todos bem :D

Esse projeto web tem por função realizar o cadastro de produtos usando 4 dados pra isso, ID, Nome, Descrição, Preço;

Para a execução deste projeto, você vai precisar ter em sua máquina os seguintes quesitos;

- IDE VS code;
- Python 3.11.8 (Linguagem de Programação);
- Flask 3.0.2 (Framework);
- Werkzeug 3.0.1 (biblioteca para desenvolvimento de apps WSGI);
- Extensões python, sql, mysql instaladas no seu VSCode;
- pymysql (Biblioteca pythom para conexão com banco).

Para instalar o vscode, você deve baixar o .exe e executa-lo - (https://code.visualstudio.com/download);

Para fazer a instalação do python basta encontrar na web o site oficial do python(https://www.python.org/downloads/), baixar a versão usada ou uma versão superior e executar o .exe, para ter certeza que a instalação foi bem sucedida, basta abrir o terminal e digitar "python --version", irá mostrar a versão instalada;

Agora vamos abrir o VScode;

Instalado o python, passamos a ter acesso ao gerenciador de contexto pip, e atravez dele, poderemos instalar o flask e o pymysql, atravez dos comandos "pip intall flask" e "pip install pymysql", no próprio terminal do vscode, podemos digitar o comando flask --version, que este nos vai trazer a versão do flask instalada, do pymysql e do Werzeug(esse vem junto da instalação do flask, não precisa instalar separado);

_______________________________________________
Vamos falar agora sobre a estrutura do projeto

- Para armazenamento dos dados foi usado o banco de dados mysql, onde no projeto existe um arquivo chamado de "connection_db.py" que repassa os dados e faz a conexão com o banco, posteriormente, os códigos em sql contidos no arquivo "db.sql", a conexão e feita usando a biblioteca pymysql;

- Foi criado um arquivo chamado de "routes.py" para a definição das rotas em HTML as quais o sistema vai rodar;

- O arquivo "app.py" e responsável pelo cadastro das url's onde estão a execusão das funções dentro do sistema;

- O arquivo "controller.py" faz a criação das classes e funções que posteriormente são chamadas para inserir, deletar, ler ou criar um cadastro de um produto;

- No arquivo "erros.py", faz a tratativa em casa da pag não estar disponível;

- Foi disponibilizado um arquivo "api.py", com as rotas para que possa ser usado posteriormente em casa da implementação de um front-end;

- O arquivo "main.py" faz o start da aplicação web;

- Coloquei duas imagens da criação do banco e da tabela no banco mysql;

- Todo o sistema foi desenvolvido em um ambiente virtual tipo virtual venv-venv;

- Existe uma pasta chamada de "static" nela pode ser colocado as imagens, arquivos .js que venham a ser usados no projeto front-end;

- Na pasta "Templates" temos todos os arquivos tipo .html, em uma pasta de nome "public" temos "index.html", "read.html", "update.html", e fora dela temos o index.html, esses arquivos são responsáveis pela criação da pag web para cadastro dos produtos;



Bom acredito que fechamos aqui, se eu não esqueci de nada a estrutura e essa.

Obrigado!!!

PS: não consegui fazer o projeto rodar de pois da implementação do banco, tenho um erro do codigo sql do banco, que apesar de rodar diretamente no mysql workbench, não rodou no projeto, coloquei duas imagens com a validação da criação do banco e das tabelas.
