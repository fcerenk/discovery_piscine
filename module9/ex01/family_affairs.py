#!/usr/bin/env python3

def find_the_redheads(dupont_family):
	red_hair = []
	for name in dupont_family.keys():
		if dupont_family[name] == "red":
			red_hair.append(name)

	res = filter(None, red_hair)
	return list(res)

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))
