from chatterbot import ChatBot

chatbot = ChatBot(
    'Ron',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

print ("1 - Executar");
print ("2 - Treinar");
op = input()

if op == '1':
	execute()

it op == '2':
	train()

def train():
	chatbot.train("chatterbot.corpus.english")

def execute():
	question = input("Eu: ")
	response = chatbot.get_response(question)
	print("Ron: ", response)
