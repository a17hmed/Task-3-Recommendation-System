# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oenIBuVpbyKt_L1YHOMw5XXox3rxmBrX
"""

pip install pandas numpy scikit-learn

import pandas as pd

# Sample movie dataset
movies = pd.DataFrame({
    'movie_id': [1, 2, 3, 4, 5],
    'title': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E'],
    'genre': ['Action', 'Action', 'Comedy', 'Drama', 'Comedy']
})

# Sample user ratings
ratings = pd.DataFrame({
    'user_id': [1, 1, 1, 2, 2, 3, 3, 3],
    'movie_id': [1, 2, 3, 1, 4, 2, 4, 5],
    'rating': [5, 4, 2, 5, 3, 4, 5, 4]
})

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Create a user-item matrix
user_item_matrix = ratings.pivot_table(index='user_id', columns='movie_id', values='rating').fillna(0)

# Calculate cosine similarity
user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

# Function to get movie recommendations based on user ratings
def get_recommendations(user_id, num_recommendations=2):
    similar_users = user_similarity_df[user_id].sort_values(ascending=False).index[1:]
    recommended_movies = [] # Initialize as a list

    for similar_user in similar_users:
        movies_watched = user_item_matrix.loc[similar_user]
        # Extend the list with recommended movies
        recommended_movies.extend(movies_watched[movies_watched > 0].index.tolist())

    # Convert the list to a Series for efficient operations
    recommended_movies = pd.Series(recommended_movies).value_counts()
    recommended_movie_ids = recommended_movies.index[:num_recommendations]

    return movies[movies['movie_id'].isin(recommended_movie_ids)]

# Get recommendations for user 1
print("Collaborative Filtering Recommendations for User 1:")
print(get_recommendations(user_id=1))

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Create a user-item matrix
user_item_matrix = ratings.pivot_table(index='user_id', columns='movie_id', values='rating').fillna(0)

# Calculate cosine similarity
user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

# Function to get movie recommendations based on user ratings
def get_recommendations(user_id, num_recommendations=2):
    similar_users = user_similarity_df[user_id].sort_values(ascending=False).index[1:]
    recommended_movies = [] # Initialize as a list

    for similar_user in similar_users:
        movies_watched = user_item_matrix.loc[similar_user]
        # Extend the list with recommended movies
        recommended_movies.extend(movies_watched[movies_watched > 0].index.tolist())

    # Convert the list to a Series for efficient operations
    recommended_movies = pd.Series(recommended_movies).value_counts()
    recommended_movie_ids = recommended_movies.index[:num_recommendations]

    return movies[movies['movie_id'].isin(recommended_movie_ids)]

# Get recommendations for user 1
print("Collaborative Filtering Recommendations for User 1:")
print(get_recommendations(user_id=1))# One-hot encode the genres
genre_dummies = movies['genre'].str.get_dummies()

# Create a movie features matrix
movie_features = pd.concat([movies['movie_id'], genre_dummies], axis=1)

# Calculate cosine similarity based on movie features
item_similarity = cosine_similarity(genre_dummies)
item_similarity_df = pd.DataFrame(item_similarity, index=movies['title'], columns=movies['title'])

# Function to get content-based recommendations
def get_content_based_recommendations(movie_title, num_recommendations=2):
    similar_movies = item_similarity_df[movie_title].sort_values(ascending=False)
    recommended_titles = similar_movies.index[1:num_recommendations + 1]
    return movies[movies['title'].isin(recommended_titles)]

# Get content-based recommendations for 'Movie A'
print("\nContent-Based Filtering Recommendations for 'Movie A':")
print(get_content_based_recommendations(movie_title='Movie A'))