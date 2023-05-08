from chatgpt_wrapper import OpenAIAPI
from chatgpt_wrapper.core.config import Config
# from chatgpt_wrapper.config import Config
import pandas as pd
import os
import math



prompt = "What do you know about code execution? " 


config = Config()
config.set('browser.debug', False)
bot = OpenAIAPI(config)


success, response, message = bot.ask(prompt )
print(response)
print ("------------------")

# print()


# metaPrompt = "Does this description match the following code correctly?"

# response = bot.ask(metaPrompt + "\nDescription:\n" + response + "\nCode:\n" +adversary_file_contents)
# print(response)


# open the excel file and read the contents into pandas dataframe
df = pd.read_excel('milestone-3-java-context.xlsx')
df
print(df.head())
# print the columns of the dataframe
print(df.columns)
startIndex = 0
endIndex = 1


def generate_responses(df):
    code = ""
    # if os.path.exists('java-responses'):
    #     os.system('rm -rf java-responses')
    if not os.path.exists('java-responses/task2'):
        os.makedirs('java-responses/task2')

    for index, row in df.iterrows():
        if index< startIndex:
            continue
        if index>endIndex:
            break
        #   if code column is not empty  and not Nan * prompt column does not contain the code

        context = row['Context']
            
        for i in range(1,6):
            mutant = row['Mutant ' + str(i)]
            print(mutant, context)
            # check if mutant or conext is not empty and not Nan and not null
            if (isinstance(mutant, float) and math.isnan(mutant)) or (isinstance(context, float) and math.isnan(context)):
                continue
            
            prompt1 ="Is the following code buggy or correct? \n" + mutant + "\n" + context 
            success, response1, message = bot.ask(prompt1)
            prompt2 = "The following code is buggy. Can you spot the statements involved in the bug?"+ "\n" + mutant
            success, response2, message = bot.ask(prompt2)

            # create a markdown file with the prompt and the response .
            # put in folder corresponding to the task

            if os.path.exists('java-responses/task2/code-' + str(index) + '.txt'):
                mode = 'a'
            else:
                mode = 'w'
            with open('java-responses/task2/code-' + str(index) + '.txt', mode, encoding="utf8") as f:
                f.write("\n Mutant " + str(i) + "\n")
                f.write("Prompt:\n" + prompt1 + "\nResponse:\n" + response1)
                f.write("\n-----------------------------------------\n")
                f.write("Prompt:\n" + prompt2 + "\nResponse:\n" + response2)
                f.write("\n-----------------------------------------\n")
                
                f.write("\n-----------------------------------------\n")
                f.close()
        print("Completed processing row " + str(index))


# generate responses for the  number_of_rows_to_process rows
generate_responses(df)





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