light_dict = {}

# start by turning on all the lights 
for light in range(1,100,1):
    light_dict[light] = True

# go over each light and turn it on or off
for frog in range(1,100,1):
    for light in light_dict:
        if light % frog == 0:
            if light_dict[light] == True:
                light_dict[light] = False
            elif light_dict[light] == False:
                light_dict[light] = True
        else:
            continue

print(light_dict)