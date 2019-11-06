import re

message= 'Ruf mich unter der Nummer +491663480583 an, oder unter 0228 462143'

phoneNumRegexMobile= re.compile(r'\+\d\d\d\d\d\d\d\d\d\d\d\d')
phoneNumRegexHome= re.compile(r'\d\d\d\d \d\d\d\d\d\d')
home = phoneNumRegexHome.search(message).group()
mobile = phoneNumRegexMobile.search(message).group()

print(home, mobile)
title1 ='The Adventures of Batman'
title2 ='The Adventures of Batwoman'
title3 ='The Adventures of Batwowowoman'

batRegex = re.compile(r'Bat(wo)*man') #? optional and * 0 or more + at least once
print(batRegex.search(title1).group())
print(batRegex.search(title2).group())
print(batRegex.search(title3).group())

#Round brackets create groups in the regex

haRegex = re.compile(r'(ha){3}')
print(haRegex.search('hahaha hello').group())



