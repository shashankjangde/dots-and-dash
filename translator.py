import json
from gtts import gTTS


all = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def to_morse(inp):
    morsed = [all[a] for a in inp.upper()]
    return (" ".join(morsed))


def to_text(morse_code):
    # return a string without leading or trailing whitespaces
    morse_code = morse_code.strip()
    morse_code = morse_code.split(' ')  # returns a list
    morse_code_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
        '----.': '9'
    }

    text = ''
    for symbol in morse_code:
        if symbol in morse_code_dict:
            text += morse_code_dict[symbol]
        elif symbol == '/':
            text += ' '
    return text


def to_aud(text):
    tts = gTTS(text=text, lang='en', slow=True)
    tts.save("S:\Morse Code\output.mp3")
