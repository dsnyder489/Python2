def listsearch(searchlist):
    csvopen = open('methodlist.csv')
    csvlist = list(csvopen)
    listcount = csvlist.count(searchlist)
    return int(listcount)


print(listsearch('taco'))
