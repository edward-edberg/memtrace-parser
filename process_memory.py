from utils import decimalCount, returnSum, create_folder
import pandas as pd


def process_memory(parse_result, unique, count_type, filename):
    pages = len(parse_result) 

    dictionary = {}
    for item in unique:
        dictionary[item] = [0 for x in range(pages)]
    
    # print(len(unique), len(parse_result))
    # print(dictionary, len(dictionary))

    # total = 0
    for x in range(pages): # interval loop
        temp_dict = {}
        for idx, i in enumerate(parse_result[x]): # address loop
            temp_result = parse_result[x][i]
            # print(temp_result, i)

            if i in temp_dict:
                temp_dict[i].append(temp_result)
            else:
                temp_dict[i] = [temp_result]

        tempCount = decimalCount(temp_dict)
        # sumCount = returnSum(tempCount)
        # total += sumCount
        
        # print(len(tempCount), tempCount)

        for idx, i in enumerate(tempCount):
            dictionary[i][x] = tempCount[i]
    
    # print(dictionary)
    # print(total)
    folder = f"pickles/{filename}"
    create_folder(folder)

    pd.to_pickle(dictionary, f"{folder}/{filename}.memory.{count_type}.pickle")
    return dictionary