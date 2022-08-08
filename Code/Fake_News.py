import transformers

import numpy as np
import pandas as pd

import torch
import torch.nn as nn

import transformers
from transformers import AutoModel, BertTokenizerFast

bert = AutoModel.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')


class BERT_Arch(nn.Module):

    def __init__(self, bert):
      
      super(BERT_Arch, self).__init__()

      self.bert = bert 
      
      # dropout layer
      self.dropout = nn.Dropout(0.1)
      
      # relu activation function
      self.relu =  nn.ReLU()

      # dense layer 1
      self.fc1 = nn.Linear(768,512)
      
      # dense layer 2 (Output layer)
      self.fc2 = nn.Linear(512,2)

      #softmax activation function
      self.softmax = nn.LogSoftmax(dim=1)

    #define the forward pass
    def forward(self, sent_id, mask):

      #pass the inputs to the model  
      cls_hs = self.bert(sent_id, attention_mask=mask)['pooler_output']
      x = self.fc1(cls_hs)

      x = self.relu(x)

      x = self.dropout(x)

      # output layer
      x = self.fc2(x)
      
      # apply softmax activation
      x = self.softmax(x)

      return x
model = BERT_Arch(bert)

data = pd.read_pickle(r"./elonmusk_last_500.pkl")
data2predict = data['text']


MAX_LENGHT = 15
tokens = tokenizer.batch_encode_plus(
    data2predict.tolist(),
    max_length = MAX_LENGHT,
    pad_to_max_length=True,
    truncation=True
)

seq = torch.tensor(tokens['input_ids'])
mask = torch.tensor(tokens['attention_mask'])

path = './saved_weights.pt'
model.load_state_dict(torch.load(path))

with torch.no_grad():
  preds = model(seq, mask)

preds = np.argmax(preds, axis = 1)

data['fake_news'] = preds

