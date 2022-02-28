groups=int(input("Please enter number of groups: "))
for i in range(0, groups):
    list_of_tweets=[]
    elements = int(input("Enter number of elements in groups: "))
    for i in range(0, elements):
        data=(input(f"Enter {i+1} name and tweet id: "))
        list_of_tweets.append(data)
        split_input= []
        d={}
    for i in range (len(list_of_tweets)):
                splitted = list_of_tweets[i].split(" ", 2)
                if splitted[0] in d:
                    d[splitted[0]]+= 1
                else:
                    d[splitted[0]] = 1
    max_value = max(d.values())
    final_keys=[i for i,j in d.items() if j == max_value]
    final_keys.sort()
    max_value = max(d.values())
    final_values=[]
    final_values.append(max_value)
    for i in range(len(final_keys)):
        print(final_keys[i], final_values[0])
