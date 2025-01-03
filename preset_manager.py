import sqlite3
import os
from input_data_cleaners import clean_input_elements_list, clean_input_payloads_list

# web parameter formatting was quite large, due to which needed a seperate function. for easiness in maintenance
def format_to_string_params(params_list:list):
    formatted_data = []
    for item in params_list:
        for key, inner_dict in item.items():
            for inner_key, inner_value in inner_dict.items():
                formatted_data.append(f"{key}|||{inner_key}|||{inner_value}")
    return formatted_data

# inverse of the web parameter formatting 
def inverse_of_web_parameter_formatting(formatted_data:str, url:str):
    parsed_list = []

    formatted_data = formatted_data.split("///")
    
    # # iterate over the data, and create a dictionary, similiar to the original one
    for i in formatted_data:
        i = str(i).split("|||")
        d = {}
        d["for site"] = url
        d["type"] = i[0]
        d["param"] = i[1]
        d["param value"] = i[2]

        parsed_list.append(d)


    return parsed_list


# function that creates presets
def create_preset(preset_name:str,
                  url_list:list,
                  elements:list,
                  payloads:list):
    cur_dir = os.getcwd().replace('\\core', '')

    # initializing the connection and the cursor
    db = sqlite3.connect(f"{cur_dir}\\data\\presets\\presets.db")
    c = db.cursor()    

    # checking if a table exists or not, else creating one
    c.execute("""
        CREATE TABLE IF NOT EXISTS Presets (
                preset_name VARCHAR,
                url VARCHAR,
                request_type CHAR(100),
                elements VARCHAR,
                parameters VARCHAR)
    """)

    if elements != []:
        cleaned_elements_list = clean_input_elements_list(element_list=elements, url_list=url_list)
    else:
        cleaned_elements_list = "NaN"

    # cleaning the inputs
    cleaned_parameters_list = clean_input_payloads_list(payload_list=payloads)

    for item in cleaned_parameters_list:
        del item['for site']
        
    cleaned_parameters_list = format_to_string_params(cleaned_parameters_list)

    # iterate over the dictionary recieved by the cleaned elements, if there are any elements
    if cleaned_elements_list != "NaN":
        for item in cleaned_elements_list:
            url = item['url']
            req_type = url_list[0]['request type']
            elems = item['elements']
            elems = [f"{i['name']}|{i['attribute']}|{i['attribute value']}" for i in elems]

            # concatenate all the list items, so that it fits into one row
            elems = "/|\\".join(i for i in elems)
            cleaned_parameters_list = "///".join(i for i in cleaned_parameters_list)

            c.execute(f"""INSERT INTO Presets VALUES ('{preset_name}', '{url}', '{req_type}', '{elems}', '{cleaned_parameters_list}')""")

            db.commit()
            db.close()
    # else just set the elements to Null
    else:
        url = url_list[0]['url']
        req_type = url_list[0]['request type']
        elems = "Null"

        # concatenate all the list items, so that it fits into one row
        cleaned_parameters_list = "///".join(i for i in cleaned_parameters_list)

        c.execute(f"""INSERT INTO Presets VALUES ('{preset_name}', '{url}', '{req_type}', '{elems}', '{cleaned_parameters_list}')""")

        db.commit()
        db.close()


def load_preset(preset_name:str):
    cur_dir = os.getcwd().replace('\\core', '')

    db = sqlite3.connect(f"{cur_dir}\\data\\presets\\presets.db")
    c = db.cursor()

    c.execute(f"""SELECT * FROM Presets WHERE preset_name = '{preset_name}'""")

    return c.fetchone()


def load_all_presets():
    cur_dir = os.getcwd().replace('\\core', '')

    db = sqlite3.connect(f"{cur_dir}\\data\\presets\\presets.db")
    c = db.cursor()

    check = c.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='Presets';""").fetchone()
    if not check:
        return "Table doesnt exist"
    else:
        c.execute("""SELECT * FROM Presets;""")

        return c.fetchall()
    

def delete_presets(preset_name:str):
    cur_dir = os.getcwd().replace('\\core', '')

    db = sqlite3.connect(f"{cur_dir}\\data\\presets\\presets.db")
    c = db.cursor()

    c.execute(f"""DELETE FROM Presets WHERE preset_name = '{preset_name}'""")

    db.commit()
    db.close()