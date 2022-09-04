# imports
import csv
import sys
import pathlib
import pickle


# person class
class Person:

    # initialize the fields
    def __init__(self, last, first, mi, id, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.id = id
        self.phone = phone

    # output the fields
    def display(self):
        print("Employee id: %s \n\t %s %s %s \n\t %s \n" % (self.id, self.first, self.mi, self.last, self.phone))


# processor for input file
def processor(filepath):
    # create dictionary
    dict = {}
    # open csv file for reading
    with open(pathlib.Path.cwd().joinpath(filepath), 'r') as data:
        reader = csv.reader(data)
        # skip first line
        next(reader)
        for line in reader:
            # store last name
            l = line[0]
            # lowercase then capitalize last name
            l = l.lower().capitalize()
            # store first name
            f = line[1]
            # lowercase then capitalize first name
            f = f.lower().capitalize()
            # store middle initial
            mi = line[2]
            # check if there was a middle initial, and uppercase if existent
            if mi:
                mi = mi.upper()
            else:
                mi = 'X'
            # store id
            id = line[3]
            # make the user enter an id if it is not in "AB1234" format
            while not (id[:2].isalpha() and id[2:6].isnumeric() and len(id) == 6):
                print("ID invalid: %s" % id)
                print("ID is two letters followed by 4 digits")
                id = input("Please enter a valid id: ").upper()
            # store phone number
            op = line[4]
            # make the user enter a phone number if it is not in "123-456-7890" format
            while not (op[:3].isnumeric() and op[3:4] == '-' and op[4:7].isnumeric()
                       and op[7:8] == '-' and op[8:].isnumeric()):
                print("Phone %s is invalid" % op)
                print("Enter phone number in form 123-456-7890")
                op = input("Enter phone number: ")
            # add person to dictionary
            dict.update({id: Person(l, f, mi, id, op)})
        # return the dictionary of persons
        return dict


# main method
if __name__ == '__main__':
    # user enters path and program checks if it is correct
    if len(sys.argv) < 2:
        print('Please enter a filename as a system arg')
        exit(1)
    # process the csv file
    test_dict = processor(sys.argv[1])
    # load dictionary into pickle file
    pickle.dump(test_dict, open("persons.pickle", "wb"))
    # open pickle file for reading
    person_dict = pickle.load(open("persons.pickle", "rb"))
    # get the list of persons
    persons = person_dict.values()
    print("\n\nEmployee List: \n")
    # display the persons' fields to show the file was unpickled correctly
    for x in persons:
        x.display()
