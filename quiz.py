from question import Question

question_prompts = [
    "What is the tallest mountain in the world?\n(a) Nanga Parbat\n(b) Mount Everest\n(c) Annapurna I\n\n",
    "Which of these is not a Continent?\n(a) North America \n(b) Antartica \n(c) Mongolia \n\n",
    "What is the fifth planet of our solar system?\n(a) Jupiter\n(b) Saturn\n(c) Pluto\n\n",
]
questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print('You got ' + str(score) + '/' + str(len(questions)) + ' correct!!!')

run_test(questions)