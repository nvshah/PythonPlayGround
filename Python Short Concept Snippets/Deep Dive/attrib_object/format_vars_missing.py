s = "The dog name is {dog_name} & eye color is {eye_color}"

dog_name = "Pluto"
eye_color = "brown"

class MissingClass(dict):
    # If keys are missing in format() then __missing__ will be called
    def __missing__(self,key):
        return "{" + key + "}"

print(s.format(**MissingClass(vars())))
del dog_name
print(s.format_map(MissingClass(vars())))
del eye_color
print(s.format_map(MissingClass(vars())))

# Output
"""
The dog name is Pluto & eye color is brown
The dog name is {dog_name} & eye color is brown
The dog name is {dog_name} & eye color is {eye_color}
"""