import player
import question


question1=question.Question("The best country in the world is Romania",'t')
question2=question.Question('The capital of Egypt is Cairo','t')
question3=question.Question('Neptune is the 6th planet in the solar system','f')
question4=question.Question("I am a smart computer",'t')

question_list=[question1,question2,question3,question4]

print("Welcome to the quiz!")
player=player.Player()
for question in question_list:
    print(question.text)
    option = input("Is the anwer True or False?(t/f)")
    if option==question.answer:
        player.correct_answer()
        print('Correct!')
    else:
        player.wrong_answer()
        print('Wrong')

print("You finished the quiz!")
print("Your score: "+str(player.score)+'/'+str(player.questions_answered))

