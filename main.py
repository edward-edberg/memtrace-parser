import argparse
import sys

### TAKING ARGUMENTS
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True,
	help="path of the file")
ap.add_argument("-i", "--interval", required=False, default=5,
	help="path of the file")
args = vars(ap.parse_args())



def main():
	print("Path: {}".format(args["path"]))
	print("Interval: {}".format(args["interval"]))
	print("\n")

	


if __name__ == "__main__":
  sys.exit(main())