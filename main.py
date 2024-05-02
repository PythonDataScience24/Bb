#!/usr/bin/env python
import pandas as pd
import numpy as np

#code is mostly selfexplanatory in the way its written so minimal coments added

global dataframe #this is the main DB in RAM

def create_dataframe(columns):
    return pd.DataFrame(columns=columns)

def load_dataframe_from_disk():
    global dataframe
    # to do
    pass

def write_dataframe_to_disk():
    global dataframe
    # to do
    pass

def get_columns(dataframe): #gets the list of columns types in the current DB
    return dataframe.columns.tolist()

def add_book(atributes_of_book): #expects list with atributes of book to be added
    global dataframe
    dataframe.loc[len(dataframe.index)] = atributes_of_book


def remove_book(book_id): #removes book by index
    global dataframe
    dataframe = dataframe.drop(book_id)


def sort_by(dataframe, type, mode): #returns a sorted dataframe and expects a column type and the way to sort
    columns = get_columns(dataframe)
    if not type in columns:
        return create_dataframe(columns)
        error_log('The database does not contain the criteria you tried sorting by.')
    else:
        if(mode =='desc'):
            return dataframe.sort_values(by=type, ascending=False)
        elif(mode == 'asc'):
            return dataframe.sort_values(by=type, ascending=True)
        else:
            return create_dataframe(columns)
            error_log('Invalid argument for mode, use terms "asc" ord "desc".')



def filter_for(dataframe, type, argument): #returns a filtered dataframe and expects a column type and the argument to search for
    columns = get_columns(dataframe)
    if not type in columns:
        return create_dataframe(columns)
        error_log('The database does not contain the criteria you tried filtering by.')
    else:
        return dataframe.loc[dataframe[type] == argument]



def print_dataframe(dataframe):
    print(dataframe)


def db_debug_display(): #debug/testing method
    global dataframe
    print(dataframe)


def error_log(error): #error log curently goes to print
    print(error)


def setup(columns): #this initializes the DB in RAM
    global dataframe
    dataframe = create_dataframe(columns)



setup(['Title', 'Author', 'Genre', 'Pages'])
