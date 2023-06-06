# Lib
Sistema de Biblioteca Online em Django:  O projeto consiste em um sistema de biblioteca online desenvolvido usando o framework Django. O objetivo principal é fornecer uma plataforma para os usuários, onde eles possam cadastrar livros, verificar se os livros estão emprestados e realizar login para acessar

Recursos Principais:

1-Autenticação de Usuários: O sistema permite que os usuários se cadastrem, façam login e gerenciem suas contas. Cada usuário tem um perfil individual que contém suas informações pessoais e histórico de empréstimos.

2-Cadastro de Livros: Os usuários autenticados têm a capacidade de cadastrar novos livros no sistema. Os detalhes do livro, como título, autor, editora, ISBN e descrição, podem ser inseridos. Essas informações serão armazenadas no banco de dados para acesso posterior.

3-Verificação de Disponibilidade: O sistema fornece uma função para verificar se um livro está disponível ou emprestado. Os usuários podem pesquisar pelo título do livro e obter informações sobre a disponibilidade do livro, como a data de empréstimo atual, se o livro está emprestado a outro usuário.

4-Empréstimo e Devolução de Livros: Usuários autenticados podem solicitar empréstimos de livros disponíveis. Uma vez que um livro seja emprestado, a data de empréstimo é registrada e o livro é marcado como indisponível para outros usuários. Da mesma forma, quando o livro é devolvido, a data de devolução é registrada e o livro fica disponível novamente.

5-Histórico de Empréstimos: Os usuários podem acessar seu histórico de empréstimos, que exibe os livros que eles já pegaram emprestados e as datas correspondentes de empréstimo e devolução.

6-Interface de Usuário Intuitiva: O sistema possui uma interface de usuário amigável e intuitiva, onde os usuários podem navegar facilmente, pesquisar livros, visualizar informações e interagir com as funcionalidades do sistema.

7-Controle de Acesso: O sistema implementa medidas de controle de acesso para garantir que apenas usuários autenticados tenham permissão para cadastrar livros, fazer empréstimos e visualizar informações sensíveis. O login é necessário para acessar a maioria dos recursos do sistema.

O projeto é desenvolvido em Django, um framework Python poderoso e versátil para desenvolvimento web. O banco de dados é utilizado para armazenar informações sobre usuários, livros e empréstimos. Além disso, bibliotecas adicionais do Django podem ser usadas para implementar recursos como autenticação de usuário e pesquisa eficiente.
Com este sistema de biblioteca online, os usuários podem facilmente gerenciar suas atividades de empréstimo de livros, verificar a disponibilidade de livros desejados e desfrutar de uma experiência de usuário conveniente e intuitiva.
