def single_root_words(root_world, *other_words):
    same_words = []
    for word in other_words:
        if root_world.lower() in word.lower() or word.lower() in root_world.lower():
            same_words += [word]
    return same_words

print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
