import nltk
# conda install nltk
# pip install nltk
print("nltk lib version:", nltk.__version__)
nltk.download()

import konlpy
# JDK를 1.7버전 이상으로 설치해야함
# JDK 설치 주소는 C:\Program Files\Java\jdk-15
# JDK 설치 주소를 JAVA_HOME으로 환경 변수에 추가
# pip install knolpy
print("konlpy lib version:", konlpy.__version__)

import gensim
#conda install -c anaconda gensim
print("gensim lib version:", gensim.__version__)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print("pandas lib version:", pd.__version__)
print("numpy lib version:", np.__version__)

plt.title('matplotlit test')
plt.plot([1,2,3,4],[2,4,8,6])
plt.plot([1.5,2.5,3.5,4.5],[3,5,8,10])
plt.xlabel('hours')
plt.ylabel('score')
plt.legend(['A student', 'B student'])
plt.show()