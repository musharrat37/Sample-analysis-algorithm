location of project C:\Users\User\PycharmProjects\testingML

file CSVTest.py

import csv
import math as m
from PIL import Image


def range_search(sorted_test_arr, start, end, wave_input):
    if end < start:
        print("wave input out of range", end, start)
        return -1
    else:
        mid = int(start + (end - start) / 2)
        print(mid)
        if sorted_test_arr[mid] == wave_input:
            print("Found exact match")
            return mid
        elif sorted_test_arr[mid] < wave_input:
            print(sorted_test_arr[mid], wave_input)
            if wave_input_f < sorted_test_arr[mid] < wave_input:
                print("entering 1")
                i = -2
                while sorted_test_arr[mid + i] <= wave_input_c and (mid + i) < len(sorted_test_arr) - 1:
                    range_test_arr.insert(i, float(sorted_test_arr[mid + 1 + i]))
                    i += 1
                return range_test_arr
            else:
                print("entering 2")
                range_search(sorted_test_arr, (mid + 1), end, wave_input)
        else:
            print(sorted_test_arr[mid], wave_input)
            if wave_input_c > sorted_test_arr[mid] > wave_input:
                print("entering 3")
                i = -1
                while sorted_test_arr[mid - i] >= wave_input_f and (mid - i) >= 0:
                    range_test_arr.insert(i, float(sorted_test_arr[mid - i]))
                    print(range_test_arr[i])
                    i += 1
                return range_test_arr
            else:
                print("entering 4")
                range_search(sorted_test_arr, start, (mid - 1), wave_input)


with open('Final DB.txt', 'r') as csv_file:
    wave_data = list(csv.reader(csv_file, delimiter='\t'))
    print(wave_data[:1])

first_column = list([float(item[0]) for item in wave_data[1:]])
element_column = [item[2] for item in wave_data[1:]]
ion_column = [item[3] for item in wave_data[1:]]
intensity_column = [item[1] for item in wave_data[1:]]
# print(len(first_column))

'''wave_data = np.genfromtxt("test csv.txt", delimiter="\t",skip_header=1)
print(wave_data)'''

sorted_test_arr = first_column

'''for i in sorted_test_arr:
    print(i)'''
wave_input = float(input("Enter the recorded wavelength: "))
print("You've entered ", wave_input)

wave_input_f = float(m.floor(wave_input) - 1)
wave_input_c = float(m.ceil(wave_input) + 1)
print(wave_input_f, wave_input_c)
range_test_arr = []

result = range_search(sorted_test_arr, 0, len(sorted_test_arr) - 1, wave_input)
print(result)

for i in range_test_arr:
    print(i, element_column[first_column.index(i)], ion_column[first_column.index(i)], intensity_column[first_column.index(i)])

first_distance = wave_input
probable_result = 0
second_distance = 0
#second_probable = 0

if len(range_test_arr) == 0:
    print(sorted_test_arr[result], " is the most probable element")
    if abs(wave_input - sorted_test_arr[result + 1]) < abs(wave_input - sorted_test_arr[result - 1]):
        print(sorted_test_arr[result + 1], " is the second probable element")
    else:
        print(sorted_test_arr[result - 1], " is the second probable element")
else:
    for i in range_test_arr:
        if abs(wave_input - i) < first_distance:
            second_distance = probable_result
            first_distance = abs(wave_input - i)
            probable_result = i
    print(probable_result," - ",element_column[first_column.index(probable_result)], end=' ')
    print(ion_column[first_column.index(probable_result)], " is the most probable element")
    if second_distance == 0:
        temp_range_arr = list(range_test_arr)
        temp_range_arr.remove(probable_result)
        second_distance = wave_input
        for i in temp_range_arr:
            if abs(wave_input - i) < second_distance:
                second_distance = abs(wave_input - i)
                second_probable = i
        print(second_probable," - ",element_column[first_column.index(second_probable)], end=' ')
        print(ion_column[first_column.index(second_probable)], "is the second probable element")
    else:
        print(second_distance, " - ", element_column[first_column.index(second_distance)], end=' ')
        print(ion_column[first_column.index(second_distance)], "is the second probable element")


image = Image.open('images.png')
image.show()


