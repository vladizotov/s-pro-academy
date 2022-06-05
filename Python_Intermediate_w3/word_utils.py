def clear_sentence_from_punctuation_marks(sentence):
    punctuation_marks = [".", ",", ":", ";", "(", ")", "!", "?", "-", "«", "»"]

    counter = 0
    while counter < len(punctuation_marks):
        sentence = sentence.replace(punctuation_marks[counter], '')
        counter += 1

    if sentence.find('  ') != -1:
        sentence = sentence.replace('  ', ' ')

    return sentence

def list_of_words_from_sentence(sentence):
    return clear_sentence_from_punctuation_marks(sentence).split()


def the_longest_word_from_sentence(sentence):
    the_longest_word = ''
    list_if_there_are_several_words = []

    for index in list_of_words_from_sentence(sentence):
        if len(index) == len(the_longest_word):
            list_if_there_are_several_words.append(index)
        if len(index) > len(the_longest_word):
            the_longest_word = index
            list_if_there_are_several_words.clear()

    if len(list_if_there_are_several_words) > 0:
        list_if_there_are_several_words.append(the_longest_word)
        return list_if_there_are_several_words
    else:
        return the_longest_word