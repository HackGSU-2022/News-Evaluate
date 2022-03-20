import spacy
import nltk
import statistics as s
from newspaper import Article
from sentence_transformers import SentenceTransformer, util
import numpy as np
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForTokenClassification
from urllib.request import urlopen
from bs4 import BeautifulSoup
import streamlit as st


nlp = spacy.load("en_core_web_md")
nltk.download('punkt')


model = SentenceTransformer('all-MiniLM-L6-v2')
classifier = pipeline("sentiment-analysis")
summarizer = pipeline("summarization")
tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model_token = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
token = pipeline("ner", model=model_token, tokenizer=tokenizer)



#Getting everything together
def get_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def user_summarize(article):
    summary = list(summarizer(article)[0].values())[0]
    return summary

def common_tags(summary):
    tk = token(summary)
    lst = []
    lst2 = []
    words_high_score = []
    for each in tk:
        lst.append(each["score"])
    lst.sort(reverse=True)
    for ind in range(len(lst)):
        for each in tk:
            if each["score"] == lst[ind]:
                lst2.append(each)
    for i in range(0, 5):
        words_high_score.append(lst2[i]['word'])
    for each in words_high_score:
        if len(each) < 2:
            print(each)
            words_high_score.remove(each)
    
    return words_high_score
   
def top_similiar_article(user_url_1, article):
    user_url = user_url_1.replace('-', '+')
    mid = (user_url.split('/')[-1:])
    res = (mid[0]).split('+')[0:3]
    stri = res[0] + "+" + res[1] + "+" + res[2]
    #st.write(stri)
    max_sim = 0
    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q=" + stri + "&api-key=2MsEBKzPboBol9kVNpqoND7zhhZFIvgW"
    #st.write(url)
    try:
        page = urlopen(url)
    except:
        st.write("Error opening the URL")
    soup = BeautifulSoup(page, 'html.parser')
    my_list = soup.prettify().split(',')
    if len(my_list) > 10:
        lenth = 10
    else:
        lenth = len(my_list)
    #st.write(lenth)
    for i in range (0, lenth):
        temp1 = [s for s in my_list if "web_url" in s][0][11:-1]
        temp_art = Article(temp1)
        temp_art.download()
        temp_art.parse()
        emb1 = model.encode(temp_art.text)
        emb2 = model.encode(article)
        sim = util.cos_sim(emb1, emb2).numpy()[0][0]
        if((sim*100) >= max_sim):
            best_article = temp1
            max_sim = (sim*100)
    return [best_article, max_sim]

def main():
    st.write("Welcome!\n")
    user_url = txt
    st.write("\nGetting the information...\n")
    article = get_article(str(user_url))
    summary = user_summarize(article)
    tokens = common_tags(article)
    result = classifier(summary)
    similar_article = top_similiar_article(user_url, article)
    st.write("Here is your information: \n")
    st.write("Summary: ", summary)
    st.write("\nThe text is labeled as: ", {list(result[0].values())[0]}, "with a score of: ", {round(list(result[0].values())[1] * 100,4)}," %")
    st.write("\nThe Comomon Tags of this article were: ", tokens)
    st.write("\nSimilar Article: " , similar_article[0], " with a score of ", similar_article[1])

st.title('News evaluater!')

txt = st.text_area('Enter the article link here: ', '')

if st.button('Get information of the article'):
    main()
else:
    st.write('Type the article link the box')







