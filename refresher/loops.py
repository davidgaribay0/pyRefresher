class Loops:
    def __init__(self):
        self.name = 'David Garibay'
        pass

    def run(self):
        for i in range(1, 5):
            print(i)

        for i in ['david', 'maldonado', 'garibay']:
            print(i)

        for index, fruits in enumerate(['bannanas', 'pineapples', 'strawberries']):
            print(index, fruits)

        count = 0

        while count <= 10:
            print(count)
            count = count + 1


