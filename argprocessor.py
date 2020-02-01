import argparse

def process():
   parser = argparse.ArgumentParser()
   parser.add_argument("curve", choices=[ "constant", "linear", "square", "gaussian"], 
                        help="The type of curve that the data set will follow.")
   parser.add_argument("-o", "--output-file", dest="output_file", default="output.csv", 
                        help="The name of the output file to write to. (default: output.csv)")
   parser.add_argument("-u", "--uncertainty", default=0.05, type=float,
                        help="The uncertainty range within which our randomly generated " +\
                        "data points will fluctuate. (default: 0.05)")
   parser.add_argument("-d", "--domain", default=10, type=int, help="The domain of x, starting " +\
                        "at 0, across which our data points will be generated. (default: 10)")
   parser.add_argument("-i", "--interval", default=0.01, type=float, help="The x-interval between " +\
                        "any two neighboring data points.")

   return parser.parse_args()
