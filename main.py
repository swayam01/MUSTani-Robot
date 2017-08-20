import sys
import yaml
import speech_recognition as sr
import brain
import tts

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

# Functioning Variables
name = profile_data['name']
city_name = profile_data['city_name']
city_code = profile_data['city_code']

tts('Welcome ' + name + ', systems are now ready to run. How can I help you?')

def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    
    try:
        speech_text = r.recognize_google(audio).lower().replace("'", "")
        print("Mustani thinks you said '" + speech_text + "'")
    except sr.UnknownValueError:
        print("Mustani could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition
        service; {0}".format(e))

    brain(name,speech_text,city_name, city_code)

main()            
