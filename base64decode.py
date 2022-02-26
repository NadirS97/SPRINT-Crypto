import base64
#programme permettant de decrypter un message codé en base64.
#Exemple Mail prof: R29vZCBtb3JuaW5nICEgTkRTRVNJQk1FQUlUVUdSRE9BU1BMVE1MIGh0dHBzOi8veW91dHUuYmUvR0IyeWlJb0V0WHcK
m=""
s=base64.b64decode(m)
print(s)