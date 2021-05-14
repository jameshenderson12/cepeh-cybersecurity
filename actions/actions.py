# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions
#
# # This is a simple example for a custom action which utters "Hello World!"
#
# # class ActionHelloWorld(Action):
# #
# #      def name(self) -> Text:
# #          return "action_hello_world"
# #
# #      def run(self, dispatcher: CollectingDispatcher,
# #              tracker: Tracker,
# #              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #
# #          dispatcher.utter_message(text="Hello World!")
# #
# #          return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

# class ActionUserToContinue(Action):
#
#     def name(self):
#         return "action_user_to_continue"
#
#     def run(self, dispatcher, tracker, domain):
#         """Sets the slot 'shall_continue' to true/false dependent on whether the user
#         wishes to proceed with the conversation"""
#         intent = tracker.latest_message["intent"].get("name")
#
#         if intent == "affirm":
#             return [SlotSet("shall_continue", True)]
#         elif intent == "deny":
#             return [SlotSet("shall_continue", False)]
#         return []
#
#
# # class ActionUserToRateQuestion(Action):
# #
# #     def name(self):
# #         return "action_user_to_rate"
# #
# #     def run(self, dispatcher, tracker, domain):
# #         """Sets the slot 'shall_continue' to true/false dependent on whether the user
# #         wishes to proceed with the conversation"""
# #         intent = tracker.latest_message["intent"].get("name")
# #         #response = tracker.latest_message["response"].get("name")
# #         rating = tracker.latest_message["intent"].get("name").value
# #
# #         if intent == "give_rating_q1":
# #             return [SlotSet("ratingQ1", rating)]
# #         elif intent == "give_rating_q3":
# #             return [SlotSet("ratingQ3", rating)]
# #         elif intent == "give_rating_q7" :
# #             return [SlotSet("ratingQ7", rating)]
# #         else :
# #             dispatcher.utter_message(text="Please enter a number between 1-10.")
# #         return []
#
#
# class ActionUserToRoleplay(Action):
#
#     def name(self):
#         return "action_user_to_roleplay"
#
#     def run(self, dispatcher, tracker, domain):
#         """Sets the slot 'shall_roleplay' to true/false dependent on whether the user
#         wishes to proceed with the roleplaying"""
#         intent = tracker.latest_message["intent"].get("name")
#
#         if intent == "affirm":
#             return [SlotSet("shall_roleplay", True)]
#         elif intent == "deny":
#             return [SlotSet("shall_roleplay", False)]
#         return []

class ActionPause(Action):

     def name(self) -> Text:
         return "action_pause"

     def run(self,
             dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         return [ConversationPaused()]


# # class ActionSearchConcerts(Action):
# #     def name(self):
# #         return "action_search_concerts"
# #
# #     def run(self, dispatcher, tracker, domain):
# #         concerts = [
# #             {"artist": "Foo Fighters", "reviews": 4.5},
# #             {"artist": "Katy Perry", "reviews": 5.0},
# #         ]
# #         description = ", ".join([c["artist"] for c in concerts])
# #         dispatcher.utter_message(text=f"{description}")
# #         return [SlotSet("concerts", concerts)]
# #
# #
# # class ActionSearchVenues(Action):
# #     def name(self):
# #         return "action_search_venues"
# #
# #     def run(self, dispatcher, tracker, domain):
# #         venues = [
# #             {"name": "Big Arena", "reviews": 4.5},
# #             {"name": "Rock Cellar", "reviews": 5.0},
# #         ]
# #         dispatcher.utter_message(text="here are some venues I found")
# #         description = ", ".join([c["name"] for c in venues])
# #         dispatcher.utter_message(text=f"{description}")
# #         return [SlotSet("venues", venues)]
# #
# #
# # class ActionShowConcertReviews(Action):
# #     def name(self):
# #         return "action_show_concert_reviews"
# #
# #     def run(self, dispatcher, tracker, domain):
# #         concerts = tracker.get_slot("concerts")
# #         dispatcher.utter_message(text=f"concerts from slots: {concerts}")
# #         return []
# #
# #
# # class ActionShowVenueReviews(Action):
# #     def name(self):
# #         return "action_show_venue_reviews"
# #
# #     def run(self, dispatcher, tracker, domain):
# #         venues = tracker.get_slot("venues")
# #         dispatcher.utter_message(text=f"venues from slots: {venues}")
# #         return []
