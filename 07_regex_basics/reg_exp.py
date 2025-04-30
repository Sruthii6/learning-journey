import re
"""
s ='abcdef abcxyz'
print(s)
s1= s.replace('abc', '*')
print(s1)

# regular expression
s2 = re.sub(r'abc', '*',s)
print(s2)

# to replace specificletters
s3 = re.sub(r'[ad]', '*', s)
print(s3)

S = 'a1 + b2 + c5 + x2'
print(S)
s4 = re.sub(r'[abc][123]', '*', S)
print(s4)

"""




"""
#[A-Z] any capital letter
#[0-9] or \d any digit
#[A-Za-z0-9] any letter or digit


# matching almost any character using dot
S1 = 'A2B AxB AxxB A$B'
print(S1)
s5 = re.sub(r'A.B', '*', S1)
print("matching any char:",s5)

# matching multiple copies
s='ABC ABBBBBBC ACBBB'
print(s)
print("matching multiple copies")
s6 = re.sub(r'AB+', '*', s)
print(s6)

"""









"""

# + match 1 or more occurrences
# * match 0 or more occurrences
# ? match 0 or 1 occurrence
# {m} match exactly m occurrences
# {m,n} match between m and n occurrences, inclusive

S2 ='ABB ABBB ABBBB ABBBBBBBBB'
print("the string to be replaced",S2)
s7 = re.sub(r'AB{3,6}', '*', S2)
print(s7)

s8 = re.sub(r'AB{3,6}?', '*', S2) # fewer replacement
print(s8)

s9 = re.sub(r'AB *?', '*', S2) # 0 or 1 occurence  +?, *?, ?? can be used
print(s9)




"""



"""



# anything to be replaced using or character
S3 ='abcdefxyz123abc'
print("the original string",S3)
s = re.sub(r'abc|xyz', '*',S3)
print(s)

s1 = re.sub('^abc', '*', S3)
print("match at beg",s1)
s2 = re.sub('xyz$', '*', S3)
print("match at end",s2)

# matching special characters
s3 = re.sub(r'AB\+', '*', 'AB+C')    # if not raw string AB\\+
print(s3)

"""











"""
# digit \d and non-digit \D
s4 = re.sub(r'\d', '*', '3 + 14 = 17')
print("digit replace",s4)

s5 = re.sub(r'\D', '*', '3 + 14 = 17')
print("non-digit",s5)


# \w number or letter and \W otherwise
S = 'This is a test. Or is it?'
print(S)
s1 = re.sub(r'\w', '*', S)
print("no or letter replace",s1)

s2 = re.sub(r'\W', '*', S)
print("anything replace",s2)

# \s matches whitespace, and \S matches non-whitespace
s3 = re.sub(r'\s', '*', S)
print("space replace",s3)
s4 = re.sub(r'\S', '*', S)
print(" not space", s4)
"""
"""


# preceding and following matches

#(?=) matches only if followed by
#(?!) matches only if not followed by
#(?<=) matches only if preceded by
#(?<!) matches only if not preceded by

S = 'The dog and the cat is on the wall.'
print("the string",S)
s1 = re.sub(r'the(?= cat)', '*', S)
print(" cat preceded by the",s1)

s2 = re.sub(r'(?<= )the', '*', S)
print("the preceded by space",s2)

s3 = re.sub(r'(?<!\w)[Tt]he(?!\w)', '*',S)
print(" separate the",s3)

s4 = re.sub('(?i)ab', '*', 'ab AB') # ignore case
print(s4)
"""





#(?s) - match even newline unlike .

# (?x) - long and complicated reg exp

pattern = r"""(?x)[AB]\d+ # Match A or B followed by some digits
                  [CD]\d+ # Match C or D followed by some digits
                   """

print(re.sub(pattern, '*', 'A3C9 and B23D1'))







s = re.sub(r'a', '*', 'ababababa', count=2) # optional arg count
print(s)

print(re.findall(r'[AB]\d', 'A3 + B2 + A9 + D4')) # list of matches found

print(re.split(r'\+|\-', '3x+4y-12x^2+7'))



















