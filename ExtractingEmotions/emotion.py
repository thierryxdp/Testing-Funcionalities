import paralleldots
from math import ceil
from googletrans import Translator

# Creating Translator Objector from Google Translate API
translator = Translator()


# Setting API Key
api_key = paralleldots.set_api_key("Ax2gN8ym1LLf050wvrgHSzDcPDIfDnUDiOEc0DETpPo")
    
f = open('C:\\Users\\thier\\ExtractingEmotions\\articles\\comidas_processadas_all.txt', 'r', encoding='utf-8')

if f.mode == 'r':
    text = f.read()
    
    result = translator.translate(text)
    
    print(result.text + "\n")
    emotions = paralleldots.emotion(result.text)
    emotions_sorted = sorted(emotions['emotion'].items(), key=lambda x: x[1], reverse=True)
    print(str(emotions_sorted[0][0]) + ("(") + str(ceil(emotions_sorted[0][1]*100)) + "%) and " + str(emotions_sorted[1][0]) + ("(") + str(ceil(emotions_sorted[1][1]*100)) +"%)\n")
    
else:
    print("Nao foi possivel abrir o arquivo :( ")
    