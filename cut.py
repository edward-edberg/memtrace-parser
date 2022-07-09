from collections import Counter
import argparse
from venv import create
from utils import convert_bytes, create_folder
import os

### TAKING ARGUMENTS
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True,
	help="path of the file")
ap.add_argument("-m", "--mode", required=True, choices=["decimal", "address"],
	help="path of the file")
ap.add_argument("-d", "--dir", required=False, default="/",
	help="path of the file")
args = vars(ap.parse_args())

print(f"--- {os.path.basename(__file__)} ---")
print("Path: {}".format(args["path"]))
print("Type: {}".format(args["mode"]))
print("Directory: {}".format(args["dir"]))
# print("\n")

path = args["path"]

new_path = ".".join(path.split(".")[:-1])
try:
    new_path = new_path.split("/")[1]
except:
    pass
mode=args["mode"]
create_folder(args["dir"])

final_path = f"{new_path}.{mode}.edit.txt"
if args["dir"] == "/":
    final_path = final_path
else:
    final_path = os.path.join(args["dir"], final_path)

g = open(final_path, "w+")
g.write("################################################################################ \n")
g.write("# Notes:\n")
g.write("# t (timestamp) - in microseconds\n")
g.write("# c (core) - core number\n")
g.write("# r (read) - read instruction size in bytes - virtual address converted to decimal\n")
g.write("# w (write) - write instruction size in bytes - virtual address converted to decimal\n")
g.write("# e (exit)\n")
g.write("# i (total instructions) - including read, write, and ifetch (already removed)\n")
g.write("################################################################################ \n")
with open(path) as f:
    stop = 0

    check_bytes = []
    read_size = 0
    write_size = 0

    read_count = 0
    write_count = 0
    
    cores = []
    timestamps = []
    while True:
        line = f.readline().strip()
        isRead = line.__contains__("read")
        isWrite = line.__contains__("write")
        isTimestamp = line.__contains__ ("timestamp")
        isCore = line.__contains__("core")
        isExited = line.__contains__("exited")
        isTotal = line.__contains__("instructions")
        
        if (isExited):
#             print(line)
            g.write(f"e\n")
            pass
        elif (isRead or isWrite):
            # check bytes
            try:
                data = line.split("@")
                temp = data[0].strip().split(" ")
    #             print(data)
                address = data[1].strip().split(" ")[0]
                if mode == "decimal":
                    decimal = int(address,16)
                read_or_write = temp[2]
                size = temp[-2]
                new_size = int(size)
    #             print(size, type(size), new_size, type(new_size))
                size_type = temp[-1]
    #             print(temp[2],temp[-2], address)
#                 print(read_or_write[0], new_size, address )

            except:
                print("error: ", line)
                data = line.split("@")
#                 print(data)
                pass
        
            if read_or_write == "read":
                read_size += new_size
                check_bytes.append(size_type)
                read_count += 1
                if mode == "decimal":
                    g.write(f"{read_or_write[0]} {new_size} {decimal}\n")
                else:
                    g.write(f"{read_or_write[0]} {new_size} {address}\n")

            elif read_or_write == "write":
                write_size += new_size
                check_bytes.append(size_type)      
                write_count += 1                         
                if mode == "decimal":
                    g.write(f"{read_or_write[0]} {new_size} {decimal}\n")
                else:
                    g.write(f"{read_or_write[0]} {new_size} {address}\n")

        elif (isCore):
            core = line.split("core")[1].replace(">","").strip()
            cores.append(core)
#             print("c", core)
            g.write(f"c {core}\n")
        elif (isTimestamp):
            timestamp = line.split("timestamp")[1].replace(">","").strip()
            timestamps.append(timestamp)
#             print("t", timestamp)
            g.write(f"t {timestamp}\n")
#             print(line)
        elif (isTotal):
            total = line.split(":")[0].strip()
#             print(total)
            g.write(f"i {total}\n")


        stop += 1
#         if stop == 100:
#             break
        if not line:
            break
result_bytes = Counter(check_bytes)
print(f"Output Path: {final_path}\n")
print(result_bytes)
print("Read Instruction Size: ", convert_bytes(read_size),read_size)
print("Write Instruction Size: ", convert_bytes(write_size), write_size)

total = read_count + write_count
read_ratio = read_count / total
write_ratio = write_count / total
print("\n")
print(f"Read Count: {read_count} - {read_ratio}")
print(f"Write Count: {write_count} - {write_ratio}")
# print(cores)
g.close()

original_size = os.path.getsize(path)
reduced_size = os.path.getsize(final_path)
reduced_ratio = (original_size - reduced_size) / original_size
print("\n")
print(f"File Size: {convert_bytes(original_size)}")
print(f"Reduced File Size: {convert_bytes(reduced_size)}")
print("Reduced Ratio: {:.2f}%".format(reduced_ratio*100))
print("---")
