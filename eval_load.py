data_types = ['train', 'test', 'valid']
dataset_dict = dict()
for data_type in data_types:

    with open('drugset/' + data_type + '.txt') as f:
        xy_list = list()
        tokens = list()
        tags = list()
        for line in f:
            items = line.split()
            if len(items) > 1 and '-DOCSTART-' not in items[0]:
                token, tag = items
                if token[0].isdigit():
                    tokens.append('#')
                else:
                    tokens.append(token)
                tags.append(tag)
            elif len(tokens) > 0:
                xy_list.append((tokens, tags,))
                tokens = list()
                tags = list()
        dataset_dict[data_type] = xy_list

for key in dataset_dict:
    print('Number of samples (sentences) in {:<5}: {}'.format(key, len(dataset_dict[key])))

print('\nHere is a first two samples from the train part of the dataset:')
first_two_train_samples = dataset_dict['train'][:2]
for n, sample in enumerate(first_two_train_samples):
    # sample is a tuple of sentence_tokens and sentence_tags
    tokens, tags = sample
    print('Sentence {}'.format(n))
    print('Tokens: {}'.format(tokens))
    print('Tags:   {}'.format(tags))


from ner.corpus import Corpus
corp = Corpus(dataset_dict, embeddings_file_path=None)

from ner.network import NER

model_params = {"filter_width": 7,
                "embeddings_dropout": True,
                "n_filters": [
                    128, 128,
                ],
                "token_embeddings_dim": 4,
                "char_embeddings_dim": 50,
                "use_batch_norm": True,
                "use_crf": True,
                "net_type": 'cnn',
                "use_capitalization": True,
               }

net = NER(corp,**model_params)

NER.load(net,"C:\\Users\\BioQwer\\Documents\\Development\\ner\\drug_model\\drug_model")


from ner.utils import tokenize, lemmatize


def print_predict(sentence, network):
    # Split sentence into tokens
    tokens = tokenize(sentence.lower())
    print(tokens)
    tags = network.predict_for_token_batch([tokens])[0]
    for token, tag in zip(tokens, tags):
        print(token, tag)
