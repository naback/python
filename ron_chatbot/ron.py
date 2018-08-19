from chatterbot import ChatBot

def train():
	chatbot.train("chatterbot.corpus.english")

def execute():
	while 1:
		question = input("Me: ")
		response = chatbot.get_response(question)
		print("Ron: ", response)

def script():
	print ("1 - Execute");
	print ("9 - Train");
	op = input()

	if op == '1':
		execute()

	elif op == '9':
		train()

	else:
		print("Invalid option!\n")
		script()


#====================================================================================================


chatbot = ChatBot(
    'Ron',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

script()
