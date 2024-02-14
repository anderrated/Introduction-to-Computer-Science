# Author : Andrea Laserna
# Created on January 7, 2023
# Modified on January 31, 2024

'''
Using the same pre-defined list in Exercise 1, ask the user to choose a sorting algorithm and perform
only that specific algorithm (Selection, Insertion, or Merge). 
'''

def main():
    #code_list = [4599, 3102, 1024, 9980, 2912, 1569, 4205, 9811, 1001, 7638, 4733, 1989, 5555, 5000, 3861]
    code_list = [2, 8, 5, 3, 9, 4, 1]

    choice = int(input("Choose your sorting algorithm (1-3): "))

    if choice == 1:
        print("Sorting with Selection Sort...")
        selection_sort(code_list)
        print(code_list) 

    elif choice == 2:
        print("Sorting with Insertion Sort...")
        insertion_sort(code_list)
        print(code_list)

    elif choice == 3:
        print("Sorting with Merge Sort...")
        merge_sort(code_list)
        
    else:
        print("Invalid choice.")

def selection_sort(code_list):
    for i in range(0, len(code_list)):
        current_min_index = i
        for j in range(i+1, len(code_list)):
            if code_list[j] < code_list[current_min_index]:
                current_min_index = j
        
        code_list[current_min_index], code_list[i] = code_list[i], code_list[current_min_index]

def insertion_sort(code_list):
    for i in range(0, len(code_list)):
        for j in range(i, 0, -1):
            if code_list[j] < code_list[j-1]:
                code_list[j], code_list[j-1] = code_list[j-1], code_list[j]
            
def merge_sort(code_list):
    if len(code_list) > 1:
        mid = len(code_list) // 2
        left_list = code_list[:mid]
        right_list = code_list[mid:]
    
        merge_sort(left_list)
        merge_sort(right_list)

        

    
main()
            
            
            
        