from chatgpt_wrapper import OpenAIAPI
from chatgpt_wrapper.core.config import Config
# from chatgpt_wrapper.config import Config
import pandas as pd
import os



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
df = pd.read_excel('milestone-3-java.xlsx')
df
print(df.head())
# print the columns of the dataframe
print(df.columns)

number_of_rows_to_process = 49


def generate_responses(df):
    code = ""
    # if os.path.exists('java-responses'):
    #     os.system('rm -rf java-responses')
    if not os.path.exists('java-responses/task1'):
        os.makedirs('java-responses/task1')
    # iterate over the rows of the dataframe from row 10 to 20
    # for index, row in df.iterrows():
    #     if index< 10 :
    #         continue
    #     if index>20:
    #         break
    for index, row in df.iterrows():
        if index<= 30:
            continue
        if index>number_of_rows_to_process:
            break
        #   if code column is not empty  and not Nan * prompt column does not contain the code
        if row['Code '] != "" and not pd.isnull(row['Code ']): 
            code = row['Code ']
            
        prompt1 =" What do you know abou the following code? \n" + code
        success, response1, message = bot.ask(prompt1)

        control_flow_change_code = row['Changed Control Flow ']
    
        prompt2 =" What do you know abou the following code? \n" + control_flow_change_code
        success, response2, message = bot.ask(prompt2)

        data_flow_change_code = row['Changed Data Flow ']
        prompt3 =" What do you know abou the following code? \n" + data_flow_change_code
        success, response3, message = bot.ask(prompt3)

        prompt4 ="Are the 3 code sninnepts discussed above semantically equivalent? \n"
        success, response4, message= bot.ask(prompt4)

        # create a markdown file with the prompt and the response .
        # put in folder corresponding to the task
    
        with open('java-responses/task1/code-' + str(index) + '.txt', 'w') as f:
            f.write("Prompt:\n" + prompt1 + "\nResponse:\n" + response1)
            print("Prompt:\n" + prompt1 + "\nResponse:\n" + response1)
            f.write("\n-----------------------------------------\n")
            f.write("Prompt:\n" + prompt2 + "\nResponse:\n" + response2)
            f.write("\n-----------------------------------------\n")
            f.write("Prompt:\n" + prompt3 + "\nResponse:\n" + response3)
            f.write("\n-----------------------------------------\n")
            f.write("Prompt:\n" + prompt4 + "\nResponse:\n" + response4)
            
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