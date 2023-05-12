"""
What does the following code do
Is the above code equivalent to the following code

"""
from chatgpt_wrapper import ChatGPT
from chatgpt_wrapper.config import Config
import os

'''
will they produce the same output in nominal cases of execution?
ignoring error cases, and library differences, will these two programs produce the same output?
2, 7, 9, 14, 15, 18, 20, 22, 23, 28, 29-33, 39, 40, 49

write a test case where the codes would have different outputs
what cases would the codes have different outputs?
would the codes be the same under nominal cases of execution?
what are the error cases that would cause the codes to have different outputs?
under what input data would the outputs be different?
ask about the difference in outputs between the two codes...

"semantically equivalent" needs to be defined as invariant outputs between 2 codes. 
just because they use different algorithms doesn't mean they're not semantically equivalent.    
'''




def run(): 
        # specify the directory containing the files
    directory = '../sample-python-data/'
    prompt1 = "What does the following code do? \n"
    prompt2 = "Is the above code equivalent to the following code? \n"
    config = Config()
    config.set('browser.debug', False)
    bot = ChatGPT(config)


    # loop through all files in the directory
    for filename1 in os.listdir(directory):
        # check if the file 1 name matches the pattern "train<number1>  Copy.py"
        # print(filename1)
        if filename1.startswith('train') and filename1.endswith(' copy.py'):
            print(filename1)
            try:
                # extract the value of number1 from the file 1 name
                number1 = int(filename1.split('train')[1].split(' copy.py')[0])
            except ValueError:
                # skip this file if number1 is not an integer
                continue
            
            # construct the file 2 name
            filename2 = f'train{number1}.py'
            
            # check if file 2 exists in the directory
            if not os.path.isfile(os.path.join(directory, filename2)):
                continue
            
            # read the text of file 1 and file 2
            with open(os.path.join(directory, filename1), 'r') as f1, open(os.path.join(directory, filename2), 'r') as f2:
                text1 = f1.read()
                text2 = f2.read()
            
            # call the doStringStuff function on the two texts
            output1 = bot.ask(prompt1 + text1)
            output2 = bot.ask(prompt2 + text2)
            
            # construct the output file name
            output_filename = f'../milestone3_1_responses/train{number1}_m3t1.txt'
            
            # write the output strings to the output file
            with open(output_filename, 'w') as f:
                f.write(prompt1 + output1 + '\n' + prompt2+output2)


if __name__ == '__main__':
    run()