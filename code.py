# --------------
from csv import reader


# Read the data file and store it as a list 'movies'
opened_file = open(path, encoding="utf8")
read_file = reader(opened_file)
movies = list(read_file)



# The first row is header. Extract and store it in 'movies_header'.
movie = movies
movies_header = movies.pop(0)
movie.pop(0)
# Subset the movies dataset such that the header is removed from the list and store it back in movies




# Delete wrong data

# Explore the row #4553. You will see that as apart from the id, description, status and title, no other information is available.
# Hence drop this row.
del movie[4553]


# Using explore_data() with appropriate parameters, view the details of the first 5 movies.
def explore_data(x):
    for index, item in enumerate(x):
        if index < 5:
            print(item) 
explore_data(movie)



# Our dataset might have more than one entry for a movie. Call duplicate_and_unique_movies() with index of the name to check the same.
duplicate_and_unique_movies = []
for index in range(len(movie)):
    duplicate_and_unique_movies.append(movie[index][13])
print(duplicate_and_unique_movies)



# We saw that there are 3 movies for which the there are multiple entries. 
# Create a dictionary, 'reviews_max' that will have the name of the movie as key, and the maximum number of reviews as values.
reviews_max = dict()
for index in range(len(movie)):
    title = movie[index][13]
    review = len(movie[index][4])
    reviews_max[title] = review
    print(title,':',review)


# Create a list 'movies_clean', which will filter out the duplicate movies and contain the rows with maximum number of reviews for duplicate movies, as stored in 'review_max'. 
movies_clean = []
duplicate = []
for index in range(len(movie)):
    if (movie[index][13]) not in duplicate:
        duplicate.append(movie[index][13])
    elif (movie[index][13]) in duplicate:
        movies_clean.append(movie[index][13])
for i in movies_clean:
    print(i,':',reviews_max.get(i))



# Calling movies_lang(), extract all the english movies and store it in movies_en.
def movies_lang(x):
    movies_en = []
    for index in range(len(x)):
        if 'en' in x[index]:
            movies_en.append(x[index][13])
    return movies_en
movies_lang(movie)



# Call the rate_bucket function to see the movies with rating higher than 8.
high_rated_movies = []
def rate_bucket(x):
    
    for index in range(len(x)):
        if 'en' in x[index]:
            b = int(float(x[index][11]))
            if b >= 8:
                high_rated_movies.append(x[index][13])
    print(high_rated_movies)
rate_bucket(movie)


