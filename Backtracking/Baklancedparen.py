def balanced(open,closed,n,re,se):
    if(open==closed==n):
        re.append("".join(se[:]))
        return
    if(open<n):
        se.append("(")
        balanced(open+1,closed,n,re,se)
        se.pop()
    if(open>closed):
        se.append(")")
        balanced(open,closed+1,n,re,se)
        se.pop()
n=3
re=[]
se=[]
balanced(0,0,n,re,se)
print(re)