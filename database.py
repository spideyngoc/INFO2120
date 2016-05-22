#!/usr/bin/env python3

from modules import pg8000
import configparser


# Define some useful variables
ERROR_CODE = 55929

#####################################################
##  Database Connect
#####################################################

def database_connect():
    # Read the config file
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Create a connection to the database
    connection = None
    try:
        connection = pg8000.connect(database=config['DATABASE']['user'],
            user=config['DATABASE']['user'],
            password=config['DATABASE']['password'],
            host=config['DATABASE']['host'])
    except pg8000.OperationalError as e:
        print("""Error, you haven't updated your config.ini or you have a bad
        connection, please try again. (Update your files first, then check
        internet connection)
        """)
        print(e)
    #return the connection to use
    return connection

#####################################################
##  Login
#####################################################

def check_login(email, password):
    # Dummy data
    val = ['Shadow', 'Mr', 'Evan', 'Nave', '123 Fake Street, Fakesuburb', 'SIT', '01-05-2016', 'Premium', '1']
    # TODO
    # Check if the user details are correct!
    # Return the relevant information (watch the order!)
    return val


#####################################################
##  Homebay
#####################################################
def update_homebay(email, bayname):
    # TODO
    # Update the user's homebay
    return True

#####################################################
##  Booking (make, get all, get details)
#####################################################

def make_booking(email, car_rego, date, hour, duration):
    # TODO
    # Insert a new booking
    # Make sure to check for:
    #       - If the member already has booked at that time
    #       - If there is another booking that overlaps
    #       - Etc.
    # return False if booking was unsuccessful :)
    # We want to make sure we check this thoroughly
    return True


def get_all_bookings(email):
    val = [['66XY99', 'Ice the Cube', '01-05-2016', '10', '4', '29-04-2016'],['66XY99', 'Ice the Cube', '27-04-2016', '16'], ['WR3KD', 'Bob the SmartCar', '01-04-2016', '6']]

    # TODO
    # Get all the bookings made by this member's email

    return val

def get_booking(b_date, b_hour, car):
    val = ['Shadow', '66XY99', 'Ice the Cube', '01-05-2016', '10', '4', '29-04-2016', 'SIT']

    # TODO
    # Get the information about a certain booking
    # It has to have the combination of date, hour and car

    return val


#####################################################
##  Car (Details and List)
#####################################################

def get_car_details(regno):
    val = ['66XY99', 'Ice the Cube','Nissan', 'Cube', '2007', 'auto', 'Luxury', '5', 'SIT', '8', 'http://example.com']
    # TODO
    # Get details of the car with this registration number
    # Return the data (NOTE: look at the information, requires more than a simple select. NOTE ALSO: ordering of columns)
    return val

def get_all_cars():
    val = [ ['66XY99', 'Ice the Cube', 'Nissan', 'Cube', '2007', 'auto'], ['WR3KD', 'Bob the SmartCar', 'Smart', 'Fortwo', '2015', 'auto']]

    # TODO
    # Get all cars that PeerCar has
    # Return the results

    return val
#####################################################
##  Bay (detail, list, finding cars inside bay)
#####################################################

def get_all_bays():
    val = [['SIT', '123 Some Street, Boulevard', '2'], ['some_bay', '1 Somewhere Road, Right here', '1']]
    # TODO
    # Get all the bays that PeerCar has :)
    # And the number of bays
    # Return the results
    return val

def get_bay(name):
    val = ['SIT', 'Home to many (happy?) people.', '123 Some Street, Boulevard', '-33.887946', '151.192958']

    # TODO
    # Get the information about the bay with this unique name
    # Make sure you're checking ordering ;)

    return val

def search_bays(search_term):
    val = [['SIT', '123 Some Street, Boulevard', '-33.887946', '151.192958']]

    # TODO
    # Select the bays that match (or are similar) to the search term
    # You may like this
    return val

def get_cars_in_bay(bay_name):
    val = [ ['66XY99', 'Ice the Cube'], ['WR3KD', 'Bob the SmartCar']]

    # TODO
    # Get the cars inside the bay with the bay name
    # Cars who have this bay as their bay :)
    # Return simple details (only regno and name)

    return val
