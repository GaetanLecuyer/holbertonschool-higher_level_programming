from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base instance
Base = declarative_base()

class State(Base):
    """
    Represents a State table in the database.
    """

    __tablename__ = 'states'  # The name of the MySQL table

    # Columns definition
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # This part is only executed when the script is run directly

    # Replace 'your_mysql_username' and 'your_mysql_password' with your actual MySQL credentials
    mysql_username = 'your_mysql_username'
    mysql_password = 'your_mysql_password'
    database_name = 'your_database_name'  # Replace with your actual database name

    # Define the connection string to connect to MySQL running on localhost at port 3306
    connection_string = f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}"

    # Create the engine to connect to the database
    engine = create_engine(connection_string)

    # Import all classes that inherit from Base before calling Base.metadata.create_all()
    from other_module import SomeOtherClass  # Import other classes if you have them

    # Create all tables defined in the Base
    Base.metadata.create_all(engine)
