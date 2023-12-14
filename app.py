from flask import Flask, render_template
import slack_sdk
import feedparser
import apscheduler
import subprocess 

SLACK_TOKEN = 'xoxb-6335849768022-6342628404050-UJaoC7jtVnCbtnu7QiruRZ3C'
SLACK_CHANNEL = 'C06A2EPPW2F'

client = slack_sdk.WebClient(token=SLACK_TOKEN)
# client.chat_postMessage(channel=SLACK_CHANNEL,text='Hello world')
parse_rss = feedparser.parse("http://feeds.feedburner.com/geeknews-feed")

for p in parse_rss.entries:
    print(p.title, p.link)

def send():
    for p in parse_rss.entries:
        print(p.title, p.link)
        response = client.chat_postMessage(
                            channel=SLACK_CHANNEL,
                            blocks=[
                                {
                                    "type": "header",
                                    "text": {
                                        "type": "plain_text",
                                        "text": p.title,
                                    }
                                },
                                {
                                    "type": "section",
                                    "text": {
                                        "type": "mrkdwn",
                                        "text": p.link
                                    }
                                }
                            ],
                            unfurl_links=False,
                            unfurl_media=False,
                            text="호외요~ 호외",
                        )
        return


# app = Flask(__name__)

# # @app.route("/")
# # def index():
# #     return render_template('./index.html')

@app.route("/")
def hello():
    return "Health Checking"

# if __name__ == "__main__":
# app.run(debug = True, port = 5002)

send()


subprocess.run(["crontab", "-l"])  # 기존 cron 작업 확인
subprocess.run(["echo", "50 15 * * * app.py "], shell=True)  # cron 작업 추가
