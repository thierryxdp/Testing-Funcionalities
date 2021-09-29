import text2emotion as te

f = open('C:\\Users\\thier\\ExtractingEmotions\\articles\\juliette_title.txt', 'r', encoding='utf-8')

if f.mode == 'r':
    text = "Minister of Education says he does not consider fear of the pandemic a 'plausible' reason for missing ENEM tests"

    print(text)
    
    print(te.get_emotion(text))
else:
    print("Nao foi possivel abrir o arquivo :( ")

