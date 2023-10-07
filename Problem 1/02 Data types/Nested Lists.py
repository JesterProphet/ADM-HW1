if __name__ == '__main__':

    data = []
    scores = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([name, score])
        scores.append(score)

    runners_up_score = sorted(set(scores))[1]

    for name, score in sorted(data):
        if score == runners_up_score:
            print(name)
