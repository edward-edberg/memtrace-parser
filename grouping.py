import numpy as np

def grouping(result):
    group = {}
    size_group = ""
    biggest_decimal = []
    for i in result:
        # print(i, type(i), len(i))
        # decimal = i
        # decimal = i
        length = len(str(i))
        biggest_decimal.append(int(length))

    max_length = max(biggest_decimal)
    if max_length > 12:
        size_group = "TB"

    elif max_length > 9:
        size_group = "GB"

    elif max_length > 6:
        size_group = "MB"

    elif max_length > 3:
        size_group = "KB"

    elif max_length >= 0:
        size_group = "B"

    # print(size_group)

    stop = 0
    for i in result:
        decimal = i
        length = len(str(i))
        if (size_group == "TB"):
            convert_size = decimal / 1024 / 1024 / 1024 / 1024
        elif (size_group == "GB"):
            convert_size = decimal / 1024 / 1024 / 1024
        elif (size_group == "MB"):
            convert_size = decimal / 1024 / 1024
        elif (size_group == "KB"):
            convert_size = decimal / 1024
        elif (size_group == "B"):
            convert_size = decimal
        final_size = round(convert_size, 1) # 1 decimal
        final_size = round(convert_size) # 0 decimal
#         print(f"{i} {decimal} {final_size} {size_group} {type(final_size)} {resultConvertMemoryRead[i]} {type(resultConvertMemoryRead[i])}")
        temp = np.array(result[i])
    #     print(temp, type(temp))
        if final_size in group:
            group[final_size] += temp
        else:
            group[final_size] = temp

    # folder = f"pickles/{filename}"
    # create_folder(folder)

    # pd.to_pickle(group, f"{folder}/{filename}.group.{count_type}.pickle")
    # pd.to_pickle(size_group, f"{folder}/{filename}.size_group.{count_type}.pickle")
    print(size_group ,group)
    return size_group, group