import numpy

with open("D:\\C++\\py_project\\database\\question.txt", mode="r", encoding="utf8") as f:
    qs = f.read().split("\n")

with open("D:\\C++\\py_project\\database\\answer.txt", mode="r", encoding="utf8") as f:
    ans = f.read().split("\n")

def handle_data(text):
    text = text.split(" ")
    ans = []
    print(text)
    for s in qs:
        count = 0
        for i in text:
            if i in s:
                count += 1
        if len(s) == 0:
            ratio = 0
        else:
            ratio = count * 10 / len(s)
        ans.append(ratio)
    print(ans)
    return numpy.argmax(ans)


# index = handle_data("bây giờ bạn bao nhiêu tuổi rồi")
# print(ans[index])
        