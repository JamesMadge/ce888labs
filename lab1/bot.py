from sopel import module
from emo.wdemotions import EmotionDetector

emo = EmotionDetector()

# Emotions
joy = 'joy'
disgust = 'disgust'
surprise = 'surprise'
anger = 'anger'
fear = 'fear'
sadness = 'sadness'

# Initialise emotions.
global total_emotion
total_emotion = dict(joy=0, disgust=0, surprise=0, anger=0, fear=0, sadness=0)

global average_emotion
average_emotion = dict(joy=0, disgust=0, surprise=0, anger=0, fear=0, sadness=0)

# Count total message count.
global message_count
message_count = 0

@module.rule('')
def hi(bot, trigger):

    #Define globals.
    global message_count
    global total_emotion
    global average_emotion

    # Increment the message count.
    message_count += 1

    # Section off the new message for readability.
    print('\n::: Message [' + str(message_count) + ']' + ' ::::::::::::::::::::::::::::::')

    # Print the text to default output.
    print(trigger.nick + ': "' + trigger + '"')

    # Emotion detection of each message.
    message_emotion = emo.detect_emotion_in_raw(trigger)
    print('Message Emotion:   ' + message_emotion.__str__())

    # Total emotion.
    total_emotion = {key: total_emotion.get(key, 0) + message_emotion.get(key, 0)
                     for key in set(total_emotion) | set(message_emotion)}

    print('Total emotion:     ' + total_emotion.__str__())

    # Average emotion.
    average_emotion = {key: (total_emotion.get(key, 0) / message_count) for key in set(total_emotion)}

    print('Average emotion:   ' + average_emotion.__str__())