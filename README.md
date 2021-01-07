# Armstrong Number
An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
    For example:
    
    9 is an Armstrong number, because 9 = 9^1 = 9
    10 is not an Armstrong number, because 10 != 1^2 + 0^2 = 1
    153 is an Armstrong number, because: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    
For more information on this subject, refer to the following link: https://en.wikipedia.org/wiki/Narcissistic_number

## How this program works:

Run the program on the command line. And give it the last number of the sequence range. And get the list of Armstrong numbers in that range as a list.

    python main.py 2563569
## Install packages:

Use the following command to install the packages:

     pip install -r requirements.txt
     
## What these packages do:

### tqdm
tqdm derives from the Arabic word taqaddum (تقدّم) which can mean “progress,” and is an abbreviation for “I love you so much” in Spanish (te quiero demasiado).

This package makes your loops show a smart progress meter - just wrap any iterable with tqdm(iterable), and you’re done!

### colorama

Makes ANSI escape character sequences (for producing colored terminal text and cursor positioning) work under MS Windows.

ANSI escape character sequences have long been used to produce colored terminal text and cursor positioning on Unix and Macs. Colorama makes this work on Windows, too, by wrapping stdout, stripping ANSI sequences it finds (which would appear as gobbledygook in the output), and converting them into the appropriate win32 calls to modify the state of the terminal. On other platforms, Colorama does nothing.

