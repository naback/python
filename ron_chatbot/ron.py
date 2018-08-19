from chatterbot import ChatBot

def train():
	chatbot.train("chatterbot.corpus.english")

def execute():
	while 1:
		question = input("Me: ")
		response = chatbot.get_response(question)
		print("Ron: ", response)

chatbot = ChatBot(
    'Ron',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

print ("1 - Execute");
print ("9 - Train");
op = input()

if op == '1':
	execute()

if op == '9':
	train()


