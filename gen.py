def generate_ahk_function(function_name, keybind, min_wait, max_wait):
    lines = []
    lines.append(f"{function_name}()")
    lines.append("{")
    
    # Handle key sequences with modifiers (e.g., "Shift c")
    keys = keybind.split()
    for key in keys:
        lines.append(f"SendInput {{{key} down}}")
        lines.append(f"Sleep, % ran({min_wait},{max_wait})")
    
    # Reverse the order for key release
    for key in reversed(keys):
        lines.append(f"SendInput {{{key} up}}")
        lines.append(f"Sleep, % ran({min_wait},{max_wait})")
    
    lines.append("}")
    return "\n".join(lines)

def generate_ahk_script(functions_and_keybinds, min_wait=1, max_wait=2):
    script = []
    for function_name, keybind in functions_and_keybinds:
        script.append(generate_ahk_function(function_name, keybind, min_wait, max_wait))
        script.append("")  # Add a blank line between functions
    return "\n".join(script)

