#!/usr/bin/python
# -*- coding: UTF8 -*-

import pymongo
import sys

# Homework 2.2 · Course M101P
#
# Write a program in the language of your choice that will remove the grade
# of type "homework" with the lowest score for each student from the dataset
# that you imported in HW 2.1. Since each document is one grade, it should
# remove one document per student.

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.students
grades = db.grades

cursor = grades.find({'type': 'homework'}).sort([('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING)])

student_id = None
previous_student_id = None

for document in cursor:
    student_id = document['student_id']

    if student_id != previous_student_id:
        previous_student_id = student_id
        grades.remove({'_id': document['_id']})
