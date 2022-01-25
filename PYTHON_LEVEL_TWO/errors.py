try:
    f = open('simple.txt','w')
    f.write("Test Write to simple text !")
except IOError:
    print('ERROR: Could not find file or read data!')
else:
    print("Success!")
    f.close()