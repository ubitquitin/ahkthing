def generate_ahk_function_with_rotation(function_name, ability_rotation, keybind_mapping, min_wait, max_wait, gcd_time=1800, tick_time=600):
    
    # 3x modifier is worst case given modifier keys.
    if 3*max_wait >= tick_time:
        raise ValueError('Warning: The max wait setting is too large given the tick time, and will result in desync!')

    lines = []
    lines.append(f"{function_name}()")  # Function header
    lines.append("{")

    # Iterate over the ability rotation
    for ability in ability_rotation:
        # Get the keybind for the current ability
        keybind = keybind_mapping.get(ability)
        if keybind is None:
            raise ValueError(f"Keybind for ability '{ability}' not found in the mapping.")
        
        lines.append("total_random_wait := 0")
        # Handle key sequences with modifiers (e.g., "Shift c")
        keys = keybind.split()
        # Press each key (down)
        for key in keys:
            lines.append(f"key_down_wait := ran({min_wait},{max_wait})")
            lines.append(f"key_down_mod_wait := ran({int(min_wait/4)},{int(max_wait/2)})")
            if key in ["Shift", "Ctrl", "Alt"]:
                # Shorter delay for modifier keys
                lines.append(f"SendInput {{{key} down}}")
                lines.append("Sleep, %key_down_mod_wait%")
                lines.append("total_random_wait := total_random_wait + key_down_mod_wait")
            else:
                # Regular delay for main key presses
                lines.append(f"SendInput {{{key} down}}")
                lines.append("Sleep, %key_down_wait%")
                lines.append("total_random_wait := total_random_wait + key_down_wait")

        # Release each key (up) in reverse order
        for key in reversed(keys):
            lines.append(f"key_up_wait := ran({min_wait},{max_wait})")
            lines.append(f"key_up_mod_wait := ran({int(min_wait/4)},{int(max_wait/2)})")
            if key in ["Shift", "Ctrl", "Alt"]:
                # Shorter delay for modifier keys
                lines.append(f"SendInput {{{key} up}}")
                lines.append("Sleep, %key_up_mod_wait%")
                lines.append("total_random_wait := total_random_wait + key_up_mod_wait")
            else:
                # Regular delay for main key releases
                lines.append(f"SendInput {{{key} up}}")
                lines.append("Sleep, %key_up_wait%")
                lines.append("total_random_wait := total_random_wait + key_up_wait")
        
        lines.append(f"Sleep, {tick_time} - %total_random_wait%")  # Adjust the remaining sleep to ensure a total of 600ms

        #sleep gcd
        lines.append(f"Sleep, % {gcd_time}")
    lines.append("}")
    return "\n".join(lines)

def generate_ahk_script_with_rotation(function_name, ability_rotation, keybind_mapping, min_wait=1, max_wait=2):
    """Generate an AHK script for the given ability rotation and keybind mapping."""
    # Generate the AHK function
    ahk_function = generate_ahk_function_with_rotation(function_name, ability_rotation, keybind_mapping, min_wait, max_wait)
    
    # Return the script content
    return ahk_function
