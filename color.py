def color(temperature):
    colors = ['White', 'Cyan', 'Varsity Blue', 'Slime', 'Forest Green', 'Varsity Gold', 'Orange', 'Magenta']
    if temperature < 20:
        return colors[0]
    elif temperature < 30:
        return colors[1]
    elif temperature < 40:
        return colors[2]
    elif temperature < 50:
        return colors[3]
    elif temperature < 60:
        return colors[4]
    elif temperature < 70:
        return colors[5]
    elif temperature < 80:
        return colors[6]
    else:
        return colors[7]