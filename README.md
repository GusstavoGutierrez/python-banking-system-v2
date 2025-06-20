# Sistema Bancário V2 (Desafio DIO)

Este projeto é a segunda versão e uma evolução do desafio de projeto "Sistema Bancário" da plataforma **Digital Innovation One (DIO)**. O foco desta versão foi aprimorar o código através da modularização com funções, introduzindo também a gestão de usuários e contas correntes para tornar o sistema mais robusto e escalável.

## ✨ Principais Melhorias e Novas Funcionalidades

Esta versão introduz melhorias significativas em relação ao sistema original:

* **Modularização do Código:** As operações de saque, depósito e extrato foram separadas em funções dedicadas, tornando o código mais limpo e organizado.
* **Regras de Passagem de Argumentos:** Para exercitar diferentes conceitos de Python, as funções agora seguem regras específicas:
    * `deposito`: Recebe argumentos apenas por posição (`positional-only`).
    * `saque`: Recebe argumentos apenas por nome (`keyword-only`).
    * `extrato`: Recebe argumentos por posição e por nome (`positional-only` e `keyword-only`).
* **Gestão de Usuários (Clientes):**
    * Nova função para criar usuários, armazenando nome, data de nascimento, CPF e endereço.
    * O sistema impede a criação de múltiplos usuários com o mesmo CPF.
* **Gestão de Contas Correntes:**
    * Nova função para criar contas correntes, que são vinculadas a um usuário existente.
    * Cada conta possui uma agência fixa ("0001") e um número sequencial único.
    * O sistema permite que um usuário tenha múltiplas contas.
* **Estrutura de Menus Aprimorada:** A interface foi dividida em múltiplos menus para uma navegação mais intuitiva: um para gestão de usuários, outro para gestão de contas e um terceiro para as operações financeiras.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3

Não são necessárias bibliotecas externas para a execução do projeto.

## 🚀 Como Executar

1.  **Clone o Repositório (ou baixe os arquivos):**
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    cd [NOME_DA_PASTA_DO_PROJETO]
    ```

2.  **Execute o Programa Principal:**
    Com o Python 3 instalado, execute o seguinte comando no seu terminal:
    ```bash
    python main.py
    ```
    Isso iniciará o sistema no seu terminal.

## 🖱️ Como Usar a Aplicação

A aplicação agora funciona em múltiplos níveis de menus. O fluxo geral é:

1.  **Menu de Usuário:**
    * **Criar um novo usuário:** Selecione a opção `[n]` e forneça os dados solicitados (nome, CPF, etc.).
    * **Logar em um usuário:** Selecione a opção `[l]` e digite o CPF do usuário para acessar o menu de contas.

2.  **Menu de Conta (Após logar como usuário):**
    * **Criar uma nova conta:** Selecione `[c]` para criar uma nova conta vinculada ao usuário logado.
    * **Listar contas:** Selecione `[l]` para ver todas as contas do usuário logado.
    * **Logar em uma conta:** Selecione `[lc]` e digite o número da conta desejada para acessar o menu de operações.

3.  **Menu de Operações (Após logar em uma conta):**
    * **[d] Depositar:** Adiciona um valor ao saldo da conta.
    * **[s] Sacar:** Retira um valor da conta, respeitando os limites de saque e saldo.
    * **[e] Extrato:** Mostra o histórico de transações e o saldo final da conta.
    * **[v] Voltar:** Retorna ao menu anterior.

## 📂 Estrutura do Projeto

* **`main.py`:** Ponto de entrada da aplicação. Sua única responsabilidade é chamar a função principal do módulo de lógica.
* **`logica.py`:** Contém toda a lógica de negócio, as funções para as operações bancárias, a gestão de usuários/contas e a estrutura de menus que interage com o usuário.

## 📬 Contato
Se você tiver alguma dúvida sobre o projeto, sugestões ou apenas quiser se conectar, sinta-se à vontade para entrar em contato:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gustavo-vitor-gutierrez-b520a2341/) [![Instagram](https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/gustavo.gutierreez/) [![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/+5511952018042)