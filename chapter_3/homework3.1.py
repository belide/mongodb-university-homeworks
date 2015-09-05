#!/usr/bin/python

import pymongo
import sys

# Homework 2.2 Course M101P
#
# Write a program in the language of your choice that
# will remove the lowest homework score for each student.
# Since there is a single document for each student containing
# an array of scores, you will need to update the scores array
# and remove the homework.

def score_without_lowest_homework(scores):
    homework_scores = [score for score in scores if score['type'] == 'homework']
    lowest_score = min([score['score'] for score in homework_scores])

    scores = [score for score in scores \
                 if score['type'] != 'homework' \
                 or score['type'] == 'homework' and score['score'] != lowest_score]

    return scores

def update_scores(collection, _id, new_scores):
    collection.update({'_id': _id}, {'$set': {'scores': new_scores}})

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.school
students = db.students

cursor = students.find({'scores.type': 'homework'})

for student in cursor:
    student_scores = student['scores']

    new_student_scores = score_without_lowest_homework(student_scores)
    update_scores(students, student['_id'], new_student_scores)
