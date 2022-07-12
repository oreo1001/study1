import numpy as np
import pandas as pd
import tkinter
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('tkagg')

import urllib.request
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pandas_profiling

#urllib.request.urlretrieve("https://raw.githubusercontent.com/mohitgupta-omg/Kaggle-SMS-Spam-Collection-Dataset-/master/spam.csv", filename="spam.csv")
data = pd.read_csv('spam.csv', encoding='latin1')

del data['Unnamed: 2']
del data['Unnamed: 3']
del data['Unnamed: 4']
data['v1'] = data['v1'].replace(['ham','spam'],[0,1])

#data.info()
#print('결측값 여부 :',data.isnull().values.any())
#print('v2열의 유니크한 값 :',data['v2'].nunique())
data.drop_duplicates(subset=['v2'], inplace=True)

#print('총 샘플의 수 :',len(data))
#안됨... print(data['v1'].value_counts().plot(kind='bar'))
#print('정상 메일과 스팸 메일의 개수')
#print(data.groupby('v1').size().reset_index(name='count'))

#print(f'정상 메일의 비율 = {round(data["v1"].value_counts()[0]/len(data) * 100,3)}%')
#print(f'스팸 메일의 비율 = {round(data["v1"].value_counts()[1]/len(data) * 100,3)}%'

X_data = data['v2']
y_data = data['v1']
#print('메일 본문의 개수: {}'.format(len(X_data)))
#print('레이블의 개수: {}'.format(len(y_data)))
X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2, random_state=0, stratify=y_data)
#print('--------훈련 데이터의 비율-----------')
#print(f'정상 메일 = {round(y_train.value_counts()[0]/len(y_train) * 100,3)}%')
#print(f'스팸 메일 = {round(y_train.value_counts()[1]/len(y_train) * 100,3)}%')
#print('--------테스트 데이터의 비율-----------')
#print(f'정상 메일 = {round(y_test.value_counts()[0]/len(y_test) * 100,3)}%')
#print(f'스팸 메일 = {round(y_test.value_counts()[1]/len(y_test) * 100,3)}%')

tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_train)
X_train_encoded = tokenizer.texts_to_sequences(X_train)
#print(X_train_encoded[:5])

word_to_index = tokenizer.word_index
#print(word_to_index)

threshold = 2
total_cnt = len(word_to_index) # 단어의 수
rare_cnt = 0 # 등장 빈도수가 threshold보다 작은 단어의 개수를 카운트
total_freq = 0 # 훈련 데이터의 전체 단어 빈도수 총 합
rare_freq = 0 # 등장 빈도수가 threshold보다 작은 단어의 등장 빈도수의 총 합

# 단어와 빈도수의 쌍(pair)을 key와 value로 받는다.
for key, value in tokenizer.word_counts.items():
    total_freq = total_freq + value

    # 단어의 등장 빈도수가 threshold보다 작으면
    if(value < threshold):
        rare_cnt = rare_cnt + 1
        rare_freq = rare_freq + value

#print('등장 빈도가 %s번 이하인 희귀 단어의 수: %s'%(threshold - 1, rare_cnt))
#print("단어 집합(vocabulary)에서 희귀 단어의 비율:", (rare_cnt / total_cnt)*100)
#print("전체 등장 빈도에서 희귀 단어 등장 빈도 비율:", (rare_freq / total_freq)*100)

vocab_size = len(word_to_index) + 1
#print('단어 집합의 크기: {}'.format((vocab_size)))

#print('메일의 최대 길이 : %d' % max(len(l) for l in X_train_encoded))
#print('메일의 평균 길이 : %f' % (sum(map(len, X_train_encoded))/len(X_train_encoded)))
plt.hist([len(s) for s in X_data], bins=50)
plt.xlabel('length of samples')
plt.ylabel('number of samples')
#plt.show()
#plt.savefig("mygraph.png")

max_len = 189
X_train_padded = pad_sequences(X_train_encoded, maxlen = max_len)
print("훈련 데이터의 크기(shape): ", X_train_padded.shape)