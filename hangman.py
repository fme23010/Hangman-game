"""
Hello, my name is Gregory Vasileiou and this is my final project for Code in Place.
I hope you enjoy it!
"""
"""
In this game you must guess the secret word. 
You must find all letters to win.
If not, the man will be hanged! Good luck!!!
"""
"""!!!NOTE!!! FOR THE BEST EXPERIENCE RUN THIS IN TERMINAL: pip install english-words  """
import random


# The program tests if the set exists, otherwise it uses the custom set so that it always works.
try:
    from english_words import get_english_words_set
    words_set = get_english_words_set(['web2'], lower=True)
    word_list = list(words_set)
    words = [word for word in word_list if len(word) >= 6]
    secret_word = random.choice(words)

#create a custom list with 500 words.
#my_words = random.sample(words, 500)
#print(my_words)
except ImportError:
    my_words_list = ['vorant', 'amphigaea', 'dure', 'behn', 'sulphamate', 'uvitinic', 'haematinum', 'hottentot', 'undergore', 'nonpatented', 'manstealer', 'phenolsulphonic', 'bizz', 'rais', 'biurate', 'restipulate', 'bichromic', 'pterodactylid', 'contection', 'tanyoan', 'incidentalness', 'albuminometry', 'undone', 'ethereal', 'stormwind', 'anarthria', 'catamenial', 'madi', 'biennia', 'cladoniaceous', 'uncalmed', 'unpublishableness', 'nibsome', 'sexto', 'contiguousness', 'obnounce', 'shockingly', 'breakfaster', 'assumedly', 'rogative', 'araneiformes', 'mesosiderite', 'skeigh', 'significativeness', 'beamhouse', 'tshi', 'intertwine', 'unfallenness', 'aphonic', 'cornetcy', 'misrender', 'spacy', 'euphemistically', 'cocculus', 'congou', 'overinventoried', 'mistend', 'misleading', 'sure', 'physiopsychical', 'discouragingly', 'balletomane', 'equilibrium', 'splenoptosia', 'bryanthus', 'phytophilous', 'lardizabalaceae', 'athrepsia', 'arresting', 'gearset', 'ladyish', 'akerite', 'redecussate', 'semiterrestrial', 'overdiffusely', 'pleading', 'foreskirt', 'agena', 'tailorism', 'pyrola', 'illegalness', 'bothlike', 'novemarticulate', 'austria', 'intuitionism', 'verminously', 'sermonist', 'gradine', 'iodoethane', 'forfaulture', 'nest', 'trophoblastic', 'prethrust', 'vividiffusion', 'unvoiced', 'clerestoried', 'endometritis', 'thunge', 'chlorine', 'syntonization', 'rigmarole', 'ollock', 'consociational', 'phenology', 'discontenting', 'unfinishedly', 'labroid', 'punchable', 'nitrometer', 'longleaf', 'waremaker', 'placoides', 'carbonification', 'washoan', 'unsigned', 'unhomogeneously', 'pathopsychosis', 'bedcord', 'february', 'punctuator', 'surfboarding', 'trimerization', 'illish', 'oligocythemia', 'bepatched', 'pleadingly', 'bigamously', 'cerography', 'javanese', 'sebate', 'unsurgical', 'sphenoidal', 'frangulaceae', 'olease', 'slag', 'alimentativeness', 'careful', 'uxoricide', 'campsheeting', 'burster', 'checkman', 'ingenuity', 'untroddenness', 'overpromptly', 'haustorium', 'sparrowish', 'plowwise', 'unroweled', 'gemauve', 'sulphonic', 'disfen', 'nexus', 'feltlike', 'unsparse', 'hiveward', 'rafik', 'endocrinologist', 'arteriodialysis', 'pulmonitis', 'unexporting', 'mischievous', 'sunblink', 'begging', 'unrepartable', 'archfriend', 'blunthead', 'tridermic', 'subtriplicate', 'idotheidae', 'stoichiometrically', 'cresorcinol', 'thymopsyche', 'peritrochium', 'piggishly', 'soporiferously', 'contemptuous', 'shakespearolater', 'siderous', 'plowmaker', 'talkworthy', 'vidually', 'congroid', 'pavier', 'barytine', 'among', 'splanchnolith', 'semistill', 'dancette', 'nauscopy', 'anathematization', 'underthief', 'semibasement', 'circumplication', 'umbelliflorous', 'retroxiphoid', 'labiose', 'infester', 'tachardiinae', 'oatear', 'subdued', 'semanteme', 'submetallic', 'cephid', 'preseminal', 'pedalion', 'measurelessness', 'tina', 'intercontradictory', 'muscidae', 'cognizability', 'polyprism', 'suspensory', 'tilasite', 'prefortunately', 'unconfidently', 'yengee', 'sinupallia', 'voltivity', 'narrative', 'return', 'superimpose', 'yakima', 'unbuxom', 'hepatization', 'coequality', 'aileron', 'preternormal', 'assidually', 'persism', 'hendecasyllable', 'thickheadedness', 'intervital', 'spoonhutch', 'unremittingness', 'isoseist', 'ceptor', 'campanulaceous', 'exarch', 'phymatorhysin', 'unlearnt', 'thrillfully', 'octogamy', 'obstetricy', 'unobjective', 'successfulness', 'elegize', 'palatinite', 'repository', 'turklike', 'pise', 'anaphrodisiac', 'extorsively', 'cataleptize', 'diploma', 'kabaka', 'greekist', 'paradisial', 'rail', 'heathenness', 'pompholygous', 'intertropic', 'somewhence', 'precontractual', 'sparganium', 'arithmetic', 'exallotriote', 'darling', 'stenobenthic', 'clypeastroidea', 'reguline', 'lagopode', 'leiotrichous', 'appliant', 'lawton', 'medrick', 'faon', 'orthosymmetrical', 'glareole', 'antifederalism', 'publicism', 'jockeyish', 'unhygienic', 'hinderment', 'altern', 'suint', 'gynophagite', 'unsoundableness', 'gastroparalysis', 'separatress', 'absinthiate', 'appraise', 'metric', 'nide', 'dense', 'preponderation', 'advancer', 'freewheel', 'basting', 'palmite', 'nephrotoxicity', 'berycomorphi', 'hoodwinkable', 'soary', 'unspokenly', 'choregic', 'asymbolic', 'ergot', 'coyotero', 'batitinan', 'sulphoichthyolate', 'antefuture', 'unpollutable', 'amidon', 'curcas', 'intramental', 'shoddyite', 'dropsicalness', 'fama', 'zygomaxillare', 'nonprojection', 'filicales', 'nonangling', 'unmunicipalized', 'hobblebush', 'omagua', 'enantiomorphic', 'syncliticism', 'solemnness', 'praecuneus', 'creophagy', 'minutissimic', 'prehalter', 'inexpansive', 'unthankfulness', 'parapsis', 'mydriatic', 'inherency', 'guardant', 'unmildewed', 'photomap', 'extrafocal', 'rink', 'axometric', 'railage', 'ampelidaceae', 'tindalo', 'mortality', 'classes', 'salivan', 'flanky', 'amygdaloid', 'vortical', 'conservatorio', 'armer', 'dustin', 'roentgenization', 'borne', 'symmetry', 'glyoxalic', 'cunner', 'vertebrata', 'refectionary', 'eversive', 'pertaining', 'lithotomous', 'unalterable', 'grouped', 'quindecemvir', 'trackshifter', 'althaea', 'enigmaticalness', 'venoatrial', 'pinnel', 'phraseological', 'spinebill', 'cinchonaceae', 'ushabti', 'overluxurious', 'tersulphuret', 'maculopapular', 'idoism', 'unpocketed', 'papayaceous', 'texcocan', 'tactless', 'jicama', 'zoocurrent', 'ornithomorph', 'intuitable', 'tercentenarian', 'antiaphrodisiac', 'lichi', 'nonconformance', 'metoposcopic', 'endless', 'pukishness', 'misogallic', 'vaporographic', 'homoeotype', 'nepotic', 'afrown', 'anthroxan', 'hairsplitter', 'unglandular', 'antipriming', 'nonusage', 'postmortal', 'eventognathous', 'orthodiagonal', 'spaewife', 'horonite', 'snorkel', 'miki', 'rath', 'afterpeak', 'periostea', 'sliverproof', 'yataghan', 'jookerie', 'smalter', 'twalpenny', 'zeugmatic', 'chloridella', 'skellat', 'deducibleness', 'unmechanically', 'epitimesis', 'epicyte', 'sublumbar', 'enantiomorph', 'plutarchic', 'squaller', 'phasianid', 'ostension', 'leptospira', 'hydrobromic', 'pyromucic', 'setulous', 'tenues', 'conferva', 'seminoma', 'demibastion', 'typarchical', 'pemphigous', 'preludial', 'conclusively', 'torchlighted', 'directoral', 'centripetency', 'nondemocratic', 'oleoresinous', 'telepathically', 'bopyridae', 'saxicolinae', 'detoxication', 'slipperwort', 'overcry', 'unbrotherliness', 'inductorium', 'antrustion', 'anthesterol', 'cyaphenine', 'ringmaster', 'pestalozzianism', 'angiohydrotomy', 'procompulsion', 'unactive', 'teddy', 'chazy', 'colorful', 'syrt', 'dextrad', 'neurophil', 'unsymphonious', 'leptochrous', 'romney', 'sawbwa', 'ralph', 'ablatival', 'rostrocarinate', 'uncoated', 'anteroventral', 'tusayan', 'scotcher', 'truismatic', 'pooa', 'caprelline', 'ithomiid', 'sporicide', 'droiturel', 'overcompensatory', 'untacked', 'refight', 'electrogenesis', 'struthioniformes', 'darkener', 'semimanufactured', 'priestliness', 'hidalgoism', 'endorsingly']
    secret_word = random.choice(my_words_list)

