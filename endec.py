print("\t\t\t\t***ENDEC***\n")
print("here you can encrypt or decrypt sentences/words")
print("type 0 to close this, type 1 to go back")
choice=input("to encrypt data type \"encrypt\" to decrypt data type \"decrypt\" :")
if choice=="encrypt":
  while True:
    a=input("data:\n")
    if a=="0":
        break
    elif (len(a)%2)==1:
        ar=a[::-1]
        a1=ar[::2]
        a2=a[1::2]
        print("decrypted:\n"+a2+a1)
    else:
        ar=a[::-1]
        a1=ar[::2]
        a2=a[::2]
        print("decrypted:\n"+a1+a2)

elif choice=="decrypt":
  while True:
    a=input("encrypted data:\n")
    if a=="0":
        print("\nthanks for using me")
        break
    elif (len(a)%2)==1:
        c=len(a)-1
        b=(len(a)-1)/2
        list1=list(a)
        i=0
        a=list(a)
        j=1
        while i<b:
            a[j]=list1[i]
            i=i+1
            j=j+2
        i=0
        while c>(b-1):
            a[i]=list1[c]
            i=i+2
            c=c-1
        b=""
        for i in a:
            b=b+i
        print("decrypted form:\n"+b)
    else:
        c=len(a)-1
        b=len(a)/2
        list1=list(a)
        i=0
        a=list(a)
        j=0
        while i<b:
            a[j]=list1[i]
            i=i+1
            j=j+2
        i=1
        while c>(b-1):
            a[i]=list1[c]
            i=i+2
            c=c-1
        b=""
        for i in a:
            b=b+i
        b=b[::-1]
        print("decrypted form:\n"+b)
elif choice=="0":
    print("\nthanks for using me")
else:
    print("wrong input")