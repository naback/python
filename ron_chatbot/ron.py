from chatterbot import ChatBot
import methods

chatbot = ChatBot(
    'Ron',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

methods.script(chatbot)
