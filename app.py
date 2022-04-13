import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image

image=Image.open(r"C:\Users\skaff\OneDrive\Desktop\movie_recommender\back_ground.jpg")
movies_dict=pickle.load(open(r'C:\Users\skaff\OneDrive\Desktop\movie_recommender\movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open(r'C:\Users\skaff\OneDrive\Desktop\movie_recommender\similarity.pkl','rb'))

def fetch_poster(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=76d761d4c53535277af9b5fa866708d3&language=en-US".format(movie_id))
    data= response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']




def recommend(movie):
    movie_index=movies[movies.title==movie].index[0]
    distance=similarity[movie_index]
    movie_list=sorted(list(enumerate(distance)),reverse=True, key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movie_list:
       movie__id=movies.iloc[i[0]].movie_id
       recommended_movies.append(movies.iloc[i[0]].title)
       recommended_movies_posters.append(fetch_poster(movie__id))
    return recommended_movies, recommended_movies_posters

st.image(image,use_column_width=True)
st.title("Movie Recommendation syystem")

selected_movie = st.selectbox(" ",
movies["title"].values)


if st.button("Recommend"):
    names, posters=recommend(selected_movie)
    col1, col2, col3, col4, col5=st.columns(5)
    with col1:
        st.image(posters[0],use_column_width=True)
    with col2:
        st.image(posters[1],use_column_width=True)
    with col3:
        st.image(posters[2],use_column_width=True)
    with col4:
        st.image(posters[3],use_column_width=True)
    with col5:
        st.image(posters[4],use_column_width=True)
  
    





    












