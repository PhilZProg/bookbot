def wc(text):
    return len(text.split())


def cc(text):
    counter = {}
    for c in text.lower():
        if c not in counter:
            counter[c] = 0
        counter[c] += 1
    return counter


def sort_on(item):
    return item["num"]


def convert(dict):
    l = []
    for k in dict:
        l.append({"char": k, "num": dict[k]})
    l.sort(reverse=True, key=sort_on)
    return l
