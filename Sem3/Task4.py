'''
Напишите программу для печати всех уникальных значений в словаре.
ist_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
'''
list_1 = [{"V": "S001"}, {"V": "S002"},
          {"VI": "S001"}, {"VI": "S005"},
          {"VII": " S005 "}, {" V ":" S009 "},
          {" VIII ":" S007 "}]

new_list = []

for item in list_1:
    for key, value in item.items():
        new_list.append(value)
        
print(new_list)
print(set(new_list))