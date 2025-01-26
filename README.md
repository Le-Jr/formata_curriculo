# MVP de Gerador de Currículos

Este projeto é um MVP (Produto Mínimo Viável) para gerar currículos formatados a partir de informações fornecidas pelo usuário. Ele permite que o usuário insira dados como nome e e-mail e, a partir dessas informações, crie um currículo em formato PDF utilizando um template LaTeX. O aplicativo também oferece a opção de remover uma marca d'água do currículo gerado por meio de um upgrade pago.

## Funcionalidades

- **Cadastro de Currículos**: O usuário pode criar um currículo simples com nome e e-mail.
- **Geração de PDF**: O currículo gerado é exportado para PDF utilizando LaTeX.
- **Upgrade Pago**: O usuário pode optar por remover a marca d'água do currículo e obter benefícios extras, como suporte prioritário e exportação avançada.

## Tecnologias Utilizadas

- **Flask**: Framework web utilizado para criar a aplicação.
- **PyMongo**: Biblioteca para integrar o MongoDB com o Flask, usada para armazenar os dados do currículo.
- **LaTeX**: Usado para gerar o PDF formatado do currículo.

## Estrutura de Diretórios

A estrutura do projeto é organizada da seguinte forma:

```
project-directory/
│
├── app/
│   ├── templates/          # Templates HTML (index.html, success.html)
│   ├── static/             # Arquivos estáticos (CSS, JS)
│   ├── routes.py           # Roteamento e lógicas de controle
│   ├── __init__.py         # Inicialização da aplicação Flask
│
├── latex_templates/        # Templates LaTeX para o currículo
│   ├── base_template.tex   # Template base para formatação do PDF
│
├── instance/               # Armazenamento de PDFs gerados
│   ├── generated_pdfs/     # PDFs gerados dinamicamente
│
├── config.py               # Arquivo de configurações da aplicação
├── run.py                  # Arquivo para rodar o servidor
├── requirements.txt        # Dependências do projeto
├── README.md               # Este arquivo
```

### 2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
```

### 3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### 4. Inicialize o MongoDB e certifique-se de que ele está rodando localmente (na porta 27017 por padrão).

### 5. Inicie o servidor Flask:

```bash
python run.py
```

### 6. Acesse a aplicação no navegador:

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Funcionalidade de Geração de Currículo

Na página inicial, o usuário pode preencher um formulário simples com o nome e e-mail.  
Ao submeter o formulário, o sistema gera um currículo simples, com um **ID único**, que pode ser baixado em PDF.

---

## Estratégia de Lançamento e Monetização

- **Versão Gratuita**: Geração de um único template de currículo com marca d'água.
- **Upgrade Pago (R$ 9,90)**: Remoção da marca d'água, suporte prioritário e exportação avançada (como PDFs personalizados ou funcionalidades adicionais).
- **Promoção de Lançamento**: Os primeiros **100 usuários** terão o upgrade gratuito como incentivo.

---

## Contribuindo

Se você quiser contribuir para este projeto, fique à vontade para abrir uma issue ou enviar um pull request.

### Passos para Contribuição

1. Faça o fork deste repositório.
2. Crie uma branch para suas modificações:
   ```bash
   git checkout -b feature/novas-funcionalidades
   ```
3. Realize as alterações e commit com uma mensagem clara.
4. Envie o seu pull request.

## Licença

Este projeto está licenciado sob a **Licença MIT**.  
Para mais detalhes, veja o arquivo [LICENSE](LICENSE).
