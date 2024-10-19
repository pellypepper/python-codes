def merge_sort(items):

    items_length = len(items)

    # Create temporary storage for merging
    temporary_storage = [None] * items_length

    # Initialize the size of subsections to 1
    size_of_subsections = 1

    # Iterate until the size of subsections is less than the length of the list
    while size_of_subsections < items_length:

    
        for i in range(0, items_length, size_of_subsections * 2):

            # Determine the start and end indices of the two subsections to merge
            first_section_start, first_section_end = i, min(i + size_of_subsections, items_length)
            second_section_start, second_section_end = first_section_end, min(first_section_end + size_of_subsections, items_length)

        
            sections = (first_section_start, first_section_end), (second_section_start, second_section_end)

            # Call the merge function to merge the subsections
            merge(items, sections, temporary_storage)

 
        size_of_subsections *= 2


    return items

def merge(items, sections, temporary_storage):
  
    (first_section_start, first_section_end), (second_section_start, second_section_end) = sections

    # Initialize indices for the two sections and temporary storage
    left_index = first_section_start
    right_index = second_section_start
    temp_index = 0


    while left_index < first_section_end or right_index < second_section_end:
      
        if left_index < first_section_end and right_index < second_section_end:
            
            # Compare lengths of the strings to sort by length from longest to shortest
            if len(items[left_index]) > len(items[right_index]):
                # Place the longer element into temporary storage
                temporary_storage[temp_index] = items[left_index]
                left_index += 1
            else:
                temporary_storage[temp_index] = items[right_index]
                right_index += 1
        # If only section 1 has elements left to merge
        elif left_index < first_section_end:
            temporary_storage[temp_index] = items[left_index]
            left_index += 1
        # If only section 2 has elements left to merge
        elif right_index < second_section_end:
            temporary_storage[temp_index] = items[right_index]
            right_index += 1

        temp_index += 1

    # Copy sorted elements from temporary storage back to the original list
    for i in range(temp_index):
        items[first_section_start + i] = temporary_storage[i]

# Test the modified merge sort on 3 lists of unsorted strings
list1 = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lime"]
list2 = ["zebra", "elephant", "cat", "hippopotamus", "tiger", "antelope", "lion", "koala", "giraffe", "monkey"]
list3 = ["mountain", "river", "sea", "ocean", "valley", "hill", "desert", "lake", "forest", "canyon"]

# Sort the lists by string length from longest to shortest
sorted_list1 = merge_sort(list1)
sorted_list2 = merge_sort(list2)
sorted_list3 = merge_sort(list3)

# Output the sorted lists
print("Sorted List 1:", sorted_list1)
print("Sorted List 2:", sorted_list2)
print("Sorted List 3:", sorted_list3)
