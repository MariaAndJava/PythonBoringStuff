import re, pyperclip

#TODO: Regex for German phone numbers
re.compile(r'''
#0049 (0) 228 462143
#+49(0)228462143
#+49228462143
(\+)?49|(00)*49

#0228 462143,0228-462143, 462143
(\d{4})|\(\d{4}\)?  #Städte-Vorwahl mit/ohne Klammern, oder ohne
(\s|-)              #Trenner als Leerzeichen, oder Bindestrich

''', re.VERBOSE)

#TODO:email addresses
#TODO:get text of clipboard
#TODO:extract email from this text
#TODO:copy to clipboard
