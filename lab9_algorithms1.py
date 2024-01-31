# Author : Andrea Laserna
# Created on January 7, 2023
# Modified on January 31, 2024

'''
EXERCISE # 1 - Linear and Binary Search

As a web developer working for a retail store, your job is to create a website where the store can sell its 
products online. Your first task is to create a search option for the customers, so they can easily find 
specific items they are looking for in your shop. 

Each item in your shop corresponds to a specific 4-digit code. Starting with a pre-defined list, perform
both searching algorithms (Linear and Binary) to find your items. Ask the user to input an item
(using a number code) and your program should output if the code was able to find your item in the list.

The predefined list should contain the following values in this order:
4599, 3102, 1024, 9980, 2912, 1569, 4205, 9811, 1001, 7638, 4733, 1989, 5555, 5000, 3861
'''

code_list = [4599, 3102, 1024, 9980, 2912, 1569, 4205, 9811, 1001, 7638, 4733, 1989, 5555, 5000, 3861]

def main():
    code = int(input("Enter a 4-digit code: "))
    print("=== LINEAR SEARCH ===")
    linear_search(code_list, code)

    print("\n=== BINARY SEARCH ===")
    sorted_list = sorted(code_list)
    #print(sorted_list)

    index = binary_search(sorted_list, code, start_index = 0, end_index = len(sorted_list) - 1)
    
    if (index!= False):
        print(f"Item found at index {index}.")
    else:
        print("Item not found.")

def linear_search(code_list, code):
    
    for i in range(0, len(code_list)):
        if code_list[i] == code:
           print(f"Item found at index {i}.")
           return
    print("Item not found.")

def binary_search(sorted_list, code, start_index, end_index):

    if (start_index > end_index):
        return False

    mid_index = (start_index + end_index) // 2 

    if (code < sorted_list[mid_index]):
        return binary_search(sorted_list, code, start_index , mid_index-1)
    elif (code > sorted_list[mid_index]):
        return binary_search(sorted_list, code, mid_index+1, end_index)
    else:
        return mid_index

main()