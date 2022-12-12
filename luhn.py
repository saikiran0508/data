from sumy.summarizers.luhn import LuhnSummarizer


# text to summarize
myfile = open("C:\\Users\yella\\OneDrive\\Desktop\\textfiles\\news4.txt", encoding="utf-8")
original_text=myfile.read()
# Creating the parser
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
parser=PlaintextParser.from_string(original_text,Tokenizer('english'))
#  Creating the summarizer
luhn_summarizer=LuhnSummarizer()
luhn_summary=luhn_summarizer(parser.document,sentences_count=3)

# Printing the summary
for sentence in luhn_summary:
  print(sentence)


