import random
import os

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(35):
    #Creating new quiz files and naming them according to serial number
    quizFile = open('capital_quizes%s.txt' % (quizNum + 1), 'w')
    #Creating new answer files and naming them according to serial number
    answerKeyFile = open('capital_quizes_answers%s.txt' % (quizNum + 1), 'w')
    #Adding Name Date and Period 
    quizFile.write('Name\n\nDate:\n\nPeriod\n\n')
    #Adding titles of each quiz file 
    quizFile.write((' '*20), 'State Capital Quiz (Form%s)' % (quizNum + 1))
    quizFile.write('\n\n')
    #creating the question paper
    states = list(capitals.keys())
    random.shuffle(states)
    #Creating the question paper
    for questionNum in range(50):
        #Making list of correct answers
        correctAnswer = capitals[states[questionNum]]
        #Making list of wrong answers
        wrongAnswers = list(capitals.values())
        #Deleteing the right answer form the wrong answers list
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        #randomly picking up wrong answers to display as option under each question
        wrongAsnwers = random.sample(wrongAnswers, 3)
        #list of options to be displayed under each question
        answersOptions = wrongAsnwers + [correctAnswer]
        #Randomly shuffling them
        random.shuffle(answersOptions)

        #Writing the question into the file
        quizFile.write('%s, What is the capital os %s\n' % (questionNum + 1, states[questionNum]))
        #Creating options
        for i in range(4):
            quizFile.write('    %s. %s[n]'%('ABCD'[i], answersOptions[i]))
        quizFile.write('\n')
        #Simultaneously adding the answers in Answers File created earlier
        answerKeyFile.write('%s. %s\n'% (questionNum + 1, 'ABCD'[answersOptions.index(correctAnswer)]))
quizFile.close()
answerKeyFile.close()



