import swpag_client as sc

# Pass in the service that you want to get targets for.
# All teams and flag ids will be printed.

url='http://34.195.187.175/'
token = '66978175b387ba7b6dee386d16b40b29'
t = sc.Team(url, token)
# Default to service 1
service = 1
if sys.argv[1] is not None:
	service = sys.argv[1]

targets = t.get_targets(service)

for target in targets:
    print(target['hostname'])
    print(target['flag_id'])
