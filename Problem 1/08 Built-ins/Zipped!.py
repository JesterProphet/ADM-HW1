n, x = map(int, input().split())

exam_results = []

for _ in range(0, x):
    exam_results.append(list(map(float, input().split())))

exam_list = list(zip(*exam_results))

for exam in exam_list:
    print(sum(exam)/len(exam))
