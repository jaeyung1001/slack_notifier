from slack_sdk import WebClient

class SlackNotifier:
    def __init__(self, token):
        self.token = token
        self.client = WebClient(self.token)

    # slack_sdk function
    def get_channel_id(self, channel_name):
        """
        슬랙 채널ID 조회
        """
        # conversations_list() 메서드 호출
        # limit -> 조회 가능한 채널수 default : 100
        # https://api.slack.com/methods/conversations.list 
        result = self.client.conversations_list(limit=2000, exclude_archived='true')
        # 채널 정보 딕셔너리 리스트
        channels = result.data["channels"]
        channel_id = None
        for channel in channels:
            if channel["name"] == channel_name and channel["is_channel"] == True:
                channel_id = channel["id"]

        if channel_id == None:
            raise Exception("None Exist Channel or Private Channel")
        return channel_id

    def get_message_ts(self, channel_id, query):
        """
        슬랙 채널 내 메세지 조회
        """
        # conversations_history() 메서드 호출
        result = self.client.conversations_history(channel=channel_id)
        # 채널 내 메세지 정보 딕셔너리 리스트
        messages = result.data["messages"]
        # 채널 내 메세지가 query와 일치하는 메세지 딕셔너리 쿼리
        # print(messages)
        try:
            message = list(filter(lambda m: m["text"] == query, messages))[0]
        except:
            raise Exception("None Exist Message")
        # 해당 메세지ts 파싱
        message_ts = message["ts"]
        return message_ts

    def post_thread_message(self, channel_id, message_ts, text):
        """
        슬랙 채널 내 메세지의 Thread에 댓글 달기
        """
        # chat_postMessage() 메서드 호출
        result = self.client.chat_postMessage(
            channel=channel_id, text=text, thread_ts=message_ts
        )
        return result

    def send_message(self, channel_id, text):
        response = self.client.chat_postMessage(channel=channel_id, text=text)
        if response.ok == False:
            print("Send Message Failed!")
