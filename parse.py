from collections import Counter
from utils import create_folder, uniqueAddress
import pandas as pd

def parse(input_path, input_interval):
    """ Take all addresses every interval seconds 

    Input: file directory, interval
    Output: list of dictionary per interval seconds
    
    """
    # timestamp
    time = [0,0]

    # save addresses
    readWrite = []
    read = []
    write = []

    allRead = []
    allWrite = []
    allReadWrite = []

    allRead2 = []
    allWrite2 = []
    allReadWrite2 = []

    # count_read_write = []

    # save results and reset
    resultRead = []
    resultWrite = []
    resultReadWrite = []

    totalReset = 0

    # amountRead=0
    # amountWrite=0

    interval = int(input_interval)
    checkInterval = 0

    with open(input_path, "r") as f:
        stop = 0
        while True:
            line = f.readline().strip()
            # print(line)

            # isCore = (line[0] == "c")
            try:
                isExit = (line[0] == "e")
                isTimestamp = (line[0] == "t")
                isRead = (line[0] == "r")
                isWrite = (line[0] == "w")
                
                if (isTimestamp):
                    timestamp = int(line.split(" ")[1])
                    
                    # count time difference
                    time[1] = timestamp
                    dif = (time[1] - time[0]) / 1000000

                    if (time[0] != 0):
                        checkInterval += dif
                        
                        if (checkInterval >= interval):
                            resultRead.append(Counter(read))
                            resultWrite.append(Counter(write))
                            resultReadWrite.append(Counter(readWrite))

                            read = []
                            write = []
                            readWrite = []

                            checkInterval = 0
                            totalReset += 1
                        else:
                            pass

                    time[0] = time[1]

                if (isExit):
                    resultRead.append(Counter(read))
                    resultWrite.append(Counter(write))
                    resultReadWrite.append(Counter(readWrite))

                    read = []
                    write = []
                    readWrite = []

                    checkInterval = 0
                    totalReset += 1

                if (isRead or isWrite):
                    address = line.split(" ")[2]
                    address = int(address, 16)
                    # decimal = int(address, 16)
                    # print(address)
                    readWrite.append(address)
                    allReadWrite.append(address)
                    # allReadWrite2.append(decimal)
                    
                    if (isRead):
                        read.append(address)
                        allRead.append(address)
                        # allRead2.append(decimal)


                    elif (isWrite):
                        write.append(address)
                        allWrite.append(address)
                        # allWrite2.append(decimal)

            except:
                print(line)
                pass
            # if stop == 100:
            #     break
            if not line:
                break

    # print(len(resultRead))
    # print(len(resultWrite))
    # print(len(resultReadWrite))
    # print(resultRead)
    # print(resultWrite)
    # print(resultReadWrite)

    uniqueRead = uniqueAddress(allRead)
    uniqueWrite = uniqueAddress(allWrite)
    uniqueReadWrite = uniqueAddress(allReadWrite)

    # uniqueRead2 = uniqueAddress(allRead2)
    # uniqueWrite2 = uniqueAddress(allWrite2)
    # uniqueReadWrite2 = uniqueAddress(allReadWrite2)

    
    
    print(input_path)
    new_path = input_path.split("/")[1] # remove the first /
    new_path = ".".join(new_path.split(".")[0:-3]) # remove {type}.edit.txt
    print(new_path)
    folder = f"pickles/{new_path}"
    create_folder(folder)

    pd.to_pickle(resultRead, f"{folder}/{new_path}.parse.read.pickle")
    pd.to_pickle(resultWrite, f"{folder}/{new_path}.parse.write.pickle")
    pd.to_pickle(resultReadWrite, f"{folder}/{new_path}.parse.readwrite.pickle")

    pd.to_pickle(uniqueRead, f"{folder}/{new_path}.unique.read.pickle")
    pd.to_pickle(uniqueWrite, f"{folder}/{new_path}.unique.write.pickle")
    pd.to_pickle(uniqueReadWrite, f"{folder}/{new_path}.unique.readwrite.pickle")

    return resultRead, resultWrite, resultReadWrite, uniqueRead, uniqueWrite, uniqueReadWrite, new_path