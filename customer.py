
class Customer:
    """A Customer.

    This class represents a customer in the simulation. Each customer will
    enter the simulation at _entry_time, will wait at most _patience turns.
    The restaurant need _prepare_time turns to prepare this customer order,
    and will receive _profit if can serve this customer on time.

    Your main task is to implement the remaining methods.

    === Private Attributes ===
    :type _entry_turn: int
        the turn a Customer enters the restaurant
    :type _id: int
        the id of a Customer
    :type _profit: float
        the profit of a Customer
    :type _prepare_time: int
        the time taken to prepare a Customer's order
    :type _patience: int
        the time a Customer will wait for order to be taken
    """
    def __init__(self, definition):
        """
        Create a new Customer self with a definition string with customer details.
        """
        #split definition to change it into a list
        self.definition = definition.split()
        self._entry_turn = int(self.definition[0])
        self._id = int(self.definition[1])
        self._profit = float(self.definition[2])
        self._prepare_time = int(self.definition[3])
        self._patience = int(self.definition[4])

    def id(self):
        """
        Return the id for Customer self.

        :return _id: the id of Customer self
        :rtype: int

        >>> c = Customer("1	23215	13	4	8")
        >>> c.id()
        23215
        """
        return self._id

    def entry_turn(self):
        """
        Return the entry_turn for Customer self.

        :return _entry_turn: the entry_turn of Customer self
        :rtype: int

        >>> c = Customer("1	23215	13	4	8")
        >>> c.entry_turn()
        1
        """
        return self._entry_turn

    def profit(self):
        """
        Return the profit for Customer self.

        :return _profit: the profit of Customer self
        :rtype: float

        >>> c = Customer("1	23215	13	4	8")
        >>> c.profit()
        13.0
        """
        return self._profit

    def prepare_time(self):
        """
        Return prepare_time for Customer self.

        :return _prepare_time: prepare_time of Customer self
        :rtype: int

        >>> c = Customer("1	23215	13	4	8")
        >>> c.prepare_time()
        4
        """
        return self._prepare_time

    def patience(self):
        """
        Return patience for Customer self.

        :return _patience: patience of Customer self
        :rtype: int

        >>> c = Customer("1	23215	13	4	8")
        >>> c.patience()
        8
        """
        return self._patience

    def __eq__(self, other):
        """
        Return whether this Customer is the same as other Customer by comparing\
        id's.

        :param Customer self: this Customer
        :param Customer other: any other Customer
        :rtype: bool

        >>> c = Customer("1	23215	13	4	8")
        >>> d = Customer("1	58923	5	6	9")
        >>> e = Customer("1	23215	5	6	9")
        >>> c.__eq__(d)
        False
        >>> c.__eq__(e)
        True
        """
        #comparing id's because other attributes of Customer may be the same
        return self.id() == other.id()

    def __str__(self):
        """
        Return a user-friendly string representation of Customer self.

        :rtype: str

        >>> c = Customer("1	58923	5	6	9")
        >>> c.__str__()
        'The following are the details for: Customer 23215, Entrance-Time: 1,
        Prepare-Time: 4, Profit: 13.0, Patience: 8'
        """
        return "The following are the details for: Customer %s, Entrance-Time: "\
               "%s, Prepare-Time: %s, Profit: %s, Patience: %s" % (self.id(),
                self.entry_turn(), self.prepare_time(),self.profit(),
                self.patience())






