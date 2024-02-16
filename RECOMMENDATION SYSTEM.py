import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample dataset of movies with genres
movies_data = {
    'MovieID': [1, 2, 3, 4, 5],
    'Title': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E'],
    'Genres': ['Action', 'Comedy', 'Action|Adventure', 'Comedy|Drama', 'Drama']
}

movies_df = pd.DataFrame(movies_data)

# User's preferences
user_preferences = {'Action': 1, 'Comedy': 0, 'Adventure': 1, 'Drama': 0}

# Transforming genres into a TF-IDF matrix
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['Genres'])

# Calculating cosine similarity between movies
cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to get movie recommendations based on user preferences
def get_recommendations(user_preferences, cosine_similarities, movie_titles):
    recommendations = []

    for idx, title in enumerate(movie_titles):
        similarity_score = 0

        # Calculate the weighted sum of similarity scores based on user preferences
        for genre, preference in user_preferences.items():
            genre_idx = tfidf_vectorizer.vocabulary_.get(genre.lower(), -1)
            if genre_idx != -1:
                similarity_score += cosine_similarities[idx, genre_idx] * preference

        recommendations.append((title, similarity_score))

    # Sort recommendations by similarity score in descending order
    recommendations.sort(key=lambda x: x[1], reverse=True)

    return recommendations

# Get movie recommendations for the user
movie_titles = movies_df['Title']
recommendations = get_recommendations(user_preferences, cosine_similarities, movie_titles)

# Display top 3 recommendations
print("Top 3 Movie Recommendations:")
for title, score in recommendations[:3]:
    print(f"{title} - Similarity Score: {score}")
