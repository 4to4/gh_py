f = open('d:/dev/arena_assignment/Artist_lists_small.txt', 'rb')

masterDict = {}
count = 1
for line in f:
    for artist in line.split(','):
        if not artist in masterDict.keys():
            masterDict[artist] = []
            masterDict[artist].append(count)
        else:
            masterDict[artist].append(count)
    count += 1

newDict = {}
for key in masterDict.keys():
    if len(masterDict[key]) >= 50:
        newDict[key] = masterDict[key]

#print len(masterDict)
#print len(newDict)

totalCount = 0
finalList = []
for key1 in newDict.keys():
    for key2 in newDict.keys():
        count = 0
        if key1 == key2:
            continue
        for number in newDict[key1]:
            if number in newDict[key2]:
                count += 1
        if count >= 50:
            if key2 + '-' + key1 in finalList:
                continue
            finalList.append(key1 + '-' + key2)
            totalCount += 1

print (finalList)
print (totalCount)