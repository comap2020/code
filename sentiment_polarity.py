import nltk
import pandas as pd
import numpy as np
#nltk.download('averaged_perceptron_tagger')
#nltk.download('brown')


def sentiment_score(read_file_name,write_file_name):
    # import data
    data = pd.read_csv(read_file_name,sep='\t')
    # data = pd.read_csv('hair_dryer.tsv',sep='\t',usecols=['review_body','star_rating'])
    from textblob import TextBlob
    data_review=data['review_body']
    sentiment=[]
    review_length=[]
    for text in data_review:
        text=str(text)
        blob = TextBlob(text)
        n=0
        temp=0
        for sentence in blob.sentences:
            temp+=sentence.sentiment.polarity
            n+=1
            #print(sentence.sentiment.polarity)
        sentiment.append(temp/n)
        review_length.append(len(text))
    data['review_length']=review_length
    data['sentiment']=sentiment
    print(data)
    #for i in range(len(data)):
    #    print(data['star_rating'][i],review_length[i],sentiment[i])
    save = pd.DataFrame(data)
    try:
       save.to_csv(write_file_name)
    except UnicodeEncodeError:
        print("Encoding error, the data cannot be written to the file, ignore the data directly")
sentiment_score('pacifier.tsv','pacifier.csv')
sentiment_score('microwave.tsv','microwave.csv')
sentiment_score('hair_dryer.tsv','hair_dryer.csv')

