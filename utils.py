import os
def unique(list1):
    list_set = set(list1)
    unique_list = list(list_set)
    return unique_list

def uniqueAddress(addressList):
    return unique(addressList)

def convert_bytes(size):
    """ Convert bytes to KB, or MB or GB"""
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.2f %s" % (size, x)
#             return size
        size /= 1024.0

def create_folder(folder_name):
    temp_dir = folder_name
    check = os.path.isdir(temp_dir)

    if not check:
        os.makedirs(temp_dir)
    # else:
        # os.system(f"rm -rf {temp_dir}")
        # os.makedirs(temp_dir)

def decimalCount(result):
    final = {}
    for i in result:
#         print(i, result[i])
        temp_sum = sum(result[i])
        final[i] = temp_sum
    return final

def returnSum(dict):
    return sum(dict.values())