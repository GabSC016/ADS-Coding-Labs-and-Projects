# Lab: 
# In this lab you will practice the basics of Python by building a small app that creates a character for an RPG adventure.

full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    
    elif name == '':
        return "The character should have a name"
    
    elif len(name) > 10:
        return "The character name is too long"

    elif " " in name:
        return "The character name should not contain spaces"

    elif not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return "All stats should be integers"
    
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"

    elif strength > 4 or intelligence > 4 or charisma > 4 :
        return"All stats should be no more than 4"
    
    elif strength + intelligence + charisma != 7:
        return "The character should start with 7 points"
    
    else:
        def dots_bar(int_dot):
            bar_empty_dot = '○○○○○○○○○○'
            bar_full_dot = '●●●●●●●●●●'
            return f"{bar_full_dot[:int_dot] + bar_empty_dot[int_dot:]}"
        
        return f"{name}\nSTR {dots_bar(strength)}\nINT {dots_bar(intelligence)}\nCHA {dots_bar(charisma)}"

print(create_character('ren', 4, 2, 1))

