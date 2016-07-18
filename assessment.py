"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   i. Abstraction: We can hide all the messy details of how something works, 
                    simplifying our code.
   ii. Encapsulation: All the things/codes/methods that do the same thing are
                        kept together. "All these codes make shapes, go into
                        a file for shapes."
  iii. Polymorpshism: If a code/method/thing is repeatable throughout, it is 
                        interchangable and can be made into an overarching 
                        method to keep the code simply/dry.

2. What is a class?
   A type/category of things like instances. Whiskers is under Class Cat, Cat is 
   under Class Animal.

3. What is an instance attribute?
    It is a behaviour/quality of that instance.

4. What is a method?
    It is a function defined under a class.

5. What is an instance in object orientation?
    It is when an object(?)/thing has been pass through a class and given attributes.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
    Class attributes are common througout all the instances in that class. 
    Instance attributes are unique to that one instance. 
    "Whiskers is the name of a cat."
    'cat' is a class attribute, species, under the Class Cat.
    'Whiskers' is a unique name to 1 individual in Class Cat.
"""

#import random

class Student(object):
    """ This the class Student that has attributes of first and last names, and
        address."""

    # initializing a student
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """ This is the class Question where there is 1 question and it's
        correct answer (hopefully 1 correct answer)."""

    #initializing a question
    def __init__(self, question_set):
        self.question = question_set[0]
        self.answer = question_set[1]

    def ask_and_evaluate(self):
        print self.question
        user_answer = raw_input("> ")
        if user_answer == self.answer
            print True
        else:
            print False


class Exam(object):
    """ This class Exam is suppose to have an attribute "questions" and take 
        in the name of the exam type at initialization."""

    #initializing an exam
    def __init__(self, name_exam):
        self.name_exam = name_exam
        self.question = []

    def add_question(self, question, correct_answer):
        question_dict = {}
        question_dict[question] = correct_answer
        self.question.append(question_dict)
        return self.question

    def administer(self):
        score = 0 
        for i in range(len(self.question)):
            ask_this = self.question[1]
            answered = Question.ask_and_evaluate(ask_this)
            if answered == True:
                score += 1
            else:
                continue
        return score 


def take_test(student, exam):
    student.score = Exam.administer()
    return student.score








