import praw

# Divide response into paragraphs for code readability.

PARAGRAPH_1 = "If you're in distress, I imagine it must be pretty annoying " \
            "to receive a generic reply from a Reddit bot encouraging you to " \
            "reconsider. Ultimately, behind each piece of automation is a " \
            "human developer, and trust me I've been there. \n \n"

PARAGRAPH_2 = "I'm not here to tell you that life is beautiful and " \
            "inherently worth living - you have the right to decide what " \
            "to do with your own life - but I'm here to tell you that " \
            "*we need you*.\n \n"

PARAGRAPH_3 = "Sure, the world is full of petty competition, poverty, war, " \
            "and we're destroying our environment at an alarming rate - but " \
            "these are challenges that we need sensitive souls to rise up " \
            "to. Believe it or not *we need you*. \n \n" \

PARAGRAPH_4 = "Funnily enough, whenever I think about all the darkness that " \
            "collectively faces humankind, I'm reminded by a quote from Lord " \
            "of the Rings: \"It's like in the great stories... the ones that " \
            "really mattered. Full of darkness and danger they were... " \
            "Those were the stories that stayed with you. That meant " \
            "something, even if you were too small to understand why. " \
            "But I think... I do understand... There's some good in this " \
            "world, and it's worth fighting for\" (See: " \
            "https://youtu.be/IOmtjCfuRvc) \n \n"

PARAGRAPH_5 = "I believe that's true. I sincerely hope you do as well. I " \
            "hope you can have a smile during the apocalypse, cause there's " \
            "a lot of good that's worth fighting for: " \
            "https://en.wikipedia.org/wiki/List_of_suicide_crisis_lines"

# Instantiate a generic reply by concatenating paragraphs.

REPLY_TEXT = PARAGRAPH_1 + PARAGRAPH_2 + PARAGRAPH_3 + PARAGRAPH_4 + PARAGRAPH_5

# These are the post keywords that will trigger a response from the bot.

KEYWORDS = ["kill myself", "commit suicide",
            "i want to die", "i wish i was dead"]


def main():

    # Instantiate an instance of PRAW. See documentation for how to fill the
    # parameters:
    # https://chatbots.studio/blog/how-to-make-a-reddit-bot-with-python/

    reddit = praw.Reddit(client_id="CLIENT_ID", client_secret="SECRET",
                     password="PASSWORD", user_agent="AGENT",
                     username="USERNAME")

    # Specify subreddits to post to.
    subreddit = reddit.subreddit("all")

    # For each submission in specified subreddits, watch and wait for a post.
    for submission in subreddit.stream.submissions():
        process_submission(submission)


def process_submission(submission):

    # Normalize the title as titles are case sensitive.
    normalized_title = submission.title.lower()

    # If any key phrase is detected in the post title, reply with our message.
    for key_phrase in KEYWORDS:
        if key_phrase in normalized_title:
            submission.reply(REPLY_TEXT)
            break


if __name__ == "__main__":
    main()



