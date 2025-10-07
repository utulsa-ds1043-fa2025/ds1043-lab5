"""Lab 5: Data Scavenger Hunt

A small program to find superlative counties of the United States.

Completed Date by Name for DS-1043
"""
import sys
import csv
import statistics
from collections.abc import Iterable, Collection, Sequence, Callable


# Functions to Complete #######################################################

def read_csv_data(filename: str) -> list[dict[str, str | float]]:
    """Reads data from a CSV file"""
    data = list()
    return data


def write_markdown_report(filename: str, contents: list[str]) -> None:
    """Writes the markdown report 'contents' to file"""
    pass


# TODO: Understand what key is and finish the function
def answer_question(data: list[dict], question: tuple) -> list[str]:
    """Generates the markdown formatted answer to a particular question"""
    description, func, order, fields = question
    key = sorted(
        enumerate([func(row) for row in reduce_table(data, fields)]),
        key=lambda t: t[1], reverse=order)
    return list(str())


# TODO: Change this function to make the columns of uniform size
def create_table(fields: list[str], records: list[tuple[str]]) -> list[str]:
    "Format records into a markdown table with fields as the headers"
    table = ['| ' + ' | '.join(fields) + ' |',
             '|' + len(fields) * ' --- |']
    for record in records:
        table.append('| ' + ' | '.join(record) + ' |')
    return table


def first_of_all(data: Iterable[float]) -> float:
    """Calculates the percentage that the first item represents of the sum of all"""
    return 0.0


def growth_rate(data: Iterable[float]) -> float:
    """Calculates the percent growth rate between two points in time"""
    # TODO: Finish this function
    return 0.0

# Provided Functions ##########################################################

def reduce_table(table: Sequence[dict], fields: Collection[str]) -> list[list]:
    """Returns a copy of the data in fields as a nested list matrix"""
    reduced = []
    for row in table:
        row_data = []
        for field in fields:
            row_data.append(row[field])
        reduced.append(row_data)
    return reduced

# Configuration Options #######################################################

# CSV File Location
DATAFILE = r'counties.csv'

# Each question: (Description, Function, Reverse?, Fields)
# TODO: Double Check These
QUESTIONS = (
    ('most temperature stable', statistics.variance, False,
     ('noaa/temp-jan', 'noaa/temp-apr', 'noaa/temp-jul', 'noaa/temp-oct')),
    ('least temperature stable', statistics.variance, True,
     ('noaa/temp-jan', 'noaa/temp-apr', 'noaa/temp-jul', 'noaa/temp-oct')), 
    ('fastest growing', growth_rate, False, ('population/2010', 'population/2019')),
    ('fastest declining', growth_rate, True, ('population/2010', 'population/2019')),
    ('deadliest', sum, False, ('deaths/suicides', 'deaths/firearm suicides',
                               'deaths/homicides', 'deaths/vehicle')),
    ('least deadly', sum, True, ('deaths/suicides', 'deaths/firearm suicides',
                                 'deaths/homicides', 'deaths/vehicle')),
    ('most skewed female', first_of_all, True, ('male', 'female')),
    ('most skewed male', first_of_all, True, ('female', 'male')),
    ('oldest', sum, False,
     ('age/65-69', 'age/70-74', 'age/75-79', 'age/80-84', 'age/85+')),
    ('youngest', sum, False, ('age/0-4', 'age/5-9', 'age/10-14', 'age/15-19')),
    ('most age diverse', statistics.variance, True,
     ('age/0-4', 'age/5-9', 'age/10-14', 'age/15-19', 'age/20-24',
      'age/25-29', 'age/30-34', 'age/35-39', 'age/40-44', 'age/45-49',
      'age/50-54', 'age/55-59', 'age/60-64', 'age/65-69', 'age/70-74',
      'age/75-79', 'age/80-84', 'age/85+')),
    ('highest employment', first_of_all, False,
     ('bls/2020/employed', 'bls/2020/unemployed')),
    ('highest unemployment', first_of_all, False,
     ('bls/2020/employed', 'bls/2020/unemployed'))
)

################################################################################

if __name__ == '__main__':
    data = read_csv_data(DATAFILE)
    report = []
    for question in QUESTIONS:
        pass
