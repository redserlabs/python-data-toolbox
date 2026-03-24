def player_summary(name, goals, assists):
    print(f"{name} has {goals} goals and {assists} assists.")


def movie_summary(title, year):
    print(f"{title} was released in {year}.")


def total_points(points_list):
    total = 0
    for points in points_list:
        total = total + points
    return total


player_summary("Mbappe", 28, 7)
movie_summary("Interstellar", 2014)

game_points = [24, 31, 18, 27]
print(total_points(game_points))