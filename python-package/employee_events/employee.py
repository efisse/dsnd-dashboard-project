# Import the QueryBase class
from .query_base import QueryBase

# Import dependencies needed for sql execution
# from the `sql_execution` module
from .sql_execution import QueryMixin

# Define a subclass of QueryBase
# called Employee
class Employee(QueryBase):

    # Set the class attribute `name`
    # to the string "employee"
    name = "employee"


    # Define a method called `names`
    # that receives no arguments
    # This method should return a list of tuples
    # from an sql execution
    def names(self):
        """
        Get all employee names and IDs
        
        Returns:
            list: List of tuples containing (full_name, employee_id)
        """
        # Query 3
        # Write an SQL query
        # that selects two columns 
        # 1. The employee's full name
        # 2. The employee's id
        # This query should return the data
        # for all employees in the database
        sql_query = """
            SELECT (first_name || ' ' || last_name) as full_name, employee_id
            FROM employee
            ORDER BY full_name
        """
        return self.query(sql_query)
    

    # Define a method called `username`
    # that receives an `id` argument
    # This method should return a list of tuples
    # from an sql execution
    def username(self, id):
        """
        Get employee full name by ID
        
        Args:
            id (int): Employee ID
            
        Returns:
            list: List of tuples containing (full_name,)
        """
        # Query 4
        # Write an SQL query
        # that selects an employees full name
        # Use f-string formatting and a WHERE filter
        # to only return the full name of the employee
        # with an id equal to the id argument
        sql_query = f"""
            SELECT (first_name || ' ' || last_name) as full_name
            FROM employee
            WHERE employee_id = {id}
        """
        return self.query(sql_query)


    # Below is method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returns containing the execution of
    # the sql query
    def model_data(self, id):
        """
        Get model data for employee recruitment risk prediction
        
        Args:
            id (int): Employee ID
            
        Returns:
            pd.DataFrame: Model data with positive and negative events
        """
        sql_query = f"""
                    SELECT SUM(positive_events) positive_events
                         , SUM(negative_events) negative_events
                    FROM {self.name}
                    JOIN employee_events
                        USING({self.name}_id)
                    WHERE {self.name}.{self.name}_id = {id}
                """
        return self.pandas_query(sql_query)