import re
from tabulate import tabulate
from collections import OrderedDict

class LexiconInterpreter:
    def __init__(self, code):
        self.code_lines = code.split("\n")
        self.symbol_table = OrderedDict()
        self.tokens = []
        self.next_id = 1
        self.reserved = {"int", "double", "char", "float", "if", "while", "for"}
        self.token_types = {
            "RESERVED": "reservada",
            "IDENTIFIER": "identificador",
            "NUMBER": "número",
        }

    def get_symbol_id(self, value):
        if value not in self.symbol_table:
            self.symbol_table[value] = {"id": self.next_id, "type": None}
            self.next_id += 1
        return self.symbol_table[value]["id"]

    def tokenize(self):
        token_specs = [
            ("RESERVED", r"\b(int|double|char|float|if|while|for)\b"),
            ("IDENTIFIER", r"\b[A-Z][A-Za-z0-9]*\b"),  # Removido o underscore da expressão regular
            ("NUMBER", r"\b\d+(?:,\d+)?\b"),
            ("OPERATOR", r"[+\-*/=<>]"),
            ("DELIMITER", r"[;{}(),]"),
            ("COMMENT", r"#.*")
        ]
        token_regex = "|".join(f"(?P<{name}>{pattern})" for name, pattern in token_specs)

        for line in self.code_lines:
            tokens_line = []
            for match in re.finditer(token_regex, line):
                kind = match.lastgroup
                value = match.group()

                if kind == "COMMENT":
                    continue

                if kind in self.token_types:
                    symbol_id = self.get_symbol_id(value)
                    symbol_type = self.token_types[kind]
                    self.symbol_table[value]["type"] = symbol_type
                    tokens_line.append(f"<{symbol_type},{symbol_id}>")
                else:
                    tokens_line.append(f"<{value},>")

            if tokens_line:
                self.tokens.append(" ".join(tokens_line))

    def show_symbol_table(self):
        table = [[data["id"], value, data["type"] or "desconhecido"] for value, data in self.symbol_table.items()]
        headers = ["Entrada", "Valor", "Tipo"]
        print(tabulate(table, headers, tablefmt="grid"))

    def show_tokens(self):
        print("\nLista de tokens válidos:")
        print("\n".join(self.tokens))


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
