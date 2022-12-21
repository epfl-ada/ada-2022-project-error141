Get unique name for each character
#Remove non-unique part of character name
character = character_metadata.loc[31186339][:]#[:-3]

def get_unique_name (name, list_names):
    name = name.lower()
    mask_unique_name = np.where([list_names.count(x) < 2 for x in name.split()])[0]
    
    return " ".join(np.array(name.split())[mask_unique_name])

name_metadata = list(chain(*[x.lower().split() for x in character.name]))
character['name'] = character.name.apply(get_unique_name, args=(name_metadata,))

character.head()

def identify_character(character_metadata, character_coref):
    #Get name and gender of character from metadata. Only keep the unique part of the name.
    name_metadata = list(chain(*[x.lower().split() for x in character_metadata.name]))
    character_metadata['name'] = character_metadata.name.apply(get_unique_name, args=(name_metadata,))
    
    #Check if the coreference resolution indentified a character not in the metadata
    #If yes add it to the character metadata
    to_add = add_character_from_coref(character_coref ,character_metadata)
    character = pd.concat([character_metadata, to_add], sort=False)
    
    return character

active = []
for token in doc:
    if token.pos_ == 'VERB':
        for child in token.children:
            
            if child.dep_ == 'nsubj':
                if child.ent_type_ == 'PERSON':
                    active.append([token.lemma_, child.text.lower()])
                    for x in child.children:
                        if x.dep_ == 'conj' and x.ent_type_ == 'PERSON':
                            active.append([token.lemma_, x.text.lower()])
                else:
                    nsubj = list(child.children)
                    #while list(nsubj):
                        #1
                    #while list(nsubj):
                        #for x in nsubj:
                            #if x.ent_type_ == 'PERSON':

                            #nsubj = nsubj.children
            #else if child.dep == 'nsubj':
                1
            #else if child.dep == 'agent':
                1
active              