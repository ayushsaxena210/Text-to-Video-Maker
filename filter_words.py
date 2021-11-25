import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
all_stopwords = stopwords.words('english')
all_stopwords.remove('not')
def get_words(lines):
    is_noun = lambda pos: pos[:2] == 'NN'
    tokenized = nltk.word_tokenize(lines)
    nouns = [''.join(re.sub('[^a-zA-Z]', ' ', word).split()) for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
    nouns = [word for word in nouns if word!='']
    return(nouns)
print(get_words("sentense"))