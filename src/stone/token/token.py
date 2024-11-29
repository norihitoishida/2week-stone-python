from abc import ABC, abstractmethod


class BaseToken(ABC):
    """
    - 字句解析の結果取り出されたトークンの抽象クラス
    - トークンは 識別子 or 整数リテラル or 文字列リテラル
    """

    # クラス変数として定義
    EOF = "EOF"  # ファイル終端
    EOL = "\n"  # 行末

    def __init__(self, line: int):
        """
        :param int line: トークンの位置の行番号
        """
        self._line_number = line

    @abstractmethod
    def get_line_number(self) -> int:
        """トークンの位置の行番号を取得"""
        return self._line_number

    @abstractmethod
    def is_identifier(self) -> bool:
        """識別子トークンかどうか"""
        ...

    @abstractmethod
    def is_number_literal(self) -> bool:
        """整数リテラルトークンかどうか"""
        ...

    @abstractmethod
    def is_string_literal(self) -> bool:
        """文字列リテラルトークンかどうか"""
        ...

    @abstractmethod
    def get_number(self) -> int:
        """整数リテラルを整数(int)として返す"""
        ...

    @abstractmethod
    def get_text(self) -> str:
        """識別子トークン/整数リテラル/文字列リテラルを文字列(str)として返す"""
        ...


class IdentifierToken(BaseToken):
    def __init__(self, line: int, identifier: str):
        """
        :param int line: トークンの位置の行番号
        """
        self._line_number = line
        self._identifier = identifier

    def get_line_number(self) -> int:
        """トークンの位置の行番号を取得"""
        return self._line_number

    def is_identifier(self) -> bool:
        """識別子トークンかどうか"""
        return True

    def is_number_literal(self) -> bool:
        """整数リテラルトークンかどうか"""
        return False

    def is_string_literal(self) -> bool:
        """文字列リテラルトークンかどうか"""
        return False

    def get_number(self) -> int:
        """整数リテラルを整数(int)として返す"""
        # TODO: エラー実装
        ...

    def get_text(self) -> str:
        """識別子トークンを文字列(str)として返す"""
        return str(self._identifier)


class NumberToken(BaseToken):
    def __init__(self, line: int, value: int):
        """
        :param int line: トークンの位置の行番号
        """
        self._line_number = line
        self._value = value

    def get_line_number(self) -> int:
        """トークンの位置の行番号を取得"""
        return self._line_number

    def is_identifier(self) -> bool:
        """識別子トークンかどうか"""
        return False

    def is_number_literal(self) -> bool:
        """整数リテラルトークンかどうか"""
        return True

    def is_string_literal(self) -> bool:
        """文字列リテラルトークンかどうか"""
        return False

    def get_number(self) -> int:
        """整数リテラルを整数(int)として返す"""
        return int(self._value)

    def get_text(self) -> str:
        """整数リテラルを文字列(str)として返す"""
        return str(self._value)


class StringToken(BaseToken):
    def __init__(self, line: int, text: str):
        """
        :param int line: トークンの位置の行番号
        """
        self._line_number = line
        self._text = text

    def get_line_number(self) -> int:
        """トークンの位置の行番号を取得"""
        return self._line_number

    def is_identifier(self) -> bool:
        """識別子トークンかどうか"""
        return False

    def is_number_literal(self) -> bool:
        """整数リテラルトークンかどうか"""
        return False

    def is_string_literal(self) -> bool:
        """文字列リテラルトークンかどうか"""
        return True

    def get_number(self) -> int:
        """整数リテラルを整数(int)として返す"""
        # TODO: エラー実装
        ...

    def get_text(self) -> str:
        """識別子トークン/整数リテラル/文字列リテラルを文字列(str)として返す"""
        return str(self._text)
