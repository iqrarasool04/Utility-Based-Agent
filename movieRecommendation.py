def UtilityBasedAgent(genre,ratings,availability):
    movie_data = {
        "Movie1": {
            "Genre": ["Action", "Adventure", "Sci-Fi"],
            "Rating": 8.5,
            "Availability": "Netflix",
        },
        "Movie2": {
            "Genre": ["Drama", "Romance"],
            "Rating": 7.9,
            "Availability": "Amazon Prime",
        },
        "Movie3": {
            "Genre": ["Comedy"],
            "Rating": 6.8,
            "Availability": "Hulu",
        },
        "Movie4": {
            "Genre": ["Action", "Thriller"],
            "Rating": 9.1,
            "Availability": "Netflix",
        },
        "Movie5": {
            "Genre": ["Animation", "Family"],
            "Rating": 8.0,
            "Availability": "Disney+",
        },
        "Movie6": {
            "Genre": ["Horror", "Mystery"],
            "Rating": 7.2,
            "Availability": "Amazon Prime",
        }
    }
    RecommendedMovies = []

    for movie,details in movie_data.items():
        if movie in movie and (genre in [genre for genre in details['Genre']] and details['Rating']>=ratings and availability in details['Availability']):
            RecommendedMovies.append(movie)
    
    if RecommendedMovies:
        print("Recommended movies based on your preferences:")
        for recommended_movie in RecommendedMovies:
            print(recommended_movie)
    else:
        print("No matching movies found in the database for your preferences.")


print("This is simple Movie Recommendation, a problem scenario for Utility Based Agent")
genre = input("Enter genre preference: ")
ratings = float(input("Enter ratings preference: "))
availability = input("Enter availability preference: ")
UtilityBasedAgent(genre,ratings,availability)
print("Agent has completed its task")