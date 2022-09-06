class SmallestNumber:
    @staticmethod
    def smallest_number_in_list():
        list = [11, 23, 9, 3, 99, 17]
        min = list[0]
        for i in range(0, len(list)):
            if (list[i] < min):
                min = list[i]
        print("Smallest number in the list is: " + str(min))

    @staticmethod
    def largest_number_in_list():
        list = [10, 20, 3, 19, 45, 99, 200]
        max = list[0]
        for i in list:
            if i > max:
                max = i
        print("Largest number in the list is: " + str(max))


x = SmallestNumber.smallest_number_in_list()
z = SmallestNumber.largest_number_in_list()
