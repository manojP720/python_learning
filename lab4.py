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
            if items[i][1] < items[j][1]:
                temp = items[i]
                items[i] = items[j]
                items[j] = temp

    print("top 10 words")
    for i in range(min(10,len(items))):
      print(items[i][0] ,":",items[i][1])


top_words()
        