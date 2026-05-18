
possible_genres = ['Comedy', 'Horror', 'Drama', 'Action']

sum_of_ratings = 0
for i in range(2):
    movie_name = input("Movie name: ")
    movie_genre = input("Movie genre: ")
    if movie_genre not in possible_genres:
        print("Please choose another genre. Defaulting to Action.")
        movie_genre = "Action"
    movie_rating = input("How much do you like this movie (1-5): ")
    if movie_rating.isdigit() == False:
        # this happens when the input is not a number
        print("Please enter a digit. For example 5. Defaulting to 1.")
        movie_rating = 1
    else:
        movie_rating = int(movie_rating)
    sum_of_ratings += movie_rating

print(sum_of_ratings/2)


