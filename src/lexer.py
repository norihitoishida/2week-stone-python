import re
from stone.token.token import BaseToken, IdentifierToken, NumberToken, StringToken


class Lexer:
    """字句解析器"""

    def __init__(self, source_code_path: str):
        self.source_code_path = source_code_path
        (
            self.comment_pattern,
            self.number_literal_pattern,
            self.string_literal_pattern,
            self.identifier_pattern,
        ) = self.compile_regex_pattern()  # 正規表現パターン
        self.temp_queue = self.read_source_code()  # ソースコード(1行ずつ)
        self.tokens_list = []
        self.read_tokens()

    def read_source_code(self) -> list:
        """ソースコードを読んで1行ずつ`self.temp_queue`に格納する"""
        with open(self.source_code_path, "r", encoding="utf-8") as f:
            temp_queue = f.readlines()
        return temp_queue

    def compile_regex_pattern(self):
        _blank = r"\s*"
        _comment = "#.*"
        _number_literal = "[0-9]+"
        _string_literal = '".*"'
        _identifier = r"[a-zA-Z_][a-zA-Z0-9_]*|==|<=|>=|&&|\|\||!|\"|$|%|&|'|\(|\)|\*|\+|,|-|\.|/|:|;|<|=|>|\?|@|\[|\\|\]|\^|\_|`|{|\||}|~"

        comment_pattern = re.compile(rf"{_blank}({_comment})")
        number_literal_pattern = re.compile(rf"{_blank}({_number_literal})")
        string_literal_pattern = re.compile(rf"{_blank}({_string_literal})")
        identifier_pattern = re.compile(rf"{_blank}({_identifier})")

        return (
            comment_pattern,
            number_literal_pattern,
            string_literal_pattern,
            identifier_pattern,
        )

    def read_tokens(self) -> None:
        for _linenum, _line in enumerate(self.temp_queue):
            while True:    
                if self.comment_pattern.match(string=_line):
                    break
                elif _line=="\n":
                    self.tokens_list.append(BaseToken.EOL)
                    break
                elif self.number_literal_pattern.match(string=_line):
                    m = self.number_literal_pattern.match(string=_line)
                    _value = int(str(m.group(0)).strip())
                    self.tokens_list.append(NumberToken(line=_linenum, value=_value))
                    _line = _line[len(str(m.group(0))):]
                    if len(_line)==0:
                        break
                elif self.string_literal_pattern.match(string=_line):
                    m = self.string_literal_pattern.match(string=_line)
                    _text = str(m.group(0)).strip()
                    self.tokens_list.append(StringToken(line=_linenum, text=_text))
                    _line = _line[len(str(m.group(0))):]
                    if len(_line)==0:
                        break
                elif self.identifier_pattern.match(string=_line):
                    m = self.identifier_pattern.match(string=_line)
                    _identifier = str(m.group(0)).strip()
                    self.tokens_list.append(IdentifierToken(line=_linenum, identifier=_identifier))
                    _line = _line[len(str(m.group(0))):]
                    if len(_line)==0:
                        break
                else:
                    if len(_line)==0:
                        break
                
        self.tokens_list.append(BaseToken.EOF)
        return None


lexer = Lexer(source_code_path="stone/sample.stone")
for token in lexer.tokens_list:
    if not isinstance(token, str):
        print(token.get_text())
    else:
        print(token)


