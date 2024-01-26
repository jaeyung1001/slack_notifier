import notifier

if __name__ == '__main__':
    my_token = ""
    channel_id = "test"
    slack = notifier.SlackNotifier(my_token)
    slack.send_message(channel_id, "test from jaeyung pc")