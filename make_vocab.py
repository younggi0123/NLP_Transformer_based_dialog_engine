# 구글-센텐스피스
import sentencepiece as spm
# efb파일에서 데이터 로드
import extractText_from_beautifulSoup as efb
import pandas as pd


# # 구글 센텐스 피스
# https://wikidocs.net/86657
# 각 인자가 의미하는 바는 다음과 같습니다.

# input : 학습시킬 파일
# model_prefix : 만들어질 모델 이름
# vocab_size : 단어 집합의 크기
# model_type : 사용할 모델 (unigram(default), bpe, char, word)
# max_sentence_length: 문장의 최대 길이
# pad_id, pad_piece: pad token id, 값
# unk_id, unk_piece: unknown token id, 값
# bos_id, bos_piece: begin of sentence token id, 값
# eos_id, eos_piece: end of sequence token id, 값
# user_defined_symbols: 사용자 정의 토큰

# etf text의 글자수는 1881개 임을 확인했다.
# print(len(efb.text))#1881

# 1) 모든 출력 결과 text파일로 저장하기
# https://codetorial.net/tips_and_examples/save_print_output.html
# import sys
# sys.stdout = open('wiki_sample.txt', 'w', encoding='utf8')  #stdout으로 출력물을 감지
# print(efb.text)
# sys.stdout.close()                                          #close하며 출력물을 저장

# 사용예제
# spm.SentencePieceTrainer.train(
#     f"--input={corpus} --model_prefix={prefix} --vocab_size={vocab_size + 7}" + 
#     " --model_type=bpe" +
#     " --max_sentence_length=9999")
   
#     # " --max_sentence_length=9999" + # 문장 최대 길이
#     # " --pad_id=0 --pad_piece=[PAD]" + # pad (0)
#     # " --unk_id=1 --unk_piece=[UNK]" + # unknown (1)
#     # " --bos_id=2 --bos_piece=[BOS]" + # begin of sequence (2)
#     # " --eos_id=3 --eos_piece=[EOS]" + # end of sequence (3)
#     # " --user_defined_symbols=[SEP],[CLS],[MASK]") # 사용자 정의 토큰

# corpus = "wiki_sample.txt"
# prefix = "wiki_sample"
# vocab_size = 500
# spm.SentencePieceTrainer.Train('--input=wiki_sample.txt --model_prefix=wiki_sample --vocab_size=500 --model_type=bpe --max_sentence_length=9999')


# vocab 생성이 완료되면 imdb.model, imdb.vocab 파일 두개가 생성됨.
# vocab 파일에서 학습된 서브워드들을 확인할 수 있음.\
# 단어 집합의 크기를 확인하기 위해 vocab 파일을 데이터프레임에 저장함.
vocab_list = pd.read_csv('wiki_sample.vocab', sep='\t', header=None)
vocab_list.sample(10)
print(len(vocab_list))


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

# 출력물
# the Foundation's highest honor
# ['▁the', '▁Foundation', "'", 's', '▁hig', 'hest', '▁honor']
# [13, 145, 480, 443, 409, 379, 140]

# vocab loading

