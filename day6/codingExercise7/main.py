if __name__ == '__main__':
    filenames = ['a.txt', 'b.txt', 'c.txt']
    for filename in filenames:
        file = open(filename, 'r')
        txt = file.read()
        file.close()
        print(txt)
