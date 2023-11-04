# Binary Search
# Used in sorted list
# Works by checking the middle value with target value
# if target equals middle search ends,
# if target greater than middle. middle becomes the new start values before middle are removed,
# if target lesser than middle. middle becomes the new end, values after the middle are removed,
# if the target is not present in the list it delivers the list is absent.

def binary_search(list_of_ele, target_value):

    start_value = 0
    middle_value = 0
    end_value = len(list_of_ele)
    steps_taken = 0

    while (start_value <= end_value):
        print("step: ", steps_taken+1, ": ",
              list_of_ele[start_value:end_value+1])

        steps_taken += 1
        middle_value = (start_value + end_value) // 2
        print("middle value : ", middle_value)

        if target_value == list_of_ele[middle_value]:
            print(middle_value)
            return middle_value
        if target_value < list_of_ele[middle_value]:
            end_value = middle_value - 1
        else:
            start_value = middle_value + 1

    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
target = int(input("choose a number between 1-12: "))
name_list = ["Aron", "Bevin", "Cyril", "Derrick", "Elbin", "Faizal",
             "Geoffery", "Hebron", "Jason", "Kevin", "Lenord", "Mario"]

names = name_list[binary_search(my_list, target)]

print("The Searched names : ", names)
