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



    for i in range (len(items)):
        for j in range(i+1,len(items)):
            if items[i][j] < items[j][i]:
                temp = items[i]
                items[i] = items[j]
                items[j] = temp

    print ("Top 10 words !")
    for i in range (min(10,len(items))):
        print(items[1][0],":",items[i][j]) 

    top_words()


    
                   
