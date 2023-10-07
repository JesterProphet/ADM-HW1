def minion_game(string):

    # Lowercase string
    string = string.lower()

    points_kevin = 0
    points_stuart = 0

    # Calculate points of both players
    for i in range(0, len(string)):
        if string[i] in 'aeiou':
           points_kevin += (len(string)-i)
        else:
           points_stuart += (len(string)-i)

    # Determine winner
    if points_kevin > points_stuart:
        print(f"Kevin {points_kevin}")
    elif points_kevin < points_stuart:
        print(f"Stuart {points_stuart}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)