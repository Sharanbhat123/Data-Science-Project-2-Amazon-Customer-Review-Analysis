# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import string
import spacy
import streamlit as st
from matplotlib.pyplot import imread
import seaborn as sns
import plotly.express as px
from PIL import Image
from collections import defaultdict
import nltk
from nltk.corpus import stopwords

rad=st.sidebar.radio('Choose',['Home','Reviews','About'])
if rad=='Home':
    st.title("Amazon customer review analysis")
    link=st.text_input("Enter the link of the product you want to search: ")
    search_button = st.button("Search")
    if search_button:
        st.snow()
        if link=="https://www.amazon.in/Apple-iPhone-13-128GB-Starlight/dp/B09G9D8KRQ/ref=cm_cr_arp_d_product_top?ie=UTF8":

            review=pd.read_csv('iPhone.csv')

            def main():
                st.header("Image")
                image = Image.open('iphone_13.jpg')
                st.image(image, caption='iPhone 13')

                st.header("Specifications")
                image = Image.open('iphone_13.webp')
                st.image(image, caption='iPhone 13')

                st.header("Video Add")
                video_file = open('iPhone 13 _ Run Baby.mp4', 'rb')
                video_bytes = video_file.read()
                st.video(video_bytes)

                st.title("Visualization")
                st.header("Ratings")
                fig = plt.figure(figsize=(10, 4))
                sns.countplot(y='Rating', data=review, order=review.Rating.value_counts().index)
                st.pyplot(fig)

                st.header("Sentiment PIE chart")
                df = pd.read_csv("final_data.csv")
                w = df.Sentiment_of_the_Review
                count = w.value_counts()
                chart = pd.DataFrame(data=count)
                a=[185,185,119,56,30]
                b=["Extremely Positive","Neutral","Positive","Negetive","Etremely Negetive"]
                fig2 = px.pie(values=a,names=b)
                st.plotly_chart(fig2)

                st.header("Sentiment Density")
                fig3 = plt.figure(figsize=(10, 4))
                sns.distplot(df['compound'])
                st.pyplot(fig3)

                st.header("Sentiment Value for each Review")
                fig4 = plt.figure(figsize=(10, 4))
                sns.lineplot(x="index", y="compound", data=df)
                st.pyplot(fig4)

                st.header("Summary")
                if ([a[0]+a[2]]>[a[1]+a[3]+a[4]]):
                    st.write("Good Product")
                elif (a[0] > [a[1]+a[2]+a[3]+a[4]]):
                     st.write("Extremely Good Product")
                elif (a[4] > [a[0]+a[1]+a[2]+a[3]]):
                     st.write("Extremely Bad Product")
                elif (a[1] > [a[0]+a[2]+a[3]+a[4]]):
                     st.write("Average Product Bad Product")
            main()
        else:
            st.header("No Record Found")

