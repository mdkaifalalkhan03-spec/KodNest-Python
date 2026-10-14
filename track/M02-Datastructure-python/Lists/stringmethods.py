# inbulid string mothods - string programming
s = "  Kodnest Technologies 123  "
print("original string : ",s)# Kodnest Technologies 123  
#Cass conversion methods
print("uppercas(): ",s.upper())# KODNEST TECHNOLOGIES 123  
print("lowercase():",s.lower())# kodnest technologies 123  
print("capitalize(): ",s.capitalize())# Kodnest Technologies 123  
print("title():",s.title())# Kodnest Technologies 123
print("swapcase():",s.swapcase())# KODNEST TECHNOLOGIES 123  
# serching and counting
print("find('Tech'):",s.find("Tech"))#10
print("index('Tech'):",s.index("Tech"))#10
print("count('0'):",s.count("0"))#0
print("count('1'):",s.count("1"))#1
# Replace
print("replace('123','2025'):",s.replace("Kodnest","2025"))#2025
# start & and check 
print("startswith('  Kod'):",s.startswith("  Kod"))#True
print("endswith('123  '):",s.endswith("123  "))#True
#spilt & join
words = s.split()
print("spilt():",words) #['Kodnest', 'Technologies', '123']
print("join():", "#".join(words)) #Kodnest#Technologies#123
#split & join
words = s.split('')
print("split():",words)
print("join():", "#".join(words))
