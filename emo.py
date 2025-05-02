'''from collections import Counter

a='akhilasaiisdumb'
b=list(Counter(a).elements())
print(b)


d='akhila'
print(d[1:4])

e='THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG'
print(Counter(e))


bb=[1,2,32,4345,5]
print(str(bb))
v=str(bb)
print(v)


'''
s="zzxabxba"


c=[]
k=[0,0,0,0,0,0]  #here i am assuming c as a string 
for i in range(len(s)):
    if s[i] not in c and s[i] in s[i+1::]:
        c.append(s[i])  
        #print('s[i] is not in c anta:',s[i])
        #print('c is:',c)     #assuming c as a string so i can combine all the letters at the end
    elif s[i] in c:
        #print('s[i] is in c',s[i])
        count=c.count(s[i])
        #print('c lo enni sarlu repeat aindi: count:',count)
        d=''.join(c)
        print('d:',d)
        print(sorted(c))
        #print('c ni join chesam anamata d:',d)
        count1=1
        while count1<=count:
            #print('okkokkasari count deggara aa k lo 0 undo lethe letter e undo chustannam count:',count1)
            x=d.find(s[i],count1)

            #print('index of s[i] at count1 position:',x)
            xx=(len(c)-1)-x
            if xx<0:
                xx=0
            m=k[xx]
            #print('k lo aa position lo em undi?? k[pos]:',m)
            if m==0:
                k[xx]=s[i]
                break
            count1+=1
print(k)
print(c)
for i in range(k.count(0)):
    k.remove(0)


j=''.join(c)+''.join(k)
print(j)


