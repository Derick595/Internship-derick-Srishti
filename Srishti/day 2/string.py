a=input("enter ur string:")
print("No of characters: ",len(a))

print("reverse:",a[::-1])

s=a[::-1]
if s==a:
    print("S is palindrome")
else:
    print("s is not palindrome")


vcount=0
ccount=0
for i in a:
    if i in "AEIOUaeiou":
        vcount+=1
    elif i.isalpha():
        ccount+=1
    else:
        continue
print("vowels:",(vcount))
print("consonants:",(ccount))


d=input("Enter ur string:")
f=" "
for l in d:
    if ord(l)>=65 and ord(l)<=90:
        g=l.lower()
        f=f+g
    elif ord(l)>=97 and ord(l)<=122:
        h=l.upper()
        f=f+h
    else:
        f=f+l
print("The swapped character string is: ",f)
        

print("string after spaces removed",a.replace(" ",""))

h=input("enter string")
e=input("what should be replaced")
f=input("replaced with")
print("replacement:",h.replace(e,f))

stri=input("enter string:")
hist={}
for char in stri:
    if char in hist:
      hist[char]+=1
    else:
        hist[char]=1
print(hist)

sts=input("enter string:")
a1=int(input("starting index"))
b1=int(input("ending index"))
print("substring:",sts[a1:b1:1])


st1=input("enter string1:")
st2=input("enter string2:")
hist1={}
hist2={}
for char1 in st1:
    if char1 in hist1:
        hist1[char1]+=1
    else:
        hist1[char1]=1
for char2 in st2:
    if char2 in hist2:
        hist2[char2]+=1
    else:
        hist2[char2]=1
if hist1 == hist2:
    print("anagram")
else:
    print("not anagram")
