from chatterbot import ChatBot

def train(chatbot):
	chatbot.train("chatterbot.corpus.english")

def execute(chatbot):
	while 1:
		question = input("Me: ")
		response = chatbot.get_response(question)
		print("Ron: ", response)

def script(chatbot):
	print ("1 - Execute");
	print ("9 - Train");
	op = input()

	if op == '1':
		execute(chatbot)

	elif op == '9':
		train(chatbot)

	else:
		print("Invalid option!\n")
		script()
