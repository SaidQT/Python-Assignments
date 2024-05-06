x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney'],
}
z = [ {'x': 10, 'y': 20} ]


x[1][0]=15
students[0]['last_name']='Bryant'
sports_directory['soccer'][0]='Andres'
z[0]['y']=30


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(list):
    for dictionary in list:
        pair= []
        for key, value in dictionary.items():
            pair.append(f'{key} - {value}')
        
        print(', '.join(pair))
        


def iterateDictionary2(key,list):
    for dictionary in list:
        if key in dictionary:
            print(dictionary[key])
            
iterateDictionary2(students)
        


def printInfo(dict):
    for key in dict:
        print(key,len(dict[key])) 
        for i in range(len(dict[key])):
            print(dict[key][i])
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

