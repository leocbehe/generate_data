import random
import math

def generate_data(args):
   distribution_function = create_function(args.curve)
   data_array = calculate_data_points(distribution_function, uncertainty=args.uncertainty, \
                         domain=args.domain, interval=args.interval)
   print(data_array)
   
   return data_array

def create_function(func_type):
   if func_type == "constant":
      return lambda x: 1
   elif func_type == "linear":
      return lambda x: x
   elif func_type == "square":
      return lambda x: x ** 2
   elif func_type == "gaussian":
      return lambda x: math.e ** -(x ** 2)
   else:
      return None

def calculate_data_points(distribution_function, **kwargs):
   uncertainty = kwargs["uncertainty"]
   domain = kwargs["domain"]
   interval = kwargs["interval"]

   xvals = [ x * interval for x in range(int(domain / interval))]

   return [[distribution_function(x) + deviation(distribution_function(x), uncertainty)] for x in xvals]

def deviation(function_val, uncertainty):
   max_deviation = function_val * uncertainty
   return random.uniform(-max_deviation, max_deviation)
