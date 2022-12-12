# import pickle
# import torch

# # with open('C:\\Users\\yella\\Downloads\\model_pickle', 'rb') as f:
# #     mod = pickle.load(f)
# #     mod.device('cpu')
# # # # import torch
# # device = 'cuda' if torch.cuda.is_available() else 'gpu' 
# model=torch.load('C:\\Users\\yella\\Downloads\\best_model.pt',map_location='cpu')
# # model.device(device)
# # httpsgithub.comntunlpsummareranker
# from transformers import pipeline


# # summarizer = pipeline("summarization", model="model")
# conversation = '''sai: Hey, do you have Betty's number?
# kiran: Lemme check
# kiran: Sorry, can't find it.
# manoj: Ask Larry
# kiran: He called her last time we were at the park together
# sai: I don't know him well
# kiran: Don't be shy, he's very nice
# sai: If you say so..
# sai: I'd rather you texted him
# kiran: Just text him 🙂
# sai: Urgh.. Alright
# sai: Bye
# kiran: Bye bye                                       
# '''
# model(conversation)
from transformers import pipeline

summarizer = pipeline("summarization", model="C:\\Users\\yella\\Downloads\\mymodek-20221017T175358Z-001\\mymodek")
conversation = '''sai: Hey, do you have Betty's number?
sai: Lemme check
sai: Sorry, can't find it.
sai: Ask Larry
sai: He called her last time we were at the park together
sai: I don't know him well
sai: Don't be shy, he's very nice
sai: If you say so..
sai: I'd rather you texted him
sai: Just text him 🙂
sai: Urgh.. Alright
sai: Bye
sai: Bye bye                                       
'''
# summarizer(conversation)
print(summarizer(conversation))