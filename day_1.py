import pandas as pd

file_path = 'Book1.xlsx'  
df = pd.read_excel(file_path, engine='openpyxl') 

sorted_df = df.apply(lambda col: col.sort_values().reset_index(drop=True))

sorted_df['Difference'] = abs(sorted_df['List_1'] - sorted_df['List_2'])

print(sorted_df.head())

sum_difference = sorted_df['Difference'].sum()

print(sum_difference)

list_1 = sorted_df['List_1'].tolist()
list_2 = sorted_df['List_2'].tolist()

def find_occurances(arr, target):

    def binary_search(arr, target): #returns the index of the match
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid  
            elif arr[mid] < target:
                low = mid + 1  
            else:
                high = mid - 1  
                
        return -1  
    
    index = binary_search(arr, target)
    if index == -1:
        return 0
    occurrences = []
    
    # Check to the left
    left = index
    while left >= 0 and arr[left] == target:
        occurrences.append(left)
        left -= 1

    # Check to the right
    right = index + 1
    while right < len(arr) and arr[right] == target:
        occurrences.append(right)
        right += 1

    return len(occurrences)

result = []
for i in list_1:
    appears = find_occurances(list_2, i)
    number = i * appears
    result.append(number)


print(sum(result))
