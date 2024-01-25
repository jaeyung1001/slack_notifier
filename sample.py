import notifier
if __name__ == '__main__':
    my_token = "xoxb-1394758654305-3810545912694-xIEY2rQfJ6imHAP0kHhOierb"
    channel_id = "jaeyung_channel"
    slack = notifier.SlackNotifier(my_token)
    slack.send_message(channel_id, "test from jaeyung pc")