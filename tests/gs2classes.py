#!/usr/bin/env python
# coding: utf-8

# Move grades from Gradescope to NYU Classes
# 
# We will use the data package `pandas` for this.
# In this script version, all of the display steps I took to 
# check my work in pandas are commented out.
# You can uncomment them if you want to see/save 
# intermediate steps.
# This script reads from sys.argv[1], and writes to stdout.


import sys
import pandas as pd


def rename_col(df, old_nm, new_nm):
    df.rename(columns = {old_nm: new_nm}, inplace = True)


def drop_col_by_pattern(df, pat):
    df.drop(df.columns[df.columns.str.contains(pat)], axis=1, inplace=True)


if len(sys.argv) < 2:
    print("Please supply a starting csv file.")
    exit(1)

# view all columns:
pd.set_option('display.max_columns', None)
grades = pd.read_csv(sys.argv[1])
# grades.head(2)


# Drop some unneeded cols -- we will keep "Max Points" for now.
# don't need email... GS has SID col.
grades.drop("Email", axis=1,  inplace=True)
grades.drop("section_name", axis=1,  inplace=True)
drop_col_by_pattern(grades, 'Submission Time')
drop_col_by_pattern(grades, 'Lateness')
drop_col_by_pattern(grades, 'Max Points')
drop_col_by_pattern(grades, 'Mock')
# grades.head(2)

# Save an intermediate version:
# grades.to_csv("grades2.csv")

# I think this could be done with a reg exp, but...
# we do have to add points!
rename_col(grades, 'Assignment 0 - Getting Started', 'Asg0 [5]')
rename_col(grades, 'Assignment 1 - Karel the Robot', 'Asg1 [19]')
rename_col(grades, 'Assignment 2 - Calculator and Text Analyzer', 'Asg2 [20]')
rename_col(grades, 'Assignment 3 - Blackjack', 'Asg3 [16]')
rename_col(grades, 'Assignment 4 - Guessing Game', 'Asg4 [19]')
rename_col(grades, 'Assignment 5 - Tic-tac-toe', 'Asg5 [45]')
grades.head(2)


MID_POINTS = '100'
rename_col(grades, 'Midterm 1', 'Mid1 [' + MID_POINTS + ']')
rename_col(grades, 'Midterm 2', 'Mid2 [' + MID_POINTS + ']')
# grades.head(2)

# Save intermediate version:
# grades.to_csv("grades3.csv")


# Move SID to first col:
cols = list(grades.columns)
cols = cols[2:3] + cols[0:2] + cols[3:]
# print(cols)

grades = grades[cols]
# grades.head(2)

# Combine first and last name into just name:
pd.options.mode.chained_assignment = None
grades["Student Name"] = grades[['First Name', 'Last Name']].apply(lambda x: ' '.join(x),
                                                                   axis=1)
# grades.head(3)

# Move name to 2nd column, as Classes demands, and git rid of first and last:
cols = list(grades.columns)
cols = cols[0:1] + cols[-1:] + cols[3:-2]
grades = grades[cols]


# Assign points for labs and midterms:
LAB_POINTS = '10'
rename_col(grades, 'Midterm 2', 'Mid2 [' + MID_POINTS + ']')
rename_col(grades, 'Lab 01', 'Lab1 [' + LAB_POINTS + ']')
rename_col(grades, 'Lab 02', 'Lab2 [' + LAB_POINTS + ']')
rename_col(grades, 'Lab 03', 'Lab3 [' + LAB_POINTS + ']')
rename_col(grades, 'Lab 04', 'Lab4 [' + LAB_POINTS + ']')
rename_col(grades, 'Lab 05', 'Lab5 [' + LAB_POINTS + ']')
rename_col(grades, 'Lab 06', 'Lab6 [' + LAB_POINTS + ']')
rename_col(grades, 'Lab 07', 'Lab7 [' + LAB_POINTS + ']')
rename_col(grades, 'Lab 08', 'Lab8 [' + LAB_POINTS + ']')
rename_col(grades, 'Lab 09', 'Lab9 [' + LAB_POINTS + ']')
rename_col(grades, 'Lab 10', 'Lab10 [' + LAB_POINTS + ']')
# grades.head()


# Save intermediate version:
# grades.to_csv("grades4.csv")

# Oops, just realized mid2 isn't fully graded! Better drop it:
# grades.drop('Mid2 [100]', axis=1,  inplace=True)
# grades.head()


# For import to Classes, we don't need 'Total': Classes will total for us!
# But if you want to calc it, do this:

# cols = list(grades.columns)
# del cols[0]
# del cols[1]
# grades['Total'] = grades[cols].sum(axis=1)
# grades["Total"].describe(percentiles=[0, 0.2, 0.4, 0.6, 0.8, 1.0])

# We want to see all the rows we ask for, not just '...':
# pd.set_option('display.max_rows', None)

# Replace all of those `Nan`s:
grades.fillna(0, inplace=True)

# Classes says the first col should be 'Student ID'... 
# not sure if the exact col name matters, but what the hey...
grades.rename(columns =
              {'SID': 'Student ID'},
              inplace = True)
grades.head()


# And now we have a file we can import to NYU Classes... we set `index=False`
# to eliminate the first column of row numbers, which will make the import to Classes fail:
# write grades to stdout so we can see result on terminal first if we wish to.
grades.to_csv(sys.stdout, index=False)
