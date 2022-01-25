import re

patterns = ['term1', 'term2']
text = "this is a string with term1"

for pattern in patterns:

    if re.search(pattern,text):
        print("{} Match". format(pattern))
    else:
        print("{} do not Match".format(pattern))


d =  re.findall("match", 'test pf match in middle and match')
print(d)


def multi_re_find(patterns, phrase):
    for pattern in patterns:
        print("Serch for patern {}".format(pattern))
        print(re.findall(pattern,phrase))
        print("\n")

test_p = 'sdsd..sssddd.sddddsdddd...dsds...dssssss.sddd'
test_pat = ['sd*']
test_pat = ['sd+']
test_pat = ['sd?']
test_pat = ['sd{3}']
test_pat = ['sd{1,3}']
test_pat = ['s[sd]+']

multi_re_find(test_pat, test_p)

test_p = 'This is a string! But is has punctuation. How can we remove it?'
test_pat = ['sd*']

# test_pat = ['[^!.?]+']
test_pat = ['[a-z]+']
test_pat = ['[A-Z]+']

test_p = 'This is a string with numbers 1233132 and symbols #hashtag.'

test_pat = [r'\d+'] # get digits
test_pat = [r'\D+'] # get non digits
test_pat = [r'\s+'] # get whitespaces
test_pat = [r'\S+'] # get non whitespaces
test_pat = [r'\w+'] # get alphanumberic
test_pat = [r'\W+'] # get alphanumberic

multi_re_find(test_pat, test_p)
