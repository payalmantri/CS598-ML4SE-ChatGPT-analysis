
import pandas as pd
import os





# open the excel file and read the contents into pandas dataframe
df = pd.read_excel('milestone2-responses.xlsx')
df
print(df.head())

number_of_rows_to_process = 15



def generate_responses(df):
    code = ""
    codeindex =0
    if os.path.exists('java-responses'):
        os.system('rm -rf java-responses')


    # create a folder for each task


    if not os.path.exists('java-responses/task1'):
        os.makedirs('java-responses/task1')
    if not os.path.exists('java-responses/task2'):
        os.makedirs('java-responses/task2')
    if not os.path.exists('java-responses/task3'):
        os.makedirs('java-responses/task3')

    # iterate over the rows of the dataframe from row 2
    for index, row in df.iterrows():  
        # if more than 10 rows have been processed, break
        if index > number_of_rows_to_process:
            break
        #   if code column is not empty  and not Nan * prompt column does not contain the code
        print("code: " ,row['Code']  )
        if  not pd.isnull(row['Code']) :
            code = row['Code']
            codeindex = codeindex + 1
            print(code, codeindex)
        prompt1 = row['Prompt'] + "\nCode:\n" 
        if prompt1.find(code) == -1:
            prompt1 = prompt1 + code
        response = row['Actual Response from Browser'] 
        task1 = row['TASK1']
        print(task1)
        task2 = row['TASK2']
        task3 = row['TASK3']
        # create a markdown file with the prompt and the response . 
        # put in folder corresponding to the task
        # deltel java-responses folder if it exists recursively
      
        if(task1 == True):
            # check if the file exists, if it does, append to it
            if os.path.exists('java-responses/task1/code-' + str(codeindex) + '.txt'):
                mode = 'a'
            else:
                mode = 'w'
            with open('java-responses/task1/code-' + str(codeindex) + '.txt', mode) as f:
                # write promt in heading 6
                f.write("\n-----------------------------------------\n")
                f.write(" Prompt: " +prompt1 + '\n\n')
                # write resposnse as highlighted text
                f.write("-----------------------------------------\n")
                f.write('ChatGPT response: ' + response + '\n')


                f.close()
        elif(task2 == True):
             # check if the file exists, if it does, append to it
            if os.path.exists('java-responses/task2/code-' + str(codeindex) + '.txt'):
                mode = 'a'
            else:
                mode = 'w' 

            with open('java-responses/task2/code-' + str(codeindex) + '.txt', mode) as f:
                f.write("\n-----------------------------------------")
                f.write( "\n Prompt: " +prompt1 + '\n')
                f.write("-----------------------------------------\n")
                f.write('ChatGPT response: ' + response + '\n')
                
                f.close()
        elif(task3 == True):
            # check if the file exists, if it does, append to it
            if os.path.exists('java-responses/task1/code-' + str(codeindex) + '.txt'):
                mode = 'a'
            else:
                mode = 'w'
            with open('java-responses/task3/code-' + str(codeindex) + '.txt', mode) as f:
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



