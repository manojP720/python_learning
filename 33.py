def top_words():
    file = open ("sample.txt","r")
    text = file.read().lower()
    file.close()


    words = text.split()
    freq = {}
    for w in words:
        if w in freq:
            freq [w] += 1
        else:
            freq = 1
    items = list(freq.items())            

