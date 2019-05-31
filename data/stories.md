## story_001
* greet
   - utter_greet
* inform
   - action_fetch_profile
   - slot{"is_grandfathered":true}
   - utter_gf_confirm
* confirm
   - utter_ask_plan
* inform{"plan_type":"monthly"}
   - slot{"plan_type": "monthly"}
   - action_set_plan
   - utter_goodbye
## story_002
* greet
   - utter_greet
* inform
   - action_fetch_profile
   - slot{"is_grandfathered":true}
   - utter_gf_confirm
* confirm
   - utter_ask_plan
* inform{"plan_type":"daily"}
   - slot{"plan_type": "daily"}
   - action_set_plan
   - utter_goodbye 
## story_003
* greet
   - utter_greet
* inform
   - action_fetch_profile
   - slot{"is_grandfathered":true}
   - utter_gf_confirm
* deny
   - utter_goodbye
## story_004
* greet
   - utter_greet
* inform
   - action_fetch_profile
   - slot{"is_grandfathered":false}
   - utter_ask_plan
* inform{"plan_type":"monthly"}
   - slot{"plan_type": "monthly"}
   - action_set_plan
   - utter_goodbye 
## story_005
* greet
   - utter_greet
* inform
   - action_fetch_profile
   - slot{"is_grandfathered":false}
   - utter_ask_plan
* inform{"plan_type":"monthly"}
   - slot{"plan_type": "monthly"}
   - action_set_plan
   - utter_goodbye
## Generated Story 1112900605242160601
* inform
    - action_fetch_profile
    - slot{"is_grandfathered": true}
    - utter_gf_confirm
* confirm
    - utter_ask_plan
* inform{"plan_type": "daily"}
    - slot{"plan_type": "daily"}
    - action_set_plan
    - slot{"plan_type": "daily"}
    - utter_goodbye

## Generated Story -1120043964473822642
* greet
    - utter_greet
* inform
    - action_fetch_profile
    - slot{"is_grandfathered": true}
    - utter_gf_confirm
* confirm
    - utter_ask_plan
* inform{"plan_type": "monthly"}
    - slot{"plan_type": "monthly"}
    - action_set_plan
    - slot{"plan_type": "monthly"}
    - utter_goodbye

## Generated Story 24994176411537609
* greet
    - utter_greet
* inform
    - action_fetch_profile
    - slot{"is_grandfathered": false}
    - utter_ask_plan
* inform{"plan_type": "monthly"}
    - slot{"plan_type": "monthly"}
    - action_set_plan
    - slot{"plan_type": "monthly"}
    - utter_goodbye

## Generated Story 6703871507871376521
* inform
    - action_fetch_profile
    - slot{"is_grandfathered": false}
    - utter_ask_plan
* inform{"plan_type": "monthly"}
    - slot{"plan_type": "monthly"}
    - action_set_plan
    - slot{"plan_type": "monthly"}
    - utter_goodbye
* goodbye
    - action_restart

