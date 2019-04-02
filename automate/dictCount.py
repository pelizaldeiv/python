import pprint
message = 'This day can  only justifiably be rivaled by the day I lived next to a zamboni farm in Queen Heights New York prior to here'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)
