# LexiconInterpreter - Analisador Léxico Simples

Este é um analisador léxico escrito em Python que identifica tokens em um código-fonte fictício. Ele reconhece identificadores, números, operadores, delimitadores e palavras reservadas, além de armazenar as informações em uma tabela de símbolos.

Esse foi um projeto desenvolvido para fins educacionais, na aula de compiladores, com o objetivo de entender os conceitos básicos de análise léxica e a construção de um analisador simples.

## Funcionalidades
- **Identificação de tokens**: Reconhece palavras reservadas, identificadores, números, operadores e delimitadores.
- **Tabela de símbolos**: Mantém uma tabela de símbolos ordenada com IDs e tipos associados.
- **Impressão formatada**: Exibe a tabela de símbolos e a lista de tokens válidos de forma organizada.

## Tecnologias Utilizadas
- `Python 3.10`
- `re` para expressões regulares.
- `tabulate` para exibição formatada de tabelas.
- `collections.OrderedDict` para armazenar a tabela de símbolos mantendo a ordem de inserção.

## Instalação e Execução
### 1. Clonar o Repositório
```sh
 git clone https://github.com/seu-usuario/LexiconInterpreter.git
 cd LexiconInterpreter
```
### 2. Criar um Ambiente Virtual
```sh
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```
### 3. Instalar as Dependências
```sh
pip install -r requirements.txt
```
### 4. Executar o Código
```sh
python lexicon_interpreter.py
```

## Exemplo de Uso
```python
code = """
int Ab;
# int Xb poderia 

doble teste
   float Exemplo # sera minha variavel de exemplo
# double Exemplo2 seria melhor?

   Exemplo = 3456,567

while ( Ab < 500)
"""

lexer = LexiconInterpreter(code)
lexer.tokenize()
lexer.show_symbol_table()
lexer.show_tokens()
```

Saída esperada:
```
+-----------+----------+---------------+
|   Entrada | Valor    | Tipo          |
+===========+==========+===============+
|         1 | int      | reservada     |
+-----------+----------+---------------+
|         2 | Ab       | identificador |
+-----------+----------+---------------+
|         3 | float    | reservada     |
+-----------+----------+---------------+
|         4 | Exemplo  | identificador |
+-----------+----------+---------------+
|         5 | 3456,567 | número        |
+-----------+----------+---------------+
|         6 | while    | reservada     |
+-----------+----------+---------------+
|         7 | 500      | número        |
+-----------+----------+---------------+

Lista de tokens válidos:
<reservada,1> <identificador,2> <;,>
<reservada,3> <identificador,4>
<identificador,4> <=,> <número,5>
<reservada,6> <(,> <identificador,2> <<,> <número,5> <),>
```

## Melhorias Futuras
- Suporte a mais tipos de tokens (strings, booleanos, etc.).
- Implementação de análise sintática.
- Suporte a mais estruturas de controle.
- Melhorias na exibição dos tokens.

## Licença
Este projeto é distribuído sob a licença MIT.
