fw = open('sample.txt', 'w')
fw.write('content inside sample text\n')
fw.write('start learning\n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()

