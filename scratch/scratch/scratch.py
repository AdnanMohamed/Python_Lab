def schoty(frame):
    number=0
    for i in range(len(frame)-1):
        number+=frame[i].find('-')*10*(len(frame)-i)
    return number+frame[-1].find('-')

test=schoty(["---OOOOOOOOOO",
        "---OOOOOOOOOO",
        "---OOOOOOOOOO",
        "OOO---OOOOOOO",
        "O---OOOOOOOOO",
        "OOOOOOOOO---O",
        "OO---OOOOOOOO"])

if __name__ == "__main__":
    print(test)




    



    