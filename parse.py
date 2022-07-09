def parse(input_path, input_interval):
    # timestamp
    time = [0,0]

    # save addresses
    readWrite = []
    read = []
    write = []

    allRead = []
    allWrite = []
    allReadWrite = []

    count_read_write = []

    # save results and reset
    resultRead = []
    resultWrite = []
    resultReadWrite = []

    totalReset = 0

    amountRead=0
    amountWrite=0

    interval = int(input_interval)
    checkInterval = 0

    