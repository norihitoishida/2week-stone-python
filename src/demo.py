from lexer import Lexer
import queue
import re

#l = Lexer(source_code_path="stone/sample.stone")
#print(l.temp_queue)

blank = r"\s*" 
comment = "#.*"
number_literal = "[0-9]+"
string_literal = '".*"'
identifier = r"[a-zA-Z_][a-zA-Z0-9_]*|==|<=|>=|&&|\|\||!|\"|$|%|&|'|\(|\)|\*|\+|,|-|\.|/|:|;|<|=|>|\?|@|\[|\\|\]|\^|_|`|{|\||}|~"

pattern = re.compile(rf'{blank}(({comment})|({number_literal})|({string_literal})|({identifier}))?')

s = "while i < 10 {"
print(pattern.match(string=s))

