playerRoster = dict()
myNum = 1

try:
    while myNum <= 5:
        jersey = input("Enter player %d's jersey number:\n" % myNum)
        rating = input("Enter player %d's rating:\n" % myNum)
        print(end='\n')
        myNum += 1
        playerRoster.update({jersey: rating})
finally:
    print('ROSTER')    
    for k in sorted(playerRoster.items()):
        print('Jersey number: ' + k[0] + ',' + ' Rating:' + k[1], end='\n') #print('Jersey number: ' + str(k) + ',' + ' Rating:' + str(v), end='\n')