import pandas as pd
from chatgpt_wrapper import ChatGPT
from chatgpt_wrapper.config import Config
import os

prompt1 = "Given that the following code should do the following task, is the code buggy or not?\n"
prompt2 = "\nThe code I provided above is buggy. Where is the bug?\n"

config = Config()
config.set('browser.debug', False)
bot = ChatGPT(config)
sample_data_dir = '../sample-python-data/'
output_dir = '../milestone3_2_responses/'
force_overwrite = False

# Load the Excel file
excel_file = pd.ExcelFile('../milestone2-responses.xlsx')

# Load the "PYTHON" sheet into a pandas dataframe
df = pd.read_excel(excel_file, sheet_name='PYTHON')

# Filter the dataframe to only include rows where TASK1 is TRUE and IsFollowup is FALSE
df_filtered = df.loc[(df['TASK1'] == True) & (df['IsFollowup'] == False)]

# Loop through the filtered dataframe and call doStringStuff() on each row's "Response" column
output_strings = []
for index, row in df_filtered.iterrows():
    resp = row['Response']
    filename = row['Filename']
    # print("filename", filename)
    # print("resp", resp)
    mutation_nums = ['2','3','4','5','6']

    for num in mutation_nums:
        
        mutated_file = filename[:-3] + ' copy '+ str(num) +'.py'

        if not os.path.isfile(os.path.join(sample_data_dir, mutated_file)):
            continue

        if not force_overwrite:
            if os.path.isfile(os.path.join(output_dir,f"M3_2_{mutated_file}_response.txt")):
                continue
        
        print("mutated_file", mutated_file)
        with open(os.path.join(sample_data_dir, mutated_file), 'r') as f1:
            text1 = f1.read()
        full_prompt = prompt1 + "\nTask:\n" + resp + "\nCode:\n" + text1 + "\n"

        output_string1 = bot.ask(full_prompt)

        output_string2 = bot.ask(prompt2)

        with open(os.path.join(output_dir,f"M3_2_{mutated_file}_response.txt"), 'w') as file:
            file.write(full_prompt)
            file.write(output_string1)
            file.write(prompt2)
            file.write(output_string2)
