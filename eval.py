from ner.utils import tokenize, lemmatize


def print_predict(sentence, network):
    # Split sentence into tokens
    tokens = tokenize(sentence)
    print(tokens)
    tags = network.predict_for_token_batch([tokens])[0]
    for token, tag in zip(tokens, tags):
        print(token, tag)


print_predict("Jachin", net)
print_predict("lodgeth", net)
print_predict("heifer", net)
print_predict("denied", net)
print_predict("bits", net)
print_predict("Inositol nicotinate", net)
print_predict("Jachin", net)

print_predict("(2R,3R)-N^1^-[(1S)-2,2-DIMETHYL-1-(METHYLCARBAMOYL)PROPYL]-N^4^-HYDROXY-2-(2-METHYLPROPYL)-3-{[(1,3-THIAZOL-2-YLCARBONYL)AMINO]METHYL}BUTANEDIAMIDE", net)


