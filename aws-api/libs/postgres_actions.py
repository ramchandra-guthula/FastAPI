from sqlalchemy import create_engine, Integer, Date, Table, Column, String, MetaData, inspect


class PostgresActions:

    def __init__(self, table_name):
        self.table_name = table_name

    def table_data(self) -> tuple:
        """
        this method used to supply data to other methods
        :return: tuple
        """
        db_string = "postgresql://postgres:changeit@localhost:5432/aws_actions"
        db = create_engine(db_string)
        meta = MetaData(db)
        return (Table(self.table_name, meta,
                      Column('execution_id', Integer, primary_key=True, nullable=False),
                      Column('user_id', String),
                      Column('status_code', Integer),
                      Column('created_on', Date),
                      Column('action_type', String),
                      ), db)

    def create_table(self) -> None:
        """
        Method used to create a table in existing database 'aws_actions'
        :return: none
        """
        aws_api_table = self.table_data()[0]

        inspector = inspect(self.table_data()[1])
        if inspector.has_table(self.table_name) is True:
            print("Table exists already")
        else:
            print("Table doesn't exist, Creating new table....")
            return aws_api_table.create()

    def add_data(self) -> None:
        """
        this method adds data to the table supplied, make sure table exists already
        :return: dic
        """
        table_params = self.table_data()[0]
        db = self.table_data()[1]
        insert_statement = table_params.insert().values(user_id="ramguthula",
                                                        status_code=500,
                                                        created_on='2022-06-08 9:30:22',
                                                        action_type='PUT')
        return db.execute(insert_statement)

    def read_data(self) -> list:
        """
        Read data from a given table
        :return: list
        """
        db = self.table_data()[1]
        result_set = db.execute(f"SELECT * FROM {self.table_name}")
        return [print(r) for r in result_set]


if __name__ == "__main__":
    initiate_db_create = PostgresActions('dummy')
    initiate_db_create.create_table()
    initiate_db_create.add_data()
    initiate_db_create.read_data()
