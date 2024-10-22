import math

tree_height = 0.0

angle_elev = float(input())
shadow_len = float(input())

''' Your solution goes here '''
tree_height = math.tan(angle_elev) * shadow_len

print('Tree height:', tree_height)
