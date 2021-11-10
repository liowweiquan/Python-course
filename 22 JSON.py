>>> r.status_code
200
>>> r.text
'{"response_code":0,"results":[{"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"What geometric shape is generally used for stop signs?","correct_answer":"Octagon","incorrect_answers":["Hexagon","Circle","Triangle"]},{"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"Which one of the following rhythm games was made by Harmonix?","correct_answer":"Rock Band","incorrect_answers":["Meat Beat Mania","Guitar Hero Live","Dance Dance Revolution"]},{"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"What type of animal was Harambe, who was shot after a child fell into it&#039;s enclosure at the Cincinnati Zoo?","correct_answer":"Gorilla","incorrect_answers":["Tiger","Panda","Crocodile"]},{"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"What is Tasmania?","correct_answer":"An Australian State","incorrect_answers":["A flavor of Ben and Jerry&#039;s ice-cream","A Psychological Disorder","The Name of a Warner Brothers Cartoon Character"]},{"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"Which candy is NOT made by Mars?","correct_answer":"Almond Joy","incorrect_answers":["M&amp;M&#039;s","Twix","Snickers"]},{"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"Which of the following is the IATA code for Manchester Airport?","correct_answer":"MAN","incorrect_answers":["EGLL","LHR","EGCC"]},{"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"Who is the youngest person to recieve a Nobel Prize?","correct_answer":"Malala Yousafzai","incorrect_answers":["Lawrence Bragg","Werner Heisenberg","Yasser Arafat"]},{"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"What is the French word for &quot;fish&quot;?","correct_answer":"poisson","incorrect_answers":["fiche","escargot","mer"]},{"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"When was the Playstation 3 released?","correct_answer":"November 11, 2006","incorrect_answers":["January 8, 2007","December 25, 2007","July 16, 2006"]},{"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"Who invented the first ever chocolate bar, in 1847?","correct_answer":"Joseph Fry","incorrect_answers":["Andrew Johnson","John Cadbury","John Tyler"]}]}'
>>> type(r.text)
<class 'str'>
>>> import json
>>> question = json.load(r.text)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    question = json.load(r.text)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/json/__init__.py", line 293, in load
    return loads(fp.read(),
AttributeError: 'str' object has no attribute 'read'
>>> question = json.loads(r.text)
>>> question
{'response_code': 0, 'results': [{'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'easy', 'question': 'What geometric shape is generally used for stop signs?', 'correct_answer': 'Octagon', 'incorrect_answers': ['Hexagon', 'Circle', 'Triangle']}, {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'easy', 'question': 'Which one of the following rhythm games was made by Harmonix?', 'correct_answer': 'Rock Band', 'incorrect_answers': ['Meat Beat Mania', 'Guitar Hero Live', 'Dance Dance Revolution']}, {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'easy', 'question': 'What type of animal was Harambe, who was shot after a child fell into it&#039;s enclosure at the Cincinnati Zoo?', 'correct_answer': 'Gorilla', 'incorrect_answers': ['Tiger', 'Panda', 'Crocodile']}, {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'easy', 'question': 'What is Tasmania?', 'correct_answer': 'An Australian State', 'incorrect_answers': ['A flavor of Ben and Jerry&#039;s ice-cream', 'A Psychological Disorder', 'The Name of a Warner Brothers Cartoon Character']}, {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'easy', 'question': 'Which candy is NOT made by Mars?', 'correct_answer': 'Almond Joy', 'incorrect_answers': ['M&amp;M&#039;s', 'Twix', 'Snickers']}, {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'easy', 'question': 'Which of the following is the IATA code for Manchester Airport?', 'correct_answer': 'MAN', 'incorrect_answers': ['EGLL', 'LHR', 'EGCC']}, {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'easy', 'question': 'Who is the youngest person to recieve a Nobel Prize?', 'correct_answer': 'Malala Yousafzai', 'incorrect_answers': ['Lawrence Bragg', 'Werner Heisenberg', 'Yasser Arafat']}, {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'easy', 'question': 'What is the French word for &quot;fish&quot;?', 'correct_answer': 'poisson', 'incorrect_answers': ['fiche', 'escargot', 'mer']}, {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'easy', 'question': 'When was the Playstation 3 released?', 'correct_answer': 'November 11, 2006', 'incorrect_answers': ['January 8, 2007', 'December 25, 2007', 'July 16, 2006']}, {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'easy', 'question': 'Who invented the first ever chocolate bar, in 1847?', 'correct_answer': 'Joseph Fry', 'incorrect_answers': ['Andrew Johnson', 'John Cadbury', 'John Tyler']}]}
>>> type(question)
<class 'dict'>
>>> import print
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    import print
ModuleNotFoundError: No module named 'print'
>>> import pprint
>>> pprint.pprint(question)
{'response_code': 0,
 'results': [{'category': 'General Knowledge',
              'correct_answer': 'Octagon',
              'difficulty': 'easy',
              'incorrect_answers': ['Hexagon', 'Circle', 'Triangle'],
              'question': 'What geometric shape is generally used for stop '
                          'signs?',
              'type': 'multiple'},
             {'category': 'General Knowledge',
              'correct_answer': 'Rock Band',
              'difficulty': 'easy',
              'incorrect_answers': ['Meat Beat Mania',
                                    'Guitar Hero Live',
                                    'Dance Dance Revolution'],
              'question': 'Which one of the following rhythm games was made by '
                          'Harmonix?',
              'type': 'multiple'},
             {'category': 'General Knowledge',
              'correct_answer': 'Gorilla',
              'difficulty': 'easy',
              'incorrect_answers': ['Tiger', 'Panda', 'Crocodile'],
              'question': 'What type of animal was Harambe, who was shot after '
                          'a child fell into it&#039;s enclosure at the '
                          'Cincinnati Zoo?',
              'type': 'multiple'},
             {'category': 'General Knowledge',
              'correct_answer': 'An Australian State',
              'difficulty': 'easy',
              'incorrect_answers': ['A flavor of Ben and Jerry&#039;s '
                                    'ice-cream',
                                    'A Psychological Disorder',
                                    'The Name of a Warner Brothers Cartoon '
                                    'Character'],
              'question': 'What is Tasmania?',
              'type': 'multiple'},
             {'category': 'General Knowledge',
              'correct_answer': 'Almond Joy',
              'difficulty': 'easy',
              'incorrect_answers': ['M&amp;M&#039;s', 'Twix', 'Snickers'],
              'question': 'Which candy is NOT made by Mars?',
              'type': 'multiple'},
             {'category': 'General Knowledge',
              'correct_answer': 'MAN',
              'difficulty': 'easy',
              'incorrect_answers': ['EGLL', 'LHR', 'EGCC'],
              'question': 'Which of the following is the IATA code for '
                          'Manchester Airport?',
              'type': 'multiple'},
             {'category': 'General Knowledge',
              'correct_answer': 'Malala Yousafzai',
              'difficulty': 'easy',
              'incorrect_answers': ['Lawrence Bragg',
                                    'Werner Heisenberg',
                                    'Yasser Arafat'],
              'question': 'Who is the youngest person to recieve a Nobel '
                          'Prize?',
              'type': 'multiple'},
             {'category': 'General Knowledge',
              'correct_answer': 'poisson',
              'difficulty': 'easy',
              'incorrect_answers': ['fiche', 'escargot', 'mer'],
              'question': 'What is the French word for &quot;fish&quot;?',
              'type': 'multiple'},
             {'category': 'General Knowledge',
              'correct_answer': 'November 11, 2006',
              'difficulty': 'easy',
              'incorrect_answers': ['January 8, 2007',
                                    'December 25, 2007',
                                    'July 16, 2006'],
              'question': 'When was the Playstation 3 released?',
              'type': 'multiple'},
             {'category': 'General Knowledge',
              'correct_answer': 'Joseph Fry',
              'difficulty': 'easy',
              'incorrect_answers': ['Andrew Johnson',
                                    'John Cadbury',
                                    'John Tyler'],
              'question': 'Who invented the first ever chocolate bar, in 1847?',
              'type': 'multiple'}]}
>>> question['results'][0]['category']
'General Knowledge'
>>> questions['results'][1]['category']
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    questions['results'][1]['category']
NameError: name 'questions' is not defined
>>> question['results'][0]['incorrect_answers']
['Hexagon', 'Circle', 'Triangle']
>>> person ={'Name': 'John', 'Age':30}
>>> person_json = json.dumps(person)
>>> person_json
'{"Name": "John", "Age": 30}'
>>> person.append('Jack")
	      
SyntaxError: EOL while scanning string literal
>>> person.append('Jack')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    person.append('Jack')
AttributeError: 'dict' object has no attribute 'append'
>>> person  {'Name': 'John', 'Jack', 'Age':30, 33}
SyntaxError: invalid syntax
>>> person = {'Name': 'John', 'Jack', 'Age':30, 33}
SyntaxError: invalid syntax
>>> questions['results'][1]['incorrect_ansers']
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    questions['results'][1]['incorrect_ansers']
NameError: name 'questions' is not defined
>>> 