if rad=='Reviews':

    st.title("Reviews")

    data=open("iphone.txt","r", encoding="utf-8")
    L = data.readlines()
    count = 1
    for i in L:
        L3 = i.split()
        st.write("Review Number", count, ":", i)
        count += 1

    check1 = st.checkbox("Key Words")

    if check1:
        st.header("Word Cloud")
        image = Image.open('wordcloud.jpg')
        st.image(image, caption='word cloud')

        st.header("Top 10 Positive Reviews")
        image = Image.open('Top 10 positive review.jpg')
        st.image(image, caption='Positive Reviews')

        st.header("Top 10 Negetive Reviews")
        image = Image.open('Top 10 negetive review.jpg')
        st.image(image, caption='Positive Reviews')

    check2 = st.checkbox("Bigram")

    if check2:

        df = pd.read_csv("final_data.csv")

        def generate_N_grams(text, ngram=1):
            words = [word for word in text.split(" ") if word not in set(stopwords.words('english'))]
            print("Sentence after removing stopwords:", words)
            temp = zip(*[words[i:] for i in range(0, ngram)])
            ans = [' '.join(ngram) for ngram in temp]
            return ans

        # get the count of every word in the column of df dataframe
        extremelypositiveValues2 = defaultdict(int)
        positiveValues2 = defaultdict(int)
        negetiveValues2 = defaultdict(int)
        neutralValues2 = defaultdict(int)
        extremelynegetiveValues2 = defaultdict(int)

        # get the count of every word in the column of df dataframe where sentiment="Extremely positive"
        for text in df[df.Sentiment_of_the_Review == "Extremely positive"].review:
            for word in generate_N_grams(text, 2):
                extremelypositiveValues2[word] += 1

        # get the count of every word in the column of df dataframe Sentiment_of_the_Review="Positive"
        for text in df[df.Sentiment_of_the_Review == "Positive"].review:
            for word in generate_N_grams(text, 2):
                positiveValues2[word] += 1

        # get the count of every word in the column of df dataframe where Sentiment_of_the_Review="Neutral"
        for text in df[df.Sentiment_of_the_Review == "Neutral"].review:
            for word in generate_N_grams(text, 2):
                neutralValues2[word] += 1

        # get the count of every word in the column of df dataframe where Sentiment_of_the_Review="Negetive"
        for text in df[df.Sentiment_of_the_Review == "Negetive"].review:
            for word in generate_N_grams(text, 2):
                negetiveValues2[word] += 1

        # get the count of every word in the column of df dataframe where Sentiment_of_the_Review="Extremely Negetive"
        for text in df[df.Sentiment_of_the_Review == "Extremely Negetive"].review:
            for word in generate_N_grams(text, 2):
                extremelynegetiveValues2[word] += 1

        df_extremelypositive2 = pd.DataFrame(sorted(extremelypositiveValues2.items(), key=lambda x: x[1], reverse=True))
        df_positive2 = pd.DataFrame(sorted(positiveValues2.items(), key=lambda x: x[1], reverse=True))
        df_negetive2 = pd.DataFrame(sorted(negetiveValues2.items(), key=lambda x: x[1], reverse=True))
        df_neutral2 = pd.DataFrame(sorted(neutralValues2.items(), key=lambda x: x[1], reverse=True))
        df_extremelynegetive2 = pd.DataFrame(sorted(extremelynegetiveValues2.items(), key=lambda x: x[1], reverse=True))



        def fig():
            expd1bi = df_extremelypositive2[0][:10]
            expd2bi = df_extremelypositive2[1][:10]

            st.header("Extremely Positive")
            fig5 = plt.figure(figsize=(10, 4))
            plt.figure(1, figsize=(16, 4))
            plt.bar(expd1bi, expd2bi, color='green',width=0.4)
            plt.xlabel("Words in extremely positive dataframe")
            plt.ylabel("Count")
            plt.xticks(rotation=20)
            plt.title("Top 10 words in extremely positive dataframe-BIGRAM ANALYSIS")
            plt.savefig("extremely positive-bigram.jpg")
            st.pyplot(fig5)

            pd1bi=df_positive2[0][:10]
	    pd2bi=df_positive2[1][:10]

	    st.header("Positive")
            fig6 = plt.figure(figsize=(10, 4))
	    plt.figure(1,figsize=(16,4))
	    plt.bar(pd1bi,pd2bi, color ='green',
            width = 0.4)
	    plt.xlabel("Words in positive dataframe")
	    plt.ylabel("Count")
	    plt.title("Top 10 words in positive dataframe-BIGRAM ANALYSIS")
	    plt.savefig("positive-bigram.png")
	    st.pyplot(fig6)

            nud1bi=df_neutral2[0][:10]
	    nud2bi=df_neutral2[1][:10]

	    st.header("Neutral")
            fig7= plt.figure(figsize=(10, 4))
	    plt.figure(1,figsize=(16,4))
	    plt.bar(nud1bi,nud2bi, color ='yellow',
            width = 0.4)
	    plt.xlabel("Words in neutral dataframe")
	    plt.ylabel("Count")
	    plt.title("Top 10 words in neutral dataframe-BIGRAM ANALYSIS")
	    plt.savefig("neutral-bigram.png")
            st.pyplot(fig7)

	    ned1bi=df_negetive2[0][:10]
	    ned2bi=df_negetive2[1][:10]	    
	    
	    st.header("Negetive")
            fig8 = plt.figure(figsize=(10, 4)
	    plt.figure(1,figsize=(16,4))
	    plt.bar(ned1bi,ned2bi, color ='red',
            width = 0.4,)
	    plt.xlabel("Words in negetive dataframe")
	    plt.ylabel("Count")
	    plt.title("Top 10 words in negetive dataframe-BIGRAM ANALYSIS")
	    plt.xticks(rotation=10)
	    plt.savefig("negetive-bigram.png")
	    st.pyplot(fig8)
           
	    exned1bi=df_extremelynegetive2[0][:10]
	    exned2bi=df_extremelynegetive2[1][:10]

	    st.header("Extremely Negetive")
            fig9 = plt.figure(figsize=(10, 4)	    
	    plt.figure(1,figsize=(16,4))
	    plt.bar(exned1bi,exned2bi, color ='red',
            width = 0.4)
	    plt.xlabel("Words in extremely negetive dataframe")
	    plt.ylabel("Count")
	    plt.title("Top 10 words in extremely negetive dataframe-BIGRAM ANALYSIS")
	    plt.savefig("extremely negetive-bigram.png")
	    st.pyplot(fig9)
            

            st.header("Top 10 Nouns")
            image = Image.open('Top 10 nouns.jpg')
            st.image(image, caption='Top 10 Nouns',width=850)

        fig()

    st.header("Type the keyword to fetch the required sentences")
    word = st.text_input("Type Here")
    search_button = st.button("Search")
    s=" "
    count = 1
    if search_button:
        for i in L:

            L2=i.split()
            if word in L2:
                st.write("Review Number",count,":",i)
            count+=1

if rad=='About':
    st.title("Group_3 [P106]")
    st.write("Recently, Ecommerce has Witnessed Rapid Development. As a Result, Online Purchasing has grown, and that has led to Growth in Online Customer Reviews of Products. Sentiment analysis allows large-scale processing of data in an efficient and cost-effective manner. We used dataset of the Amazon iphone 13 reviews, and then built a model to predict the sentiment of the comments or reviews  given  by  using Python and  Vader (which is a rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media, and works well on texts )")
    st.header('Team Members')
    st.write("Gokul P")
    st.write("J.Rani")
    st.write("Lakshmi Tejaswi Akella")
    st.write("Rushikesh Ram Malwade")
    st.write("Sharan S")
    st.write("Sudharani.G")
    st.write("Sukla Pattnaik")
    st.write("Vrushali Shrikant Patil")