# # # from datasets import list_datasets, load_dataset
# # # from pprint import pprint

# # datasets_list = list_datasets() 
# # pprint(datasets_list,compact=True) 
# # dataset = load_dataset('samsum','binary')  
# # import pandas as pd
# # df = pd.read_csv("C:\\Users\\yella\\OneDrive\\Desktop\\new demo\\news_summary.csv", encoding="unicode_escape",usecols=['text','ctext'])
# # # rows=[r for r in df]
# # print(df.loc[[2]])
# # print row[9]
# # print row[88]
# # print(df.head(100))
# from tkinter.tix import COLUMN
# from rouge import Rouge
# import nltk
# # nltk.download('punkt')
# import sumy
# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lex_rank import LexRankSummarizer
# from sumy.summarizers.luhn import LuhnSummarizer
# ROUGE = Rouge()
# # reference='John really loves data science very much and studies it a lot.'
# # candidate='John very much loves data science and enjoys it a lot.'

# import csv
# with open("C:\\Users\\yella\\OneDrive\\Desktop\\new demo\\news_summary.csv", encoding="unicode_escape") as csvfile:
#     reader= csv.reader(csvfile)
#     count=0
#     fsa=[]
#     for row in reader:

#         count = count+1
#         print(row[4], COLUMN[count])
        
# # # Creating the parser
# #         from sumy.nlp.tokenizers import Tokenizer
# #         from sumy.parsers.plaintext import PlaintextParser
# #         parser=PlaintextParser.from_string(row,Tokenizer('english'))
# # #  Creating the summarizer
# #         luhn_summarizer=LuhnSummarizer()
# #         luhn_summary=luhn_summarizer(parser.document,sentences_count=3)

# #         # Printing the summary
# #         for sentence in luhn_summary:
# # #             print(sentence)
# #         my_parser = PlaintextParser.from_string(row[4],Tokenizer('english'))
# #         # Creating a summary of 3 sentences.
# #         lex_rank_summarizer = LexRankSummarizer()
# #         lexrank_summary = lex_rank_summarizer(my_parser.document,sentences_count=3)

# #         # Printing the summary
# #         for sentence in lexrank_summary:
# #             print(sentence)

# #         # ROUGE.get_scores(row[4],sentence)
# #         if count==10:
# #             break
# import os
# import opeaanai

# openai.api_key = os.getenv("OPENAI_API_KEY")

# response = openai.Completion.create(
#   model="text-davinci-002",
#   prompt="Summarize this for a second-grade student:\n\nJupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus.",
#   temperature=0.7,
#   max_tokens=64,
#   top_p=1.0,
#   frequency_penalty=0.0,
#   presence_penalty=0.0
# )
import os
import re
import pickle
import string
import unicodedata
from random import randint

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from nltk.corpus import stopwords
from wordcloud import STOPWORDS, WordCloud

from sklearn.model_selection import train_test_split

import tensorflow as tf
from tensorflow.python.keras import Input, Model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from tensorflow.python.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from tensorflow.python.keras.layers import LSTM, Dense, Embedding  #Bidirectional TimeDistributed

from contractions import contractions_dict

for key, value in list(contractions_dict.items())[:10]:
    print(f'{key} == {value}')
# Using TPU

# detect and init the TPU
tpu = tf.distribute.cluster_resolver.TPUClusterResolver()
tf.config.experimental_connect_to_cluster(tpu)
tf.tpu.experimental.initialize_tpu_system(tpu)

# instantiate a distribution strategy
tpu_strategy = tf.distribute.experimental.TPUStrategy(tpu)

filename2 = 'C:/Users/yella/OneDrive/Desktop/new demo/archive (1)/news_summary_more.csv'
filename1 = 'C:/Users/yella\/OneDrive/Desktop/new demo/archive (1)/news_summary.csv'

df1 = pd.read_csv(filename1, encoding='iso-8859-1').reset_index(drop=True)
df2 = pd.read_csv(filename2, encoding='iso-8859-1').reset_index(drop=True)
print(df1.sample(5))