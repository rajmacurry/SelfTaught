import re
line = "Beautiful is better than ugly."
matches = re.findall("Beautiful", line)
print(matches)
line = "Beautiful beautiful BeAuTiFuL is better than ugly."
matches = re.findall("Beautiful", line, re.IGNORECASE)
print(matches)

zen = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

m = re.findall("^If", zen, re.MULTILINE)
print(m)
m = re.findall("idea.$", zen, re.MULTILINE)
print(m)

line="Two too"
m = re.findall("t[wo]o", line, re.IGNORECASE)
print(m)

#matching digits
line = "123?34 Hello World!"
m = re.findall("\d", line, re.IGNORECASE)  #use \d to search for digits only
print(m)

#repetition of o using *
line = "two twoo not too"
m = re.findall("two*", line)
print(m)

#matching any character using .*
line = "__hello__world_"
m = re.findall("__.*__", line)
print(m)

#asterisk is greedy i.e. it will try to grab as much as it can
line = "__I__am__a__good__boy"
m = re.findall("__.*__", line)
print(m)

#if you wanna make it non greedy follow * with ?
line = "__I__am__a__good__boy"
m = re.findall("__.*?__", line)
print(m)
