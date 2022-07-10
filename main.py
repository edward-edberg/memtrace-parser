import argparse
import sys
from parse import parse

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


	parse(path, interval)



if __name__ == "__main__":
  sys.exit(main())