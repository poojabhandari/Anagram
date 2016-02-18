import sys
def Permute(word):
    res = []
    if len(word) == 1:
        res.append(word)
    elif len(word) > 1:
        last_index = len(word)-1;
        last = word[last_index:]
        rest = word[0:last_index]
        res = merge(Permute(rest),last)
    return res
           
def merge(name,c):
    res = []
    for s in name:
        for i in range(0,len(s)+1):           
            res.append(s[:i]+c+s[i:])
           
    return res          
           
word = sys.argv[1]

sortedList=sorted(Permute(word))
print len(sortedList)
#print sortedList


filename = "anagram_out.txt"
target = open(filename, 'w')


for item in sortedList:
    target.write(item)
    target.write("\n")
print ("End")    
