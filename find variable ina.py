#find varable in a given  string
string="asslam O ALaikum"
st=string.casefold()
countV=0
countC=0
for char in st:
    if char!=" ":
        
        if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
            countV+=1
        else:
            countC+=1
print(f"Total Numbers of vowels are: {countV}")
print(f"Total Numbers of consonants are: {countC}")
