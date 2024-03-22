from flask import Flask, request, jsonify
import re
import main as long

app = Flask(__name__)

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
#def response(bot_response, list_of_words, single_response=False, required_words=[]):