"""import re

blank = r"\s*"
comment = "#.*"
number_literal = "[0-9]+"
string_literal = '".*"'
identifier = r"[a-zA-Z_][a-zA-Z0-9_]*|==|<=|>=|&&|\|\||!|\"|$|%|&|'|\(|\)|\*|\+|,|-|\.|/|:|;|<|=|>|\?|@|\[|\\|\]|\^|_|`|{|\||}|~"

comment_pattern = re.compile(rf"{blank}({comment})")
number_literal_pattern = re.compile(rf"{blank}({number_literal})")
string_literal_pattern = re.compile(rf"{blank}({string_literal})")
identifier_pattern = re.compile(rf"{blank}({identifier})")

s = ""
if comment_pattern.match(string=s):
    print("comment_pattern")
    print(comment_pattern.match(string=s).group(0))
elif number_literal_pattern.match(string=s):
    print("number_literal_pattern")
    print(number_literal_pattern.match(string=s).group(0))
elif string_literal_pattern.match(string=s):
    print("string_literal_pattern")
elif identifier_pattern.match(string=s):
    print("identifier_pattern")
    print(identifier_pattern.match(string=s).group(0))
else:
    print("naaaaaaa")
"""

s = "123 "
print(int(s.strip()))