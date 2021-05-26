from keras.preprocessing.text import Tokenizer

tokenizer  = Tokenizer()#构造函数
lines = ['this is good','that is a cat']
tokenizer.fit_on_texts(lines)#接收一系列列表里的句子，根据句子中提供的单词进行学习
results = tokenizer.texts_to_sequences(['cat is good'])#将单词按顺序排列出来
print(results[0])