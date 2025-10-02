# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.


def kilometer_conversion(kilometers):    
    miles = 0.0
    ######################
def askUserForKilometers():
    userKilometers = float( input( "Please enter the distance" + " in kilometers: " ))
    return userKilometers
def convertKilometersToMiles( userKilometers ):
    miles = userKilometers * 0.6214
    return miles
def main():
    userKilometersTyped = askUserForKilometers()
    convertedMiles = convertKilometersToMiles( userKilometersTyped )

    print( "\n", userKilometersTyped, "Kilometers converted to miles is", \
          format( convertedMiles, ".2f" ), "miles", sep="" )
    
main()
    ######################    


    # Return the variable to the calling function
    

#### This piece of the code has been done for you,
#### you only need to worry about the actual kilometer
#### conversion logic in the kilometer_conversion function

    # Get User Input
   
    # Call kilometer_conversion, don't forget to pass in the kilometer parameter!
    
    # Display the miles
