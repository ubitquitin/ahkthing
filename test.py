from gen import generate_ahk_script_with_rotation

# Input list of tuples (FunctionName, Keybind)
keybind_mapping = {
    "piercing": "1",
    "dazing": "2",
    "binding": "3",
    "grico": "4",
    "corr": "5",
    "frag": "6",
    "deadshot": "x",
    "ds": "c",
    "snap": "w",
    "rapid": "q",
    
}

#Input ordered list of abilities. Entries must match keys in above mapping.
rotation = ["ds", "grico", "snap", "rapid", "dazing", "piercing", "deadshot", "corr", "frag"]

# Specify your random wait times here
ahk_script = generate_ahk_script_with_rotation('rohans_rotation', rotation, keybind_mapping, min_wait=100, max_wait=199)

# Print or save to a file
print(ahk_script)

# To save to a file:
with open("output.ahk", "w") as file:
    file.write(ahk_script)