import pytest
from lexicon_interpreter import LexiconInterpreter

def test_reserved_words():
    code = "int float double char if while for"
    lexer = LexiconInterpreter(code)
    lexer.tokenize()
    assert len(lexer.symbol_table) == 7
    for word in lexer.reserved:
        assert word in lexer.symbol_table
        assert lexer.symbol_table[word]["type"] == "reservada"

def test_identifiers():
    code = "Abc Xyz123 Test_Var"
    lexer = LexiconInterpreter(code)
    lexer.tokenize()
    assert "Abc" in lexer.symbol_table
    assert "Xyz123" in lexer.symbol_table
    assert "Test_Var" not in lexer.symbol_table  # deve falhar pois identificadores começam com maiúscula

def test_numbers():
    code = "123 456,789"
    lexer = LexiconInterpreter(code)
    lexer.tokenize()
    assert "123" in lexer.symbol_table
    assert "456,789" in lexer.symbol_table
    assert lexer.symbol_table["123"]["type"] == "número"
    assert lexer.symbol_table["456,789"]["type"] == "número"

def test_operators():
    code = "A = B + C * D / E"
    lexer = LexiconInterpreter(code)
    lexer.tokenize()
    tokens = " ".join(lexer.tokens)
    assert "=," in tokens
    assert "+," in tokens
    assert "*," in tokens
    assert "/," in tokens

def test_comments():
    code = """
    int A # esta é uma variável
    # esta linha deve ser ignorada
    float B
    """
    lexer = LexiconInterpreter(code)
    lexer.tokenize()
    assert len(lexer.tokens) == 2  # apenas duas linhas de código efetivo

def test_complex_expression():
    code = """
    int Value;
    Value = 123,456;
    while (Value < 500)
    """
    lexer = LexiconInterpreter(code)
    lexer.tokenize()
    assert "Value" in lexer.symbol_table
    assert "123,456" in lexer.symbol_table
    assert "500" in lexer.symbol_table
    assert "<," in " ".join(lexer.tokens)

def test_invalid_identifier():
    code = "abc123"  # identificador inválido (não começa com maiúscula)
    lexer = LexiconInterpreter(code)
    lexer.tokenize()
    assert "abc123" not in lexer.symbol_table

def test_symbol_table_id_increment():
    code = "int A float B char C"
    lexer = LexiconInterpreter(code)
    lexer.tokenize()
    ids = [data["id"] for data in lexer.symbol_table.values()]
    assert ids == list(range(1, len(ids) + 1))

def test_complete_output():
    code = """
int Ab;
float Exemplo
Exemplo = 3456,567
while ( Ab < 500)
"""
    lexer = LexiconInterpreter(code)
    lexer.tokenize()
    
    # Validar tabela de símbolos
    expected_table = {
        "int": {"id": 1, "type": "reservada"},
        "Ab": {"id": 2, "type": "identificador"},
        "float": {"id": 3, "type": "reservada"},
        "Exemplo": {"id": 4, "type": "identificador"},
        "3456,567": {"id": 5, "type": "número"},
        "while": {"id": 6, "type": "reservada"},
        "500": {"id": 7, "type": "número"}
    }
    
    assert lexer.symbol_table == expected_table
    
    # Validar lista de tokens
    expected_tokens = [
        "<reservada,1> <identificador,2> <;,>",
        "<reservada,3> <identificador,4>",
        "<identificador,4> <=,> <número,5>",
        "<reservada,6> <(,> <identificador,2> <<,> <número,7> <),>"
    ]
    
    assert lexer.tokens == expected_tokens
