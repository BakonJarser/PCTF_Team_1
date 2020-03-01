import swpag_client as sc

url='http://34.195.187.175/'
token = '66978175b387ba7b6dee386d16b40b29'
t = sc.Team(url, token)
targets = t.get_targets(2)

for target in targets:
    print(target['hostname'])
    print(target['flag_id'])
