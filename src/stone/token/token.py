from abc import ABC, abstractmethod

class BaseToken(ABC):
    """
    - 字句解析の結果取り出されたトークンの抽象クラス
    - トークンは 識別子 or 整数リテラル or 文字列リテラル
    """

    # クラス変数として定義する
    EOF = "EOF" # ファイル終端
    EOL = "\n"  # 行末
    

    def __init__(self, line: int):
        """
        :param int line: トークンの位置の行番号
        """
        self._line_number = line
        
    def get_line_number(self) -> int:
        """トークンの位置の行番号を取得"""
        return self._line_number

    @abstractmethod
    def is_identifier(self) -> bool:
        """識別子トークンかどうか"""
        ...

    @abstractmethod
    def is_number(self) -> bool:
        """整数リテラルトークンかどうか"""
        ...

    @abstractmethod
    def is_string(self) -> bool:
        """文字列リテラルトークンかどうか"""
        ...

    @abstractmethod
    def get_number(self) -> int:
        """整数リテラルを整数(int)として返す"""
        ...

    @abstractmethod
    def get_text(self) -> str:
        """文字列リテラルを文字列(str)として返す"""
        ...


class IdentifierToken(BaseToken):
    pass

class NumberToken(BaseToken):
    pass

class StringToken(BaseToken):
    pass
