import paralleldots

# Setting API Key
api_key = paralleldots.set_api_key("Ax2gN8ym1LLf050wvrgHSzDcPDIfDnUDiOEc0DETpPo")

f = open('C:\\Users\\thier\\ExtractingEmotions\\articles\\juliette_title.txt', 'r', encoding='utf-8')

if f.mode == 'r':
    text = f.read()

    print(text)
    
    print("Emotion\n")
    print(paralleldots.emotion(text))
else:
    print("Nao foi possivel abrir o arquivo :( ")

f = open('C:\\Users\\thier\\ExtractingEmotions\\articles\\educacao_title.txt', 'r', encoding='utf-8')

if f.mode == 'r':
    text = f.read()

    print(text)
    
    print("Emotion\n" + "\n")
    print(paralleldots.emotion(text))
else:
    print("Nao foi possivel abrir o arquivo :( ")

f = open('C:\\Users\\thier\\ExtractingEmotions\\articles\\judicial_title.txt', 'r', encoding='utf-8')

if f.mode == 'r':
    text = f.read()

    print(text)
    
    print("Emotion\n")
    print(paralleldots.emotion(text))
else:
    print("Nao foi possivel abrir o arquivo :( ")
