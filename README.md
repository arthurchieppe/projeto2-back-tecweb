# Backend do Projeto 2 TecWeb
O projeto consite em um app que mostra as condições climáticas atuais para diversas cidades. O backend é responsável pela persistência de dados e pelas requisições Django REST. Inicialmente, a proposta era implementar um sistema de login para salvar as cidades que o usuário deseja acompanhar. Na versão final, optei por não implementar o login, de modo que o papel do backend é armazenar a lista de cidades favoritas para apenas um usuário.

O frontent é capaz de realizar requisições do tipo GET e POST para o backend.
* GET: O cliente pode requisitar ao servidor uma lista de nomes das cidades que o usuário deseja visiaulizar o tempo atual.

* POST: O usuário pode, a partir da página web, adicionar novas cidades a partir de seu nome. Ademais, o usuário também pode remover cidades que não deseja mais acompanhar. Na requisição POST, o frontend sempre vai enviar a lista completa das cidaes que o usuário est'a acompanhando, de modo que uma API de requisição DELETE não se faz necessária.
