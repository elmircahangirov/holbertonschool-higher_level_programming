#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element in a list at a specific position without modifying the original list."""
    # Orijinal list-in surətini yaradırıq
    new_list = my_list.copy()
    # Əgər index düzgündürsə, element-i dəyişirik
    if idx >= 0 and idx < len(my_list):
        new_list[idx] = element
    return new_list
