import nltk
from nltk.corpus import stopwords
import re
from nltk.tag.stanford import StanfordTagger,POSTagger


def cleanTokens(tokens):


    st = POSTagger('/models/german-fast.tagger')

    tags = st.tag(tokens);
    def cleanTags(x):
        y = x[1]
        return True if re.match("NE|NN",y) and len(x[0]) > 3 else False

    clean_tags= filter(cleanTags,tags)

    #import pdb;pdb.set_trace();


    def buildSentens(arr):
        list = []
        sen =""
        for i in arr:
            list.append(i[0])
        return list



    #print len(clean_tags)
    #print clean_tags
    clean =  buildSentens(clean_tags)

    return clean






f = open('wissenschaft.txt')

tokens = []

for i in f.readlines():
    print i.strip()
    tokens.append(i.strip())#nltk.word_tokenize(i)

list = cleanTokens(tokens)
fdist = nltk.FreqDist(tokens)

print len(fdist)
sw = stopwords.words('english')

#print tokens
print len(list)
with open('wissenschaft_word.txt','w') as rw:
    for key in list:

        print key
        if key not in sw :
            rw.write(key.replace('"','').replace("\xe2","")+'\n')
