if __name__ == '__main__':

    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()

    query_name_scores = student_marks[query_name]
    avg_score = sum(query_name_scores) / len(query_name_scores)

    print("%.2f" % avg_score)



