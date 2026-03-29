# Automacao de Cadastro de Produtos com Python

Projeto de automacao desktop com Python para acessar uma pagina web, realizar login automaticamente e cadastrar produtos em lote a partir de uma planilha `.csv`.

## Visao geral

Este projeto foi criado para automatizar um fluxo repetitivo de cadastro de produtos usando:

- `PyAutoGUI` para controlar mouse e teclado
- `pandas` para ler a base de dados
- `python-dotenv` para proteger credenciais e configuracoes locais

O script abre o Google Chrome no macOS, acessa a pagina de login, entra no sistema e preenche o formulario de cadastro com os dados de `produtos.csv`.

## Funcionalidades

- Login automatizado no sistema
- Leitura de produtos em lote via CSV
- Preenchimento automatico do formulario
- Suporte a observacoes opcionais
- Configuracao de coordenadas via `.env`
- Estrutura pronta para publicar no GitHub sem expor senha

## Estrutura do projeto

```text
.
├── codigo.py
├── pegar_posicao.py
├── produtos.csv
├── tabela.py
├── requirements.txt
├── .env.example
└── README.md
```

## Tecnologias

- Python 3
- PyAutoGUI
- pandas
- python-dotenv

## Como executar

### 1. Clone o repositorio

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd "AUTOMAÇAO PYTHON"
```

### 2. Crie e ative um ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependencias

```bash
pip install -r requirements.txt
```

### 4. Configure as variaveis locais

Crie o arquivo `.env` com base no exemplo:

```bash
cp .env.example .env
```

Depois edite o `.env` com:

```env
AUTOMACAO_EMAIL=seu_email@exemplo.com
AUTOMACAO_SENHA=sua_senha_aqui
CAMPO_EMAIL_X=564
CAMPO_EMAIL_Y=401
BOTAO_LOGIN_X=727
BOTAO_LOGIN_Y=568
CAMPO_FORM_X=534
CAMPO_FORM_Y=290
SCROLL_APOS_CADASTRO=5000
```

## Como descobrir as coordenadas da tela

Use o arquivo `pegar_posicao.py` para capturar a posicao do mouse:

```bash
python3 pegar_posicao.py
```

Voce tera alguns segundos para posicionar o mouse sobre o elemento desejado. O script imprimira as coordenadas no terminal.

## Como rodar a automacao

```bash
python3 codigo.py
```

## Formato do arquivo CSV

O arquivo `produtos.csv` deve conter as seguintes colunas:

```text
codigo | marca | tipo | categoria | preco_unitario | custo | obs
```

Exemplo:

```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
MOLO000251,Logitech,Mouse,1,25.95,6.50,
CAHA000252,Hashtag,Camisa,2,25.00,11.00,Conferir estoque
```

Observacao: o arquivo atual do projeto esta separado por tabulacao, e o script ja trata isso com `sep="\t"`.

## Cuidados importantes

- Este projeto depende de coordenadas da tela, entao pequenas mudancas na resolucao ou no zoom podem exigir ajuste.
- Evite usar o computador durante a execucao da automacao.
- O script foi preparado para macOS por usar `open -a 'Google Chrome'`.
- O arquivo `.env` esta no `.gitignore`, entao suas credenciais nao serao enviadas ao GitHub.

## Proximos passos para evoluir o projeto

- Trocar coordenadas fixas por reconhecimento de imagem
- Adicionar logs de execucao
- Validar dados antes do envio
- Criar tratamento de erros por etapa

## Autor

Desenvolvido por Matheus, com foco em automacao de tarefas repetitivas usando Python.
