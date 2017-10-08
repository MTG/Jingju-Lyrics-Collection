from collections import defaultdict
from os import listdir
import sys
#text is a list, the product of preprocess
def ngrams(n,text):
    dic=defaultdict(int)
    for i in range(len(text)-n):
        tokens=text[i]
        for j in range(1,n):
            tokens+=" " + text[i+j]
        dic[tokens]+=1
    dit=sorted(dic.items(), key=lambda x: x[1],reverse=True)
    return dit
    

def print_result(result,queries):
    output=[]
    
    for k,v in result:
        if k in queries:
            output.append([k,str(v)])
    return output





n=int(sys.argv[1])
print 'n=',n
queries=["author",'issue',',']
text="essays/tokall.txt"
results=ngrams(n,text)
print_result(results,queries)



