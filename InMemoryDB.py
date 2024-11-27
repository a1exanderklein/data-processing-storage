class InMemoryDB:
    def __init__(self):
        self.data = {}  #committed data
        self.transaction_data = None  #uncommitted transaction data (None when no transaction in progress)

    def get(self, key):
        #check type
        if not isinstance(key, str):
            raise TypeError("Keys should be strings")
        #return value from self.data
        return self.data.get(key, None)

    def put(self, key, val):
        #check types
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        if not isinstance(val, int):
            raise TypeError("Value must be an integer")
        #if transaction is not in progress, throw exception
        if self.transaction_data is None:
            raise Exception("No transaction in progress")
        #store in self.transaction_data
        self.transaction_data[key] = val

    def begin_transaction(self):
        #if transaction data is not None, a transaction is in progress
        if self.transaction_data is not None:
            raise Exception("Transaction already in progress")
        self.transaction_data = {}

    def commit(self):
        #if transaction is not in progress, throw exception
        if self.transaction_data is None:
            raise Exception("No transaction in progress")
        #add additions from transaction_data to data
        for key, val in self.transaction_data.items():
            self.data[key] = val
        # Clear transaction_data
        self.transaction_data = None

    def rollback(self):
        #if transaction is not in progress, throw exception
        if self.transaction_data is None:
            raise Exception("No transaction in progress")
        #clear transaction_data
        self.transaction_data = None
