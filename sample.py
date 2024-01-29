import notifier

if __name__ == '__main__':
    my_token = ""
    channel_name = ""
    slack = notifier.SlackNotifier(my_token)
    
    # print(slack.get_channel_id(channel_name))
    
    # print(slack.get_message_ts(channel_name, "test from jaeyung pc"))
    
    # slack.send_simple_message(channel_name, "test from jaeyung pc")
    
    # message_block = [
	# 	{
	# 		"type": "section",
	# 		"text": {
	# 			"type": "mrkdwn",
	# 			"text": "New Paid Time Off request from <example.com|Fred Enriquez>\n\n<https://example.com|View request>"
	# 		}
	# 	}
	# ]
    # slack.send_custom_message(channel_name, message_block)

    # slack.post_thread_message(channel_name, "test from jaeyung pc", "hi welcome thread")