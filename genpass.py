# Description: This script generates a password based on a desired length.
# Author: Armando Montero
# Version 1.0


# Import required libraries
import random
import string
import argparse 
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# Function to pass arguments. 
def parse_args():
    parser = argparse.ArgumentParser(
            prog = 'genpass.py',
            description = "High Entropy Password Generator.",
            epilog = "Generates passwords based on a desired length. Recommended length is 16 characters or higher.",
            usage = "%(prog)s --generate --length # or -g -l #",
            add_help = True, 
            allow_abbrev = True,
            exit_on_error= True)
    
    parser.add_argument('-l','--length', 
                        required = False,                        
                        action = 'store', 
                        type = int,                       
                        help = 'Length of the password.')
    parser.add_argument('-g', '--generate',
                        action = 'store_true',
                        required = False, 
                        help= 'Generates a password',
                        )
    

    # Parse the arguments and store them in args.  
    args = vars(parser.parse_args())
    return args


# Function to generate password.

def gen_pass(args,length): 
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(length))

    return password

# Main function
def main():
    
    # Parse arguments
    args = parse_args()
    length = args["length"]

    # Conditional to check if the generate flag is set. If true, generate a high entropy password based on the desired length.     
    if args['generate']:  
        password = gen_pass(args, length)
        print(f"Generated password: {password}")
    else:
        print("No password generated, See full menu genpass.py --help or execute genpass.py --generate --length # to generate..")

# Call to main
if __name__ == "__main__":
    try:
        main()
    except Exception as e:        
        logger.error("An error occurred: %s", e, exc_info=True)
        raise
