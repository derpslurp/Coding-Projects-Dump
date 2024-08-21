from Questions import Question

question_prompts = [
    'What is 10+3x2?\n(a) 26\n(b) 13\n(c) 16\n\n',
    'If CxC-C is equal to 30, what does C represent?\n(a) 10\n(b) 3\n(c) 6\n\n',
    'If A+A is 6, and BxB is 36, what is AxB?\n(a) 20\n(b) 18\n(c) 36\n\n'
]

questions = [
    Question(question_prompts[0], 'c'),
    Question(question_prompts[1], 'c'),
    Question(question_prompts[2], 'b'),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print('You got ' + str(score) + '/' + str(len(questions)) + ' correct')


run_test(questions)