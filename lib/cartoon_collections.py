
cheeses = ["camembert", "gouda", "cheddar"]
def roll_call_dwarves(dwarf):
    x=1
    for name in dwarf:
        print(f'{x}. {name}')
        x+=1

def summon_captain_planet(planteers):
    return [f'{element.title()}!' for element in planteers]

def long_planeteer_calls(calls_list):
    for call in calls_list:
        if len(call)>4:
            return True
    return False

def find_the_cheese(foods):
    for food in foods:
        if food in cheeses:
            return food
    return None
