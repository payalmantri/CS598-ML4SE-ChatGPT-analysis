from chatgpt_wrapper import ChatGPT
from chatgpt_wrapper.config import Config

file=open("../sample-python-data/train0.py","r")
file_contents = file.read()


prompt = "What does the following code do?"


config = Config()
config.set('browser.debug', True)
bot = ChatGPT(config)


response = bot.ask(prompt + " \n " + file_contents)
print(response)