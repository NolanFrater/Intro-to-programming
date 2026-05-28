import csv

#2 points - print the title and rating of the lowest rated movie - done
#2 points - print the title and rating of the highest rated movie - done
#1 point - print the average rating of all movies - done
#1 point - print the move title with the longest name - done
#1 point EXTRA CREDIT - print the longest time between movies in years - done


with open("C:\\Users\\826311\\Documents\\Intro to Programming\\Intro-to-programming\\Assignments\\csv\\deniro.csv", "r") as file:
    table = csv.DictReader(file)
    movie_titles = []
    ratings = []
    total_rating = 0
    release_years = []
    time = 0
    longest_time = 0


    for row in table:
        movie_titles.append(row["Title"])
        ratings.append(float(row["Score"]))
        total_rating += float(row["Score"])
        release_years.append(int(row["Year"]))
        if len(release_years) > 1:
            time = release_years[-1] - release_years[-2]
            if time > longest_time:
                longest_time = time


print("The lowest rated movie is:", movie_titles[ratings.index(min(ratings))], "with a rating of", min(ratings))
print("The highest rated movie is:", movie_titles[ratings.index(max(ratings))], "with a rating of", max(ratings))
print("The average rating of all movies is:", total_rating / len(ratings))
print("The movie with the longest name is:", max(movie_titles, key=len))
print("The longest time between movies is:", longest_time, "years")