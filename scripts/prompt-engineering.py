from chatgpt_wrapper import ChatGPT
from chatgpt_wrapper.config import Config

main_file=open("../sample-python-data/train0.py","r")
file_contents = main_file.read()

adversary_file=open("../sample-python-data/train1.py","r")
adversary_file_contents = adversary_file.read()


prompt = "Please generate a unit test for the following function:"


config = Config()
config.set('browser.debug', False)
bot = ChatGPT(config)


response = bot.ask(prompt + " \n " + file_contents)
print(response)
# print()


metaPrompt = "Does this description match the following code correctly?"

response = bot.ask(metaPrompt + "\nDescription:\n" + response + "\nCode:\n" +adversary_file_contents)
print(response)

"""
Things to prompt:

Task 1:
a. what does this code do?
b. what happens if we change <input> in some way
c. what is the output if the input is some way
d. what is the type of <variable>
e. how can this function be optimized

Task 2:
a. generate unit tests for this code
b. what kinds of edge cases should we test in this code
c. generate a unit test for if <variable> is <situation>
d. generate an exceptional unit test for the code

Task 3:
a. generate code that is semantically equivalent to <function>
b. generate code that is semantically equivalent to <snippet>
c. how would I rewrite this code and get the same output: <code>



"""
"""
Questions for OH:
1. How do we validate and evaluate the output that chatgpt provides. 
    For instance, how do we run the unit tests that chatgpt has generated if we don't have those requisite files
2. How can we specify inputs to a function programmatically without knowing what they are?
3. The reflection questions seem to be different from the base question for each task. How do we reconcile that?
4. How do we run any of this code in java - it won't compile off the bat?
5. Are we supposed to input the 100 source files manually? 
6. If we do modify the prompt so that it outputs in a format friendly to evaluation 
    (For instance, making every java output the full class with a deterministic class name)
    then we may lose construct validity on testing the output of chatgpt
7. Unclear what kind of code we are supposed to write - how much should the code do? 
    is it just to automate basic workflows, or to do most of the heavy lifting for prompt engineering.
8. Is there feedback available for our paper reviews?
"""