#!/usr/bin/env python
import pandas as pd
import numpy as np

class Backend:

    def __init__(self, noload):
        self.columns = ["Title", "Author", "Genre", "Pages"]
        if not noload:
            self.dataframe = self.load_dataframe_from_disk()
        else:
            self.dataframe = pd.DataFrame(columns=self.columns)

    def load_dataframe_from_disk(self):
        try:
            data = pd.read_csv("database.csv", index_col=0)
        except:
            print("FATAL ERROR, could not load database from disk to ram!")
            print("Creating an empty database...")
            data = pd.DataFrame(columns=self.columns)
        return data

    def write_dataframe_to_disk(self):
        try:
            self.dataframe.to_csv("database.csv", encoding='utf-8')
        except:
            print("FATAL ERROR, could not write database from ram to disk! Do not close the program or you will have data loss.")


    def get_columns(self):  # gets the list of columns types in the current DB
        return self.dataframe.columns.tolist()


    def add_book(self, atributes_of_book):  # expects list with atributes of book to be added
        self.dataframe.loc[len(self.dataframe.index)] = atributes_of_book


    def remove_book(self, book_id):  # removes book by index
        self.dataframe = self.dataframe.drop(book_id)


    def sort_by(self, type, mode):  # returns a sorted dataframe and expects a column type and the way to sort
        columns = self.get_columns()
        if not type in columns:
            return pd.DataFrame(columns=self.columns)
            error_log("The database does not contain the criteria you tried sorting by.")
        else:
            if mode == "desc":
                return self.dataframe.sort_values(by=type, ascending=False)
            elif mode == "asc":
                return self.dataframe.sort_values(by=type, ascending=True)
            else:
                return pd.DataFrame(columns=self.columns)
                error_log('Invalid argument for mode, use terms "asc" ord "desc".')


    def filter_for(self, type, argument):  # returns a filtered dataframe and expects a column type and the argument to search for
        columns = self.get_columns()
        if not type in columns:
            return pd.DataFrame(columns=self.columns)
            error_log("The database does not contain the criteria you tried filtering by.")
        else:
            return self.dataframe.loc[self.dataframe[type] == argument]


    def db_debug_display(self):  # debug/testing method
        print(self.dataframe)

    def get_dataframe(self):
        return self.dataframe

    def error_log(error):  # error log curently goes to print
        print(error)
