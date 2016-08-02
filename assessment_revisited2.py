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
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask_and_evaluate(self):
        print self.question
        user_answer = raw_input("> ")
        if user_answer == self.answer:
            return True
        else:
            return False


class Exam(object):
    """ This class Exam is suppose to have an attribute "questions" and take 
        in the name of the exam type at initialization."""

    #initializing an exam
    def __init__(self, name_exam, questions):
        self.name_exam = name_exam
        self.questions = questions

    def add_question(self, question, answer):
        """ Take the question object from class question and initialize here"""
        object_question = Question(question, answer)
        self.questions.append(object_question)

    def administer(self):
        """ Asks the questions in an exam. Evaluate and score"""
        score = 0 
        for question in self.questions:
            question.ask_and_evaluate()
            if True:
                score += 1
        return (float(score)/len(self.questions)) * 100

class Quiz(Exam):
    """ Basically it's inheriting from Exam """

    def administer(self):
        """ Runs the quiz which are questions from exam.
        Tells the teacher if the student passed """
    result = super(Quiz, self). administer()
    if result > 0.5:
        return "This student passed."
    else:
        return "This student failed."


def take_test(student, exam):
    """ student takes the test and their score is recorded """
    student.score = exam.administer()
    print "Your score is %.2f percent." % (student.score)

def example():
    """ Example of a student taking the exam. """

    student = Student('Hillary', 'Clinton', '1600 Pennsylvania Avenue')

    exam = Exam("finals", [])

    exam.add_question(
        'Which cuisine is creme brulee associated with?',
        'French')

    exam.add_question(
        'What part of a creme brulee jiggles when it is done?',
        'center')

    exam.add_question(
        'Candy cap is a _____.',
        'mushroom')

    exam.add_question(
        'When made into desserts, what is the flavor profile of candy cap?',
        'Maple syrup')

    exam.add_question(
        'What kind of sugar is not suitable for brulee-ing?',
        'powdered sugar')

    exam.add_question(
        'What property common to coffee, orange and lime makes them '
        'difficult to turn into creme brullee?',
        'acidic')

    results = quiz.administer()



def quiz_example():
    """ Example of a student taking a quiz """

    quiz = Exam('Weekly_Quiz', [])

    quiz.add_question('Which cuisine is creme brulee associated with?',
        'French')

    quiz.add_question(
        'What part of a creme brulee jiggles when it is done?',
        'center')

    quiz.add_question(
        'Candy cap is a _____.',
        'mushroom')

    quiz.add_question(
        'When made into desserts, what is the flavor profile of candy cap?',
        'Maple syrup')








