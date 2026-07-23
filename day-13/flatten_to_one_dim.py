#Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)  #[1, 2, 3, 4, 5, 6, 7, 8, 9]
