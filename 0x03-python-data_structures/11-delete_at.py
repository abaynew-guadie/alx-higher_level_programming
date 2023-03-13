#!/usr/bin/python3
<<<<<<< HEAD

# 11-delete_at.py#
=======
>>>>>>> 98403f72630129e9e00862b8cb62e6b8d3ffe6fc
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        del my_list[idx]
        return my_list
