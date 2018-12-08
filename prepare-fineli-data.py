from collections import OrderedDict

foodfile = "Fineli_Rel19_open/food.csv"
componentfile = "Fineli_Rel19_open/component_value.csv"

eufdnames = [ 'ENERC', 'CHOAVL', 'FAT', 'PROT', 'FIBC', 'STARCH', 'SUGAR', 'FASAT', 'NACL' ]
# ENERC	energia, laskennallinen
# CHOAVL	hiilihydraatti imeytyvä
# FAT	rasva
# PROT	proteiini
# FIFIBC	kuitu, kokonais-
# STARCH	tärkkelys
# SUGAR	sokerit
# FASAT	rasvahapot tyydyttyneet
# NACL	suola

default_value = '0'

def main():
    """ Reads Fineli database files and combines relevant data into a single file. """

    foods = OrderedDict()

    # 1. read food names
    with open(foodfile, 'r') as file_foods:
        for idx, row in enumerate(file_foods):
            if idx == 0:
                continue

            columns = row.split(";")
            food_id = int(columns[0])
            food_name = columns[1].lower()
            foods[food_id] = {'FOODNAME': food_name}
    
    # 2. from component file add fields mentioned in eufdnames to data
    with open(componentfile, 'r') as file_components:
        for idx, row in enumerate(file_components):
            if idx == 0:
                continue

            columns = row.split(";")
            food_id = int(columns[0])
            eufdname = columns[1]
            value = columns[2].replace(",", ".")
            
            if food_id in foods and eufdname in eufdnames:
                item = { eufdname: value }
                combination = { **foods[food_id], **item }
                foods[food_id] = combination 

    # 3. save data
    sort_order = ['FOODNAME'] + eufdnames
    sort_order = eufdnames
    print(";".join(sort_order))
    for row in foods.values():
        row_items = [row.get(x, default_value) for x in sort_order]
        print(";".join(row_items))

if __name__ == "__main__":
    main()
