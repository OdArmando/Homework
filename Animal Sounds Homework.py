sunete_animale = {
    "Leu": "grr",
    "Tigru": "rawr",
    "Sarpe": "sss",
    "Pasare": "cirip"
}

user_input = input(
    "Va rog introduceti unul din urmatoarele sunete pentru a vedea ce animal este: grr,rawr,sss,cirip \n")

user_input_list = user_input.split(" ")
print(type(user_input_list))
animale = ""
for sunet_input in user_input_list:
    for sound_key in sunete_animale:
        if sunete_animale[sound_key] == sunet_input:
            animale += sound_key + " "

print(animale)