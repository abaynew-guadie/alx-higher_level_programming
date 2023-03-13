#!/usr/bin/python3
def element_at(my_list, idx):
<<<<<<< HEAD

 """Retrive an element from a list."""

   if idx < 0 or idx > (len(my_list) - 1):
       return None
    return (my_list[idx])
=======
    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    return my_list[idx]
>>>>>>> 98403f72630129e9e00862b8cb62e6b8d3ffe6fc
