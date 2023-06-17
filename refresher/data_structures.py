class DataStructures:
    def __init__(self):
        pass

    def run(self):
        self.lists()
        self.tuples()
        self.dictionaries()
        self.sets()

    def lists(self):
        # can contain duplicates, different types, and are mutable
        my_list = ['Toby', 'Bear', 3, True, {}]

        my_list.append("David")
        print(f"size of list: {len(my_list)}")

        my_list.remove(3)
        print(f"size of list: {len(my_list)}")

        for item in my_list:
            print(type(item), item)

    def tuples(self):
        # can contain duplicates, different types, but are immutable
        my_tuple = ('David', 5)
        print(my_tuple)

    def dictionaries(self):
        # key value pairs, mutable
        my_info = {'animal': 'racoon', 'age': 27, 'country': 'USA', 'favorite_food': 'tacos'}
        my_info['computer'] = 'macbook air m2'

        my_info.pop("animal")
        print(my_info.get("age"))
        for key, value in my_info.items():
            print(key, value)

    def sets(self):
        # does not allow for duplicate values
        demo_set = {1, 2, 3, 4, 5}
        demo_set.add(8)
        demo_set.remove(3)
        print(demo_set)
        demo_set.clear()
        print(demo_set)
