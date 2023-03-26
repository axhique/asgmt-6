import json

caps={"capital":[ {"Tamil nadu":"Chennai",
         "Kerala":"Thiruvanandapuram",
         "Karnataka":"Bengaluru",
         "Telangana":"hyderabad",
         "West bengal":"Kolkata",
         "Goa":"Panaji",
         "Himachal pradesh":"Shimla"}]}

contents=json.dumps(caps)
file=open('newf1.json','w+')
file.write(contents)
file_contents=json.load(file)


print(file_contents)
file.close()