settings_file = open("volume.txt", "a+")
for j in settings_file:
    if "Maneesh"==j[:len(j)-4]:
        print "SDF"