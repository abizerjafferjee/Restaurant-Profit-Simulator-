from customer import Customer
class Restaurant(object):
    """A Restaurant.

    This class represents a restaurant in the simulation. This is the base
    class for different restaurant approaches. The main purpose of this
    class to define common interfaces for different approaches. If there
    are common tasks for all approaches that did not depend on a specific
    management style, they should be implemented here. Otherwise, they should
    be implemented in the subclasses.

    This class is abstract; subclasses must implement add_customer and
    process_turn functions.

    You may, if you wish, change the API of this class to add
    extra public methods or attributes. Make sure that anything
    you add makes sense for ALL approaches, and not just a particular
    approach.

    === Private Attributes ===
    :type customer_list: lst
        a list of Customers entering the Restaurant
    :type profit: float
        the sum of profits for Customers whose orders have been taken
    :type customer_served: int
        the sum of Customers whose orders have been taken
    :type currently_serving: int
        the sum of entry_turn + prepare_time for Customers whose order have been taken
    """
    def __init__(self):
        """Initialize a restaurant.
        """
        #initiate list to add new customer
        self.customer_list = []
        #profit accumulates the profits for any approach
        self.profit = 0
        #customer_served accumulates the sum of customers served for any approach
        self.customer_served = 0
        #currently_preparing accumulates the sum of entry_turn + prepare_time for any approach
        self.currently_preparing = 0

    def add_customer(self, new_customer):
        """
        Add a new entering customer to the restaurant.

        :type new_customer: Customer
            The new customer that is entering the restaurant
        :rtype: None
        """
        #appends the new customer to the list
        self.customer_list.append(new_customer)

    def process_turn(self, current_turn):
        """Process the current_turn.

        This function will process the current turn. If the restaurant is not
        serving any customer now, and there are waiting customers, it should
        select one of them to serve.

        You can assume that all customers who entered the restaurant before or
        during this turn were already passed to the restaurant by simulator via
        calling the AddCustomer function.

        :type self: Restaurant
        :type current_turn: int
            The number of current turn
        :rtype: None
        """
        #override this method in the subclasses
        raise NotImplementedError('subclass needed')

    def write_report(self, report_file):
        """Write the final report of this restaurant approach in the report_file.

        :type self: Restaurant
        :type report_file: File
            This is an open file that this restaurant will write the report into.
        :rtype: None
        """
        #override this method in the subclasses
        raise NotImplementedError("subclass needed")


class PatApproach(Restaurant):
    """A Restaurant with Pat management style.

    This class represents a restaurant that uses the Pat management style,
    in which customers are served based on their arrival time. This class is
    a subclass of Restaurant and implements two functions: add_customer and
    process_turn.

    """
    def process_turn(self, current_turn):
        """
        Process the current_turn.

        This function will process the current turn. If the restaurant is not
        serving any customer now, and there are waiting customers, it should
        select one of them to serve.

        You can assume that all customers who entered the restaurant before or
        during this turn were already passed to the restaurant by simulator via
        calling the AddCustomer function.

        :param current_turn: the current turn
        :type current_turn: int
        :rtype: None

        Overrides Restaurant.process_turn(self, current_turn)
        """
        #removes any customer from customer_list whose patience has run out
        for i in self.customer_list:
            if current_turn > i.entry_turn() + i.patience():
                self.customer_list.remove(i)
        #checks whether restaurant is allowed to pick next order then picks next order
        if current_turn > self.currently_preparing \
                and (len(self.customer_list)!= 0):
            #removes the customer who is picked to serve
            j = self.customer_list.pop(0)
            self.customer_served += 1
            self.profit += j.profit()
            #updates currently_preparing
            self.currently_preparing += j.entry_turn() + j.prepare_time()
        else:
            pass

    def write_report(self, report_file):
        """Write the final report of this restaurant approach in the report_file.

        :type self: Restaurant
        :type report_file: File
            This is an open file that this restaurant will write the report into.
        :rtype: None

        Overrides Restaurant.write_report(self, report_file)
        """
        report_file.write("Results for the serving approach using Pat's suggestion:\n")
        report_file.write("Total profit: ${} \n" .format(format(self.profit, ".2f")))
        report_file.write("Customer served: {} \n" .format(self.customer_served))

