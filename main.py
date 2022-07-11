import argparse
import sys
from parse import parse
from process_memory import process_memory
from grouping import grouping
from add_padding import add_padding
from utils import create_temp_folder
from plot_heatmap import plot_heatmap

### TAKING ARGUMENTS
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True,
	help="path of the file")
ap.add_argument("-i", "--interval", required=False, default=5,
	help="path of the file")
args = vars(ap.parse_args())



def main():

	path = args["path"]
	interval = args["interval"]
	print(f"Path: {path}")
	print(f"Interval: {interval}")
	print("\n")


	read, write, read_write, unique_read, unique_write, unique_read_write, filename = parse(path, interval)

	result_read = process_memory(read, unique_read, "read", filename)
	result_write = process_memory(write, unique_write, "write", filename)
	result_read_write = process_memory(read_write, unique_read_write, "read_write", filename)

	size_read, group_read = grouping(result_read)
	size_write, group_write = grouping(result_write)
	size_read_write, group_read_write = grouping(result_read_write)

	padded_group_read = add_padding(group_read)
	padded_group_write = add_padding(group_write)
	padded_group_read_write = add_padding(group_read_write)

	temp_directory = "temp_output"
	create_temp_folder(temp_directory)

	plot_heatmap(padded_group_read, "Read", size_read, filename, temp_directory)
	plot_heatmap(padded_group_write, "Write", size_write, filename, temp_directory)
	plot_heatmap(padded_group_read_write, "Read Write", size_read_write, filename, temp_directory)


if __name__ == "__main__":
  sys.exit(main())