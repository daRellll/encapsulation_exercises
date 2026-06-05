from the_fan_class import Fan

fan1 = Fan(speed=Fan.FAST, radius=10, color="yellow", on=True)
fan2 = Fan(speed=Fan.MEDIUM, radius=5, color="blue", on=False)

print(f"Fan1; Speed: {fan1.get_speed()} Radius: {fan1.get_radius()} Color: {fan1.get_color()} Status: {fan1.get_on()}")