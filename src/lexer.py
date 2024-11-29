import re
from stone.token.token import BaseToken, IdentifierToken, NumberToken, StringToken

class Lexer:
    """字句解析器"""

    def __init__(self, source_code_path: str):
        self.source_code_path = source_code_path
        self.pattern = self.regex_pattern_compile() # 正規表現パターン
        self.temp_queue = self.read_source_code() # ソースコード(1行ずつ)
        self.tokens_list = []
    
    def read_source_code(self) -> list:
        """ソースコードを読んで1行ずつ`self.temp_queue`に格納する
        """
        with open(self.source_code_path, "r", encoding="utf-8") as f:
            temp_queue = f.readlines()
        return temp_queue

    def regex_pattern_compile(self):
        _blank = r"\s*" 
        _comment = "#.*"
        _number_literal = "[0-9]+"
        _string_literal = '".*"'
        _identifier = r"[a-zA-Z_][a-zA-Z0-9_]*|==|<=|>=|&&|\|\||!|\"|$|%|&|'|\(|\)|\*|\+|,|-|\.|/|:|;|<|=|>|\?|@|\[|\\|\]|\^|_|`|{|\||}|~"
        pattern = re.compile(rf'{_blank}(({_comment})|({_number_literal})|({_string_literal})|({_identifier}))?')
        return pattern

    def read_tokens(self, lines: list[str, int]):
        return None
