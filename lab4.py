def top_words():
    file = open("sample.txt","r")
    text = file.read().lower()
    file.close()

    words = text.split()
    freq = {}

    for w in words:
        for i in range
    