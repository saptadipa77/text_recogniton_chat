import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_MATERIALS="Sure, we offer a wide range of materials including steel, cement, tiles, pipes, and valves. What are you looking for?"
R_PRICING="The pricing for our materials varies depending on factors such as quantity, type, and location. Can you provide more details so I can assist you better?"
R_PLACEMENT= "Great! Let's get started with your order. Could you please specify the material, quantity, and delivery address?"
def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(5)]
    return response
