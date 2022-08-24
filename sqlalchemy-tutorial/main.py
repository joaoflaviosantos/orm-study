from functions._first_command import first_command
from functions._command_with_conn import command_with_conn
from functions._create_first_row import create_first_row
from functions._first_query import first_query
from functions._class_method_query import class_method_query
from functions._create_all_tables import create_all_tables


class Main:
    def __init__(self):
        self.project_name = 'SQLAlchemy Basics Tutorial - Leticia Portella'

    def run(self):
        print(f'\n-------- {self.project_name} --------')
        first_command()
        command_with_conn()
        create_all_tables()
        create_first_row()
        first_query()
        class_method_query()
        print(f'\n-------- Finished --------')


if __name__ == '__main__':
    test = Main()
    test.run()
