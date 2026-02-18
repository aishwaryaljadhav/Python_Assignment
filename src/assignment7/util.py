def generate_logo(thickness):
    if thickness <= 0 or thickness % 2 == 0:
        return []

    c = 'H'
    lines = []

    # Top Cone
    for i in range(thickness):
        line = (c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1)
        lines.append(line)

    # Top Pillars
    for i in range(thickness + 1):
        line = (c*thickness).center(thickness*2) + (c*thickness).center(thickness*6)
        lines.append(line)

    # Middle Belt
    for i in range((thickness + 1) // 2):
        line = (c*thickness*5).center(thickness*6)
        lines.append(line)

    # Bottom Pillars
    for i in range(thickness + 1):
        line = (c*thickness).center(thickness*2) + (c*thickness).center(thickness*6)
        lines.append(line)

    # Bottom Cone
    for i in range(thickness):
        line = ((c*(thickness-i-1)).rjust(thickness) + 
                c + 
                (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)
        lines.append(line)

    return lines
