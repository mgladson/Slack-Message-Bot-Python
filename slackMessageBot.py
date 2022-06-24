#!/usr/bin/env python3
import json
import sys
import requests

def scrape_data_for_alerting():
    title_literal=determine_title()
    message_literal="A sample test mesasge"
    return (title_literal,message_literal)

def determine_title():
    title=(f"New Incoming Message :zap:")
    return (title)

def populate_title_and_message(title,message):
    title_and_message_dict={"title_fixed" : "{}".format(title),
                            "message_fixed" : "{}".format(message)}
    #print("{}".format(title_and_message_dict["title_fixed"]))
    return (title_and_message_dict)

def slack_send_channel_automated_message(titleMessageDict):
    #alerts-link-eth-rinkeby
    url = "https://hooks.slack.com/services/YOUR_SLACK_ALERT_CHANNEL_WEBHOOK"

    slack_data = {
        "username": "NotificationBot",
        "icon_emoji": ":satellite:",
        #"channel" : "#somerandomcahnnel",
        "attachments": [
            {
                "color": "#7bf538", #9733EE=red,#7bf538=green
                "fields": [
                    {
                        "title": "{}".format(titleMessageDict["title_fixed"]),
                        "value": "{}".format(titleMessageDict["message_fixed"]),
                        "short": "false",
                    }
                ]
            }
        ]
    }
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)

def run_main_function():
    (titleLiteral,messageLiteral)=scrape_data_for_alerting()
    titleMessageDict=populate_title_and_message(titleLiteral,messageLiteral)
    slack_send_channel_automated_message(titleMessageDict)
    return

if __name__ == '__main__':
    run_main_function()
