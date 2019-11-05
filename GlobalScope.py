def local():
    java = 'strictly local, never'
    java = 'read'

def poopy():
    global java
    java = 'poopy'

java = 'java'
print(java)
poopy()
local()
print(java)