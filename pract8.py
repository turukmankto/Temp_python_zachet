def main(s):
    res = {}
    s = s.replace("\n", " ")
    s = s.replace("<%", " ")
    s = s.replace("%>", " ")
    s = s.replace("(", " ")
    s = s.replace(")", " ")
    s = s.replace("<=", " ")
    s = s.replace(".", " ")
    s = s.split(' ')
    try:
        while True:
            s.remove("")
    except ValueError:
        pass
    for i in range(len(s) - 1):
        if s[i] == "variable":
            key = s[i + 1]
            value = s[i + 2]
            res[key] = value
    return res


print(main("((<% variable biqu <= laoned_507. %>, <% variable inbe<=edti. %>,<%\nvariable inteen <= raen_166. %>,))"))
