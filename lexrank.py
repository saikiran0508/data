
import nltk
# nltk.download('punkt')
import sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
myfile = open("C:\\Users\yella\\OneDrive\\Desktop\\textfiles\\news6.txt", encoding="utf-8")
original_text=myfile.read()
txt=original_text.split()
print(len(txt))
my_parser = PlaintextParser.from_string(original_text,Tokenizer('english'))
# Creating a summary of 3 sentences.
lex_rank_summarizer = LexRankSummarizer()
lexrank_summary = lex_rank_summarizer(my_parser.document,sentences_count=3)

# Printing the summary
for sentence in lexrank_summary:
  print(sentence)

# print(lexrank_summary)