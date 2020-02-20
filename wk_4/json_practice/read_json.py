import json

with open('gitinfo.json') as f:
    reader = json.load(f)
    print(reader)

projects = {}
projects['group1'] = ['Dan', 'Eric', 'Joe', 4]
projects['group2'] = ['Dan', 'Eric', 'Joe', 4]
projects['group3'] = (True, 'oric', 3, 4)
projects['group4'] = ['Dan', ('father','son'), 'Joe', 4]
projects['group5'] = [452]

with open('groups.json','w') as f:
    json.dump(projects, f)



