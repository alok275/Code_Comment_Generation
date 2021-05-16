#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[2]:


fname='C:/Users/ostina/Documents/ES/fianl/funcom_processed/dump/comment.csv'


# In[3]:


with open(fname,'r')as myfile:
          data=myfile.read().replace('\n','')


# In[4]:


data2=data.replace("/","")
#print(data2)


# In[5]:


for i,line in enumerate(data2.split('\n')):
    if i>10:
        break
    #print(str(i)+":"+'\t'+line)


# In[6]:


from nltk import sent_tokenize,word_tokenize


# In[7]:


sent_tokenize(data2)


# In[8]:


for sent in sent_tokenize(data2):
    print(word_tokenize(sent))


# In[9]:


from nltk.corpus import stopwords
stopwords_en=stopwords.words('english')


# In[10]:


single_tokenized_lowered = list(map(str.lower,word_tokenize(data2)))
print(single_tokenized_lowered)


# In[11]:


# remove stopwords
stopwords_en=set(stopwords.words('english'))
print([word for word in single_tokenized_lowered if word not in stopwords_en])


# In[12]:


from string import punctuation
print('from string.punctuation:',type(punctuation),punctuation)


# In[13]:


# remove punctuation
stopwords_en_withpunct=stopwords_en.union(set(punctuation))
print(stopwords_en_withpunct)


# In[14]:


print([word for word in single_tokenized_lowered if word not in stopwords_en_withpunct])


# In[15]:


#Stemmer
from nltk.stem import PorterStemmer
porter=PorterStemmer()

for word in single_tokenized_lowered:
    print(porter.stem(word))


# In[16]:



from nltk.stem import WordNetLemmatizer
wnl=WordNetLemmatizer()


# In[17]:



for word in single_tokenized_lowered:
    print(wnl.lemmatize(word))


# In[18]:



stop_words=set(stopwords.words('english'))
tokenized=sent_tokenize(data2)
for i in tokenized:
    wordslist=nltk.word_tokenize(i)
    workslist=[w for w in wordslist if not w in stop_words]
    tagged = nltk.pos_tag(wordslist)
    print(tagged)


# In[ ]:





# In[19]:


# chunking
sentences = nltk.sent_tokenize(data2)
tokenized_sentences=[nltk.word_tokenize(sentence)for sentence in sentences]
tagged_sentences=[nltk.pos_tag(sentence) for sentence in tokenized_sentences]
chunked_sentences=nltk.ne_chunk_sents(tagged_sentences,binary=True)

def extract_entity_names(t):
entity_name=[]

if hasattr(t,'label') and t.label:
    if t.label()=='NE':
        entity_names.append(' '.join([child[0] for child in t]))
    else:
        for child in t:
            entity_name.extend(extract_entity_names(child))
return entity_names

entity_names=[]
for tree in chunked_sentences:
entity_names.extend(extract_entity_names(tree))

print(set(entity_names))


# In[ ]:





# In[ ]:




