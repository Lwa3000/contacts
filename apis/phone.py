
class Phone(object):
    """A simple Phone class to keep track of contacts"""

    def __init__(self, number, name, contacts=None):
        self.number = number
        self.name = name
        if contacts:
            self.contacts = contacts
        else:
            self.contacts = {}

    # The __repr__ method gives the class a print format that is meaningful to
    # humans, in this case we chose first and last name
    def __repr__(self):

        return self.name

    def add_contact(self, first_name, last_name, number):
        """Creates new Contact instance and adds the instance to contacts"""
        # See the types of each parameter from the function call in contact_ui.py
        contact = Contact(first_name, last_name, number)
        self.contacts[first_name] = contact
        print self.contacts

    def call(self, first_name, last_name):
        """Call a contact."""
        number=self.contacts[first_name].mobile_phone
        print "Calling %s at %i" %(first_name, number)
        #should find contact in contacts and print calling name and number   

    def text(self, first_name, message):
        """Send a contact a message."""
        number=self.contacts[first_name].mobile_phone
        print "To: %s at %i - %s" % (first_name, number, message)
        #should find contact in contacts and print name and number and message     

    def del_contact(self, first_name):
        """Remove a contact from phone"""
        del self.contacts[first_name]


    def _get_contact_key(self, first_name, last_name):
        """This is a private method. It's meant to be used only from within
        this class. We notate private attributes and methods by prepending with
        an underscore.
        """
        return first_name.lower() + " " + last_name.lower()


# class definition for a Contact
class Contact(object):
    """A class to hold information about an individual"""
    # initialize an instance of the object Contact
    def __init__(self,
                 first_name,
                 last_name,
                 mobile_phone,
                 email="",
                 twitter_handle=""):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_phone = mobile_phone
        self.email = email
        self.twitter_handle = twitter_handle

    # The __repr__ method gives the class a print format that is meaningful to
    # humans, in this case we chose first and last name
    def __repr__(self):
        return "%s %s" % (self.first_name, self.last_name)


    def full_name(self):
        return self.first_name + " " + self.last_name

# some examples of how to use these two classes

# Make a Phone instace
# tommys_phone = Phone(5555678, "Tommy Tutone's Phone")

# Use the Phone class to add new contacts!
# tommys_phone.add_contact("Jenny", "From That Song", 8675309)
