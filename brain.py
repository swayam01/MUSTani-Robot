import conversation,tell_time,weather,define_subject,business_news_reader

def brain(name, speech_text,city_name,city_code):
    def check_message(check):
        words_of_message = speech_text.split()
        if set(check).issubset(set(words_of_message)):
            return True
        else:
            return False

    if check_message(['who','are', 'you']):
        general_conversations.who_are_you()

    elif check_message(['how', 'i', 'look']) or check_message(['how', 'am', 'i']):
        general_conversations.how_am_i()

    elif check_message(['tell', 'joke']):
        general_conversations.tell_joke()

    elif check_message(['who', 'am', 'i']):
        general_conversations.who_am_i(name)

    elif check_message(['where', 'born']):
        general_conversations.where_born()

    elif check_message(['how', 'are', 'you']):
        general_conversations.how_are_you()

    elif check_message(['time']):
        tell_time.what_is_time()

    elif check_message(['how', 'weather']) or check_message(['hows', 'weather']):
        weather.weather(city_name, city_code)

    elif check_message(['define']):
        define_subject.define_subject(speech_text)

    elif check_message([‘business’, ‘news’]):
        business_news_reader.news_reader()

    else:
        general_conversations.undefined()
