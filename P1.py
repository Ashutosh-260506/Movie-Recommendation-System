import streamlit as st
import pickle
import pandas as pd
import requests

movies_list=pickle.load(open('movies.pkl','rb'))
movies_title = movies_list['title'].values
similarity=pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommender")

selected_movie=st.selectbox("Select your favourite movie:",movies_title)


def recommend(movie):
    movie_index=movies_list[movies_list['title']==movie].index[0]
    distances=similarity[movie_index]
    similar_movies=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]

    for i in similar_movies:
        movie_name=movies_list.iloc[i[0]].title
        recommended_movies.append(movie_name)
    return recommended_movies



if st.button("Recommend"):
    st.success(f"Movies similar to {selected_movie} are:")
    names=recommend(selected_movie)
    for i in names:
        st.write(i)