class MatApproach(Restaurant):
    """A Restaurant with Mat management style.

    This class represents a restaurant that uses the Mat management style,
    in which customers are served based on the person that arrives the latest.
    This class is a subclass of Restaurant and implements two functions:
    process_turn and write_report.

    """
    def process_turn(self, current_turn):
        """
        Process the current_turn.

        This function will process the current turn. If the restaurant is not
        serving any customer now, and there are waiting customers, it should
        select one of them to serve.

        You can assume that all customers who entered the restaurant before or
        during this turn were already passed to the restaurant by simulator via
        calling the AddCustomer function.

        :param current_turn: the current turn
        :type current_turn: int
        :rtype: None

        Overrides Restaurant.process_turn(self, current_turn)
        """
        #removes any customer from customer_list whose patience has run out
        for i in self.customer_list:
            if current_turn > i.entry_turn() + i.patience():
                self.customer_list.remove(i)
        #checks whether restaurant is allowed to pick next order then picks next order
        if current_turn > self.currently_preparing\
                and (len(self.customer_list)!= 0):
            index = 0
            #sets priority
            priority = self.customer_list[0].entry_turn()
            i = 1
            while i < len(self.customer_list):
                if self.customer_list[i].entry_turn() >= priority:
                    #if condition is true, updates priority
                    priority = self.customer_list[i].entry_turn()
                    index = i
                i += 1
            #removes the customer who is picked to serve
            j = self.customer_list.pop(index)
            self.customer_served += 1
            self.profit += j.profit()
            self.currently_preparing += j.entry_turn() + j.prepare_time()
        else:
            pass

    def write_report(self, report_file):
        """Write the final report of this restaurant approach in the report_file.

        :type self: Restaurant
        :type report_file: File
            This is an open file that this restaurant will write the report into.
        :rtype: None

        Overrides Restaurant.write_report(self, report_file)
        """
        report_file.write("Results for the serving approach using Mat's suggestion:\n")
        report_file.write("Total profit: ${} \n" .format(format(self.profit,".2f")))
        report_file.write("Customer served: {} \n" .format(self.customer_served))

class MaxApproach(Restaurant):
    """A Restaurant with Pat management style.

    This class represents a restaurant that uses the Max management style,
    in which customers are served based on whoever brings the highest profit.
    This class is a subclass of Restaurant and implements two functions:
    process_turn and write_report.

    """
    def process_turn(self, current_turn):
        """
        Process the current_turn.

        This function will process the current turn. If the restaurant is not
        serving any customer now, and there are waiting customers, it should
        select one of them to serve.

        You can assume that all customers who entered the restaurant before or
        during this turn were already passed to the restaurant by simulator via
        calling the AddCustomer function.

        :param current_turn: the current turn
        :type current_turn: int
        :rtype: None

        Overrides Restaurant.process_turn(self, current_turn)
        """
        #removes any customer from customer_list whose patience has run out
        for i in self.customer_list:
            if current_turn > i.entry_turn() + i.patience():
                self.customer_list.remove(i)
        #checks whether restaurant is allowed to pick next order then picks next order
        if current_turn > self.currently_preparing \
                and (len(self.customer_list)!= 0):
            index = 0
            priority = self.customer_list[0].profit()
            i = 1
            while i < len(self.customer_list):
                if self.customer_list[i].profit() > priority:
                    #if condition is true, updates priority
                    priority = self.customer_list[i].profit()
                    index = i
                i += 1
            #removes the customer who is picked to serve
            j = self.customer_list.pop(index)
            self.customer_served += 1
            self.profit += j.profit()
            self.currently_preparing += j.entry_turn() + j.prepare_time()
        else:
            pass

    def write_report(self, report_file):
        """Write the final report of this restaurant approach in the report_file.

        :type self: Restaurant
        :type report_file: File
            This is an open file that this restaurant will write the report into.
        :rtype: None

        Overrides Restaurant.write_report(self, report_file)
        """
        report_file.write("Results for the serving approach using Max's suggestion:\n")
        report_file.write("Total profit: ${} \n" .format(format(self.profit,".2f")))
        report_file.write("Customer served: {} \n" .format(self.customer_served))

class PacApproach(Restaurant):
    """A Restaurant with Pat management style.

    This class represents a restaurant that uses the Pac management style,
    in which customers are served based on the shortest time to prepare order.
    This class is a subclass of Restaurant and implements two functions:
    process_turn and write_report.

    """
    def process_turn(self, current_turn):
        """
        Process the current_turn.

        This function will process the current turn. If the restaurant is not
        serving any customer now, and there are waiting customers, it should
        select one of them to serve.

        You can assume that all customers who entered the restaurant before or
        during this turn were already passed to the restaurant by simulator via
        calling the AddCustomer function.

        :param current_turn: the current turn
        :type current_turn: int
        :rtype: None

        Overrides Restaurant.process_turn(self, current_turn)
        """
        #removes any customer from customer_list whose patience has run out
        for i in self.customer_list:
            if current_turn > i.entry_turn() + i.patience():
                self.customer_list.remove(i)
        #checks whether restaurant is allowed to pick next order then picks next order
        if current_turn > self.currently_preparing\
                and (len(self.customer_list)!= 0):
            index = 0
            priority = self.customer_list[0].prepare_time()
            i = 1
            while i < len(self.customer_list):
                if self.customer_list[i].prepare_time() <= priority:
                    #if condition is true, updates priority
                    priority = self.customer_list[i].prepare_time()
                    index = i
                i += 1
            #removes the customer who is picked to serve
            j = self.customer_list.pop(index)
            self.customer_served += 1
            self.profit += j.profit()
            self.currently_preparing += j.entry_turn() + j.prepare_time()
        else:
            pass

    def write_report(self, report_file):
        """Write the final report of this restaurant approach in the report_file.

        :type self: Restaurant
        :type report_file: File
            This is an open file that this restaurant will write the report into.
        :rtype: None

        Overrides Restaurant.write_report(self, report_file)
        """
        report_file.write("Results for the serving approach using Pac's suggestion:\n")
        report_file.write("Total profit: ${} \n".format(format(self.profit, ".2f")))
        report_file.write("Customer served: {} \n".format(self.customer_served))
