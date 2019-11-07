
berthaVonSuttner = {'belderberg_Ampeln':'green', 'platz_Ampeln':'red'}

def switchLights(intersection):
    for key in intersection.keys():
        light = intersection[key]
        if light == 'green':
            intersection[key] = 'yellow'
        elif light == 'yellow':
            intersection[key] = 'red'
        elif light == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)


print(berthaVonSuttner)
switchLights(berthaVonSuttner)
print(berthaVonSuttner)
