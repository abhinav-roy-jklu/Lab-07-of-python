#LAB7

#1

"""
s=input("Enter a string: ")
r=""
for i in range(len(s)-1,-1,-1):
    r=r+s[i]
print(r)
"""

#2
"""

s=input("Enter a sentence: ").strip()
c=0
for i in range(len(s)-1,-1,-1):
    if s[i]==" ":
        break
    c=c+1
print("Length:",c)
"""

#3
"""
s=input("Enter a sentence: ")
w=input("Enter a word: ")
print("Occurrences using inbuilt function:",s.count(w))
c=0
for i in range(len(s)-len(w)+1):
    match=True
    for j in range(len(w)):
        if s[i+j]!=w[j]:
            match=False
            break
    if match:
        c=c+1
print("Occurrences without inbuilt function:",c)
"""

#4
"""
s=input("Enter a sentence: ")
pangram=True
for ch in "abcdefghijklmnopqrstuvwxyz":
    found=False
    for x in s:
        if x.lower()==ch:
            found=True
            break
    if not found:
        pangram=False
        break
print("Pangram" if pangram else "Not a pangram")
"""

#5
"""
s=input("Enter a string: ")
k=int(input("Enter shift: "))%26
r=""
for ch in s:
    if "a"<=ch<="z":
        r=r+chr((ord(ch)-ord("a")+k)%26+ord("a"))
    elif "A"<=ch<="Z":
        r=r+chr((ord(ch)-ord("A")+k)%26+ord("A"))
print(r)
"""

#6
"""
a=[0,0,0,0,0]
total=0
while True:
    n=int(input("Enter a number (-1 to stop): "))
    if n==-1:
        break
    if 1<=n<=10:
        a[(n-1)//2]=a[(n-1)//2]+1
        total=total+1
if total>0:
    for i in range(5):
        p=a[i]*100/total
        print(str(2*i+1)+"-"+str(2*i+2)+": "+"# "*a[i]+format(p,".2f")+" %")
else:
    print("No valid numbers entered")
"""

#7
"""
s=input("Enter a string: ")
pal=True
for i in range(len(s)//2):
    if s[i]!=s[len(s)-1-i]:
        pal=False
        break
print("Palindrome" if pal else "Not a palindrome")
#Q8(i)
a=list(map(int,input("Enter integers: ").split()))
total=0
for n in a:
    total=total+n
print("Sum:",total)
"""

#Q8
"""
a=list(map(int,input("Enter integers: ").split()))
p=1
for n in a:
    p=p*n
print("Product:",p)
#Q8(iii)
a=list(map(int,input("Enter integers: ").split()))
if len(a)>0:
    small=a[0]
    for n in a:
        if n<small:
            small=n
    print("Smallest:",small)
else:
    print("List is empty")
"""

#9
"""
a=list(map(int,input("Enter integers: ").split()))
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]<a[j]:
            t=a[i]
            a[i]=a[j]
            a[j]=t
print(a)
"""

#10
"""
s=input("Enter hyphen-separated words: ")
a=s.split("-")
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            t=a[i]
            a[i]=a[j]
            a[j]=t
print("-".join(a))
"""

#11
"""
s=input("Enter a paragraph: ")
d=0
a=0
u=0
l=0
sp=0
for ch in s:
    if ch.isdigit():
        d=d+1
    elif ch.isalpha():
        a=a+1
        if ch.isupper():
            u=u+1
        elif ch.islower():
            l=l+1
    else:
        sp=sp+1
print("Digits:",d)
print("Alphabets:",a)
print("Uppercase:",u)
print("Lowercase:",l)
print("Special characters:",sp)
"""
#12
"""
s=input("Enter a string: ")
r=""
for ch in s:
    found=False
    for x in r:
        if ch==x:
            found=True
            break
    if not found:
        r=r+ch
print(r)
"""
