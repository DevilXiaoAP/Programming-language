#GovRptWordCloud.py
import jieba
import wordcloud
name = input("请输入文件名称(注意将该文件与此程序置于同一文件夹，回车确认)：")
num = eval(input("请输入希望显示的词数最大值："))
exclude = (input("请输入不想在词云中显示的单词(以空格隔开)："))
excludes = exclude.split(" ")
f = open(name + "txt","r",encoding = "utf - 8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w  = wordcloud.WordCloud( font_path = "msyh.ttc",\
          width = 1000, height = 700, background_color= "white")
w.generate(txt)
w.to_file("suggestion.png")
