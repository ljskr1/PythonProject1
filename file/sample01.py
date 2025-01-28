# open file for read
file = open ('/Users/lijah/PycharmProjects/DSML-DTC/file/data/sample01.csv', 'r')


#file.seek(0) #this makes the cursor go first 0 line

print(file.readlines())




file.close()

