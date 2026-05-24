with open("./files/Jabberwocky.txt", "r", encoding="utf-8") as jabber:
        for line in jabber:
            print(line.rstrip())