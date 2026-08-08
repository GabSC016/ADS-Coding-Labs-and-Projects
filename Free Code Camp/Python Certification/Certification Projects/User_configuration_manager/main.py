test_settings = {'volume' : 'low'}

def add_setting(dic_set, key_value):

    # Converte valores para minúsculo

    key = key_value[0].lower()
    value = key_value[1].lower()

    # Verifica se a chave existe no dicionário e adiciona

    if key in dic_set.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    elif not key in dic_set.keys():
        dic_set.update({key : value})
        return f"Setting '{key}' added with value '{value}' successfully!"
        

def update_setting(dic_set, key_value):

    key = key_value[0].lower()
    value = key_value[1]. lower()

    if key in dic_set.keys():
        dic_set.update({key : value})
        return f"Setting '{key}' updated to '{value}' successfully!"
    
    elif not key in dic_set.keys():
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dic_set, key):
    key = key.lower()


    if key in dic_set.keys():
        dic_set.pop(key)
        return f"Setting '{key}' deleted successfully!"
    
    if not key in dic_set.keys():
        return f"Setting not found!"

def view_settings(dic_set):
    if not dic_set:
        return "No settings available."
    else:
        view_set = "Current User Settings:\n"

        for key, value in dic_set.items():
            view_set += f"{key.capitalize()}: {value}\n"
        
        return view_set
        

print(view_settings({'theme': 'light', 'volume':'low'}))