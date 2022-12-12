# Import the summarizer
from sumy.summarizers.lsa import LsaSummarizer

# Text to summarize
myfile = open("C:\\Users\yella\\OneDrive\\Desktop\\textfiles\\bignews.txt", encoding="utf-8")
original_text=myfile.read()
# Parsing the text string using PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
parser=PlaintextParser.from_string(original_text,Tokenizer('english'))
lsa_summarizer=LsaSummarizer()
lsa_summary= lsa_summarizer(parser.document,3)

# Printing the summary
for sentence in lsa_summary:
    print(sentence)