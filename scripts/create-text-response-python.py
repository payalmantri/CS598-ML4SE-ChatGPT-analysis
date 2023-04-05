
import pandas as pd
import os





# open the excel file and read the contents into pandas dataframe
df = pd.read_excel('milestone2-responses.xlsx', sheet_name='PYTHON')
df
print(df.head())

number_of_rows_to_process = 15



def generate_responses(df):
    code = ""
    codeindex =0
    if os.path.exists('python-responses'):
        os.system('rm -rf python-responses')


    # create a folder for each task


    if not os.path.exists('python-responses/task1'):
        os.makedirs('python-responses/task1')
    if not os.path.exists('python-responses/task2'):
        os.makedirs('python-responses/task2')
    if not os.path.exists('python-responses/task3'):
        os.makedirs('python-responses/task3')

    # iterate over the rows of the dataframe from row 2
    for index, row in df.iterrows():  
        # if more than 10 rows have been processed, break
        
        if index > number_of_rows_to_process:
            break
        #   if code column is not empty  and not Nan * prompt column does not contain the code
        filename = row['Filename']
        # get the code from the file
        code_file = open("sample-python-data/" + filename, "r")
        code = code_file.read()
        # close the file
        code_file.close()
        #  get codeindex from the filename train0.py -> 0
        codeindex = filename.split('.')[0].split('train')[1]
        if(row['IsFollowup']==True):
            code = ""
        prompt1 = row['Prompt'] 
        if prompt1.find(code) == -1:
            prompt1 = prompt1 + "\nCode:\n" + code
        response = row['Response'] 
        task1 = row['TASK1']
        task2 = row['TASK2']
        task3 = row['TASK3']
        # create a markdown file with the prompt and the response . 
        # put in folder corresponding to the task
        # deltel python-responses folder if it exists recursively
      
        if(task1 == True):
            # check if the file exists, if it does, append to it
            if os.path.exists('python-responses/task1/code-' + str(codeindex) + '.txt'):
                mode = 'a'
            else:
                mode = 'w'
            with open('python-responses/task1/code-' + str(codeindex) + '.txt', mode) as f:
                # write promt in heading 6
                f.write("\n-----------------------------------------\n")
                f.write(" Prompt: " +prompt1 + '\n\n')
                # write resposnse as highlighted text
                f.write("-----------------------------------------\n")
                f.write('ChatGPT response: ' + response + '\n')


                f.close()
        elif(task2 == True):
             # check if the file exists, if it does, append to it
            if os.path.exists('python-responses/task2/code-' + str(codeindex) + '.txt'):
                mode = 'a'
            else:
                mode = 'w' 

            with open('python-responses/task2/code-' + str(codeindex) + '.txt', mode) as f:
                f.write("\n-----------------------------------------")
                f.write( "\n Prompt: " +prompt1 + '\n')
                f.write("-----------------------------------------\n")
                f.write('ChatGPT response: ' + response + '\n')
                
                f.close()
        elif(task3 == True):
            # check if the file exists, if it does, append to it
            if os.path.exists('python-responses/task1/code-' + str(codeindex) + '.txt'):
                mode = 'a'
            else:
                mode = 'w'
            with open('python-responses/task3/code-' + str(codeindex) + '.txt', mode) as f:
                # write promt in heading 6
                f.write("\n----------------------------------------")
                f.write("\n Prompt: " +prompt1 + '\n')
                f.write("-----------------------------------------\n")
                f.write('ChatGPT response: ' + response + '\n')

                f.close()
        else:
            print("No task found for this row"+ str(index))
        


# generate responses for the  number_of_rows_to_process rows
generate_responses(df)



