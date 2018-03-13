""" A Rolodex Full of Friends """

# dictionary of name/number pairs
rolodex = {'Aaron'  : 5556069,
           'Bill'   : 5559824,
           'Dad'    : 5552603,
           'David'  : 5558331,
           'Dillon' : 5553538,
           'Jim'    : 5555547,
           'Mom'    : 5552603,
           'Olivia' : 5556397,
           'Verne'  : 5555309}

# print(rolodex['Amanda']) # throws error

rolodex['Amanda'] = 5559754
print(rolodex['Amanda'])

print(rolodex['David'])
rolodex['David'] = 5550902
print(rolodex['David'])

rolodex['David'] = (5558331, 5550902)
print(rolodex['David'])

rolodex['David'] = 5558331
print(rolodex['David'])

rolodex['David (Amanda)'] = 5550902
print(rolodex)
