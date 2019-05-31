from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class FetchProfileAction(Action):
    def name(self):
        return "action_fetch_profile"

    def run(self, dispatcher, tracker, domain):
        mock_profile = {
                "name" : "Yi Yang",
                "account #" : "12341234",
                "is_grandfathered" : True
                }
        response = "Customer profile:\n  Name: {}  Account #: {}  is_grandfathered: {}".format(mock_profile["name"], mock_profile["account #"], mock_profile["is_grandfathered"])
        dispatcher.utter_message(response)
        return [SlotSet("is_grandfathered", mock_profile["is_grandfathered"])]

class SetPlanAction(Action):
    def name(self):
        return "action_set_plan"

    def run(self, dispatcher, tracker, domain):
        plan_type = tracker.get_slot('plan_type')
        response = "Set plan type to {}".format(plan_type)
        dispatcher.utter_message(response)
        return [SlotSet("plan_type", plan_type)]
