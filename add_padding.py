import numpy as np
import math

def add_padding(group):
    # take sample array
    keys=list(group.keys())
    # print(keys[0])
    # print(group[keys[0]])
    
    # take num array 
    num_array = len(group[keys[0]])
    # print(num_array)
    
    # max y limit
    max_keys = max(list(group.keys()))
    # print(math.ceil(max_keys))
    
    # create step 0.1 
#     all_step = np.arange(-5.0, math.ceil(max_keys)+5.0, 0.1)
    # increase the top
    temp = math.ceil(max_keys)
    condition = True
    while (condition):
        mod = temp % 10
        if mod == 0:
            condition = False
        else:
            temp += 1
    
    all_step = np.arange(0, temp, 1)
#     print(all_step)
    final_step = []
    for i in all_step:
#         temp = round(i,1)
        temp = round(i)
        final_step.append(temp)
#         print(temp)
#     print(final_step)
    
    # start padding
    for i in final_step:
        if i in group:
#             print("yes", i)
            group[i] = list(group[i])
            continue
        else:
    #         print("no", i)
            array = [0 for x in range(num_array)]
            group[i] = np.array(array)
    # print(group)

    return group

