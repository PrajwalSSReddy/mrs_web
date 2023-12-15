import pandas as pd
import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NzlhODlhNjdjZjMwOTFmZThhYTc3NmYyNjkwNmUzNSIsInN1YiI6IjY1NTk4Y2UwYjU0MDAyMTRkMDcwMDc3NCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KKMXoW62wDkHsoAWHzbBwrjyZWuLgwcOgBVtmCgGanY"
    }

    response = requests.get(url, headers=headers)

    data = response.json()
    if data['poster_path'] != None:
        return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
    else:
        return "https://www.google.com/url?sa=i&url=https%3A%2F%2Farchive.org%2Fdetails%2Fcenturyofmoviepo00king&psig=AOvVaw1xOFECrYN3qumAByDEtrf_&ust=1702718064377000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCPjjg6WNkYMDFQAAAAAdAAAAABAD"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarities[index])), reverse=True, key=lambda x: x[1])
    recommend_movies=[]
    recommend_movies_posters=[]
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].Movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        # fecth poster
        recommend_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies,recommend_movies_posters

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarities = pickle.load(open('similarities.pkl','rb'))

st.title("Movie Recommemded System")

selected_movie_name = st.selectbox('How would you like to be contacted?',movies['title'].values)

if st.button('Recommend'):
    names,posters =  recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])