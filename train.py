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

net = NER(corp, **model_params)

learning_params = {'dropout_rate': 0.5,
                   'epochs': 5,
                   'learning_rate': 0.005,
                   'batch_size': 8,
                   'learning_rate_decay': 0.707}
results = net.fit(**learning_params)
NER.save(net,"C:\\Users\\BioQwer\\Documents\\Development\\ner\\drug_model\\drug_model")