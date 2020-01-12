import argprocessor
import data_generator

def main():
   args = argprocessor.process()
   data_array = data_generator.generate_data(args)

if __name__ == "__main__":
   main()
