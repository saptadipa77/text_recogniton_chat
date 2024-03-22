import re
import long_responses as long
import random


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('hello', ['hi','wassup','sup','heya'],single_response=True)
    # response ("materials_inquiry",["Sure, we offer a wide range of materials including steel, cement, tiles, pipes, and valves. What are you looking for?"],required_words=['materials'])
    # response(  "pricing_inquiry", ["The pricing for our materials varies depending on factors such as quantity, type, and location. Can you provide more details so I can assist you better?"],required_words=['quantity','type','location'])
    # response(  "order_placement",["Great! Let's get started with your order. Could you please specify the material, quantity, and delivery address?"],required_words=['address','shipping','quantity','order'])
    response("order_confirmation",["Your order has been confirmed. We will process it shortly and notify you once it's ready for delivery."],required_words=['confirmation','confirm','order','ready'])
    response( "goodbye", ["Thank you for visiting us! If you need any further assistance, feel free to reach out. Goodbye!"],required_words=['bye','Bye','BYE','TATA','goodnight'])
    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_MATERIALS,['help','materials','inquiry'],required_words=['materials'])
    response(long.R_PRICING,['price','of','materials'],required_words=['price','materials'])
    response(long.R_PLACEMENT,['order','placement','materials','address','shipping','quantity','place'],required_words=['address','shipping','quantity','order','place','I','want'])
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))
