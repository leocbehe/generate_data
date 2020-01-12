import csv

def write_output_file(output_filename, data_array):
   try:
      with open(output_filename, 'w') as of:
         writer = csv.writer(of, dialect='unix')
         for xval in data_array:
            writer.writerow(xval)
   except IOError as ioe:
      print(ioe)
