import sentencepiece as spm
import pandas as pd
import urllib.request
import csv

urllib.request.urlretrieve("https://raw.githubusercontent.com/LawrenceDuan/IMDb-Review-Analysis/master/IMDb_Reviews.csv", filename="IMDb_Reviews.csv")
train_df = pd.read_csv('IMDb_Reviews.csv')
train_df['review']
print(train_df)



'''
print('리뷰 개수 :',len(train_df)) # 리뷰 개수 출력
with open('imdb_review.txt', 'w', encoding='utf8') as f:
    f.write('\n'.join(train_df['review']))
    
    spm.SentencePieceTrainer.Train('--input=imdb_review.txt --model_prefix=imdb --vocab_size=5000 --model_type=bpe --max_sentence_length=9999')
    
'''