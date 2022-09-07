def prepareDictionary():
    # read file txt -> lines
    file = open('words.txt', 'r')
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    # convert into dict - key str - value list of strings
    myDict = {}
    for l in lines:
        tempList = l.split("\t")
        key = tempList[0]
        values = tempList[1].split(',')
        myDict[key] = values
    return myDict

# md = prepareDictionary()

# try to choose question list as a sample from whole list
# does random sample work for dictionary?
# another option - full test - random shuffle

# add a prononunciation - wave files opened with playsound



