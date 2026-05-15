from flask import Flask, render_template, request
import pickle
import requests

app = Flask(__name__)


#  FIX: Make the Python 'zip' function available as a Jinja filter

app.jinja_env.filters['zip'] = zip


# Load Data

movies = pickle.load(open('models/movie_list.pkl', 'rb'))
similarity = pickle.load(open('models/similarity.pkl', 'rb'))



# Fetch movie poster

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        # Fallback for movies without a poster
        full_path = "https://via.placeholder.com/500x750?text=No+Poster+Available"
    return full_path



# Recommendation Logic

def recommend(movie):
    # Ensure movie is found before trying to access index
    if movie not in movies['title'].values:
        return [], []

    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_names = []
    recommended_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_names.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_names, recommended_posters


# Flask Routes

@app.route('/', methods=['GET', 'POST'])
def home():
    movie_list = movies['title'].values
    selected_movie = None
    names = []
    posters = []
    show_results = False

    if request.method == 'POST':
        selected_movie = request.form.get('movie')
        if selected_movie:
            names, posters = recommend(selected_movie)
            show_results = True

    # Render template for both GET and POST
    return render_template(
        'index.html',
        movie_list=movie_list,
        selected_movie=selected_movie,
        recommended_names=names,
        recommended_posters=posters,
        show_results=show_results
    )


# Run Flask

if __name__ == '__main__':
    app.run(debug=True)

