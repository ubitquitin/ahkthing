from gen import generate_ahk_script

# Input list of tuples (FunctionName, Keybind)
functions_and_keybinds = [
    ("T95_Spec", "Home"),
    ("Range2h", "b"),
    ("Melee2h", "Shift c")
]

# Specify your random wait times here
ahk_script = generate_ahk_script(functions_and_keybinds, min_wait=1, max_wait=2)

# Print or save to a file
print(ahk_script)

# To save to a file:
with open("output.ahk", "w") as file:
    file.write(ahk_script)