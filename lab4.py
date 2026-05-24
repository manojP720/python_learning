def top_words():
    file = open("sample.txt","r")
    text = file.read().lower()
    file.close()

    words = text.split()
    freq = {}

    for w in words:
        if w in freq :
            freq[w] += 1
        else:
            freq[w] = 1

    items = list(freq.items()) 

    for i in range(len(items)):
        for j in range(i + 1,len(items)):
                   
    