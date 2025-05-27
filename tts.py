import pyttsx3
from configparser import ConfigParser
from colorama import init, Fore, Style

def main():
    init(autoreset=True)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id) #female

    list_voices(voices)

    print(Fore.CYAN + '\n\nWelcome to ' + Fore.MAGENTA + 'Terra\'s ' + Fore.CYAN + 'TTS :3\n')
    show_command_list()

    speech = 'TTS'

    while speech != ':q':
        if speech[0:2] == ':h':
            show_command_list()
            speech = 'List of commands'
        if speech[0:4] == ':vol':
            cmd = parse_command_volume(speech.split())
            if cmd >= 0:
                engine.setProperty('volume',cmd)
                speech = 'Volume set to ' + str(cmd * 100) + '%'
        if speech[0:4] == ':vls':
            list_voices(voices)
            speech = 'List of voices'
        if speech[0:2] == ':v':
            cmd = parse_command_voice(speech.split(), voices)
            if cmd >= 0:
                engine.setProperty('voice',voices[cmd].id)
                speech = 'Voice changed'
        if speech[0:2] == ':r':
            cmd = parse_command_rate(speech.split())
            if cmd >= 0:
                engine.setProperty('rate',cmd)
                speech = 'Rate set to ' + str(cmd)

        engine.say(speech)
        engine.runAndWait()
        speech = input(Fore.CYAN + ':3 | ' + Fore.MAGENTA)

    print(Fore.CYAN + '\nEnded TTS.\n' + Style.RESET_ALL)
    engine.say('ended tts')
    engine.runAndWait()
    engine.stop()
#end main

def show_command_list():
    commands = [
        'Commands',
        ':h\tHelp',
        ':q\tQuit',
        ':v\tSet voice of TTS (index of voice in list)',
        ':vls\tList of voices',
        ':vol\tSet volume of TTS (0-100)',
        ':r\tSet rate of speech (> 0) default 200',
        #'(IN DEV):w Save voice to config file'
    ]
    for cmd in commands:
        print(Fore.CYAN + cmd)

def parse_command_volume(cmd):
    if cmd[-1].isdigit():
        vol = int(cmd[-1])
        if vol <= 100 and vol >= 0:
            print('Volume set to %s' % (vol))
            return vol/100
        else:
            print('Volume must be 0-100')
    else:
        print('Enter a valid volume like \':v 95\'')
    return -1

def parse_command_voice(cmd, voices):
    if cmd[-1].isdigit():
        voice = int(cmd[-1])
        if voice >= 0 and voice < len(voices):
            return voice
    print('Index Error')
    return -1

def parse_command_gender_OLD(cmd):
    if cmd[-1].isalpha():
        gen = cmd[-1]
        if gen == 'm':
            print('voice set to masc')
            return 0
        if gen == 'f':
            print('voice set to fem')
            return 1
    print('Error only m or f available')
    return -1

def parse_command_rate(cmd):
    if cmd[-1].isdigit():
        rate = int(cmd[-1])
        if rate >= 0:
            print('Rate set to %s' % (rate))
            return rate
        else:
            print('Rate must be integer greater than 0.')
    else:
        print('Enter a valid rate like \':r 95\'')
    return -1

def list_voices(voices):
    print(Fore.CYAN + 'Voices')
    for voice in voices:
        v_name = voice.id.split('\\')
        print(Fore.CYAN + v_name[-1])
    pass



if __name__ == '__main__':
    main()