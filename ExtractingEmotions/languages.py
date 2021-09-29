from googletrans import Translator

translator = Translator()

f = open('C:\\Users\\thier\\ExtractingEmotions\\articles\\juliette_subtitle.txt', 'r', encoding='utf-8')

if f.mode == 'r':
    contents = f.read()
    print(contents)
    
    result = translator.translate(contents)
    
    print(result.text)
else:
    print("Nao foi possivel abrir o arquivo :( ")