print("Welcome!!!")
empty_gallows = r"""
  +---+
  |   |
  O   |
      |     O
      |    /|\
     /|\   / \
================
"""
print(empty_gallows)
print(f"The secret word has {len(secret_word)} letters!")


#We need the first letter of the words and the other letters are hidden with dashes for the player to find.
first_letter = secret_word[0]
hidden_letters = ["_"]*(len(secret_word)-1)
hidden_word = [first_letter] + hidden_letters
guessed_letters = [first_letter]


lives = ""
#The player chooses a level of difficulty, the loop checks if they write the correct word.
while lives not in  ["hard", "mid" , "easy"] :
    lives = input("choose: hard: 5 lives, mid: 10 lives, easy: 15 lives " ).lower()
    if lives not in  ["hard", "mid" , "easy"] :
        print("Invalid choice! Please type 'hard', 'mid', or 'easy'.")
if lives == "hard" :
    lives = 5
elif lives == "mid":
    lives = 10
elif lives == "easy":
    lives = 15



while lives > 0  and "_" in hidden_word:
    print(f"lives: {lives}")
    print("".join(hidden_word))
    guess = input("Guess a letter... ").lower()

    print("".join(guessed_letters))

    if guess in guessed_letters:
        print("You already said it. Guess again.")
    else:
        guessed_letters.append(guess)
        if guess in secret_word:
            print("correct!")
            for i in range(len(secret_word)):
                if guess == secret_word[i]:
                    hidden_word[i] = guess
        else:
            print("false")
            lives = lives-1

if "_" not in hidden_word :
    print("Congratulations!!! You win! ")
elif lives == 0:
    hanged_man = r"""
      +---+
      |   |
      O   |
     /|\  |
     / \  |
         /|\
    =========
        """
    print(hanged_man)
    print("Sorry you lost! Try again!")












