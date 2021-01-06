import json

payload = {"id":1,"firstName":"Vernon","lastName":"Harper","email":"egestas.rhoncus.Proin@massaQuisqueporttitor.org","programme":"Financial Analysis","courses":["Accounting","Statistics"]}

# Loads  method parse json string and it returns dict object


dict_payload = json.loads(json.dumps(payload))

course = dict_payload['courses']
print(type(course))

print(course[0])
print(course[1])
# for x in course:
#     print(x)
