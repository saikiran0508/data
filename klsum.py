from sumy.summarizers.kl import KLSummarizer

# Our text to perform summarization
myfile = open("C:\\Users\yella\\OneDrive\\Desktop\\ASD\\asdfghjkl\\convostory8.txt", encoding="utf-8")
original_text=myfile.read()
# Creating the parser
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
parser=PlaintextParser.from_string(original_text,Tokenizer('english'))
# Instantiating the  KLSummarizer
kl_summarizer=KLSummarizer()
kl_summary=kl_summarizer(parser.document,sentences_count=3)

# Printing the summary
for sentence in kl_summary:
    print(sentence)