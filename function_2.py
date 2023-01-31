students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(list):
    for dictionary in list:
        iteration = 1
        for key, value in dictionary.items():
            print(f"{key} - {value}", end="")
            if(not len(dictionary) == iteration):
                print(", ", end="")
            iteration += 1
        print()

iterateDictionary(students) 

