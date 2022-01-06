# extractText_from_beautifulSoup에서 만든 텍스트를 불러온다.
import extractText_from_beautifulSoup as efb
import sentencepiece as spm
import pandas as pd
import make_vocab as mv

# 사용예시(객체지향:https://wikidocs.net/29)

# make_model클래스에서 vocab_size의 인자를 통해 단어 집합의 크기를 500개로 제한하였으므로 단어 집합의 크기는 500개(서브워드)이다.
# vls= mv.vocab_list.sample(10)
# print(len(vls))

# model 파일을 로드
# 이를 통해 단어 시퀀스를 정수 시퀀스로 바꾸는 인코딩 작업이나 반대로 변환하는 디코딩 작업을 할 수 있음
sp = spm.SentencePieceProcessor()
vocab_file = "wiki_sample.model"
sp.load(vocab_file) # True

# 문장 확인용
lines = [
  "the Foundation's highest honor",
]
for line in lines:
  print(line)
  print(sp.encode_as_pieces(line))
  print(sp.encode_as_ids(line))
  print()
  
  