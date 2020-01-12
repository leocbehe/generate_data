import argprocessor
import data_generator
import file_writer

def main():
   args = argprocessor.process()
   data_array = data_generator.generate_data(args)
   file_writer.write_output_file(args.output_file, data_array)

if __name__ == "__main__":
   main()
