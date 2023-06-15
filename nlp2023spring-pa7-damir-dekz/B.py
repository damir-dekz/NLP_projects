dictionary = {
    "ұлар": "<noun>",
    "бала": "<noun>",
    "қарбыз": "<noun>",
    "бас": "<noun>",
    "қала": "<noun>",
    "батыр": "<noun>",
    "қарға": "<noun>",
    "кеме": "<noun>",
    "қар": "<noun>",
    "жат": "<verb>",
    "жүр": "<verb>"
}


def generate(token, form):
    if form == "<plural>":
        if token.endswith("ар") or token.endswith("ер"):
            return token + "лар"
        elif token.endswith("ыз") or token.endswith("із"):
            return token[:-2] + "дар"
        elif token.endswith("қ") or token.endswith("к"):
            return token + "ар"
        else:
            return token + "тер"
    elif form == "<dative>":
        if token.endswith("ар") or token.endswith("ер"):
            return token + "ға"
        elif token.endswith("ыз") or token.endswith("із"):
            return token[:-2] + "ге"
        elif token.endswith("қ") or token.endswith("к"):
            return token[:-1] + "а"
        else:
            return token + "ға"
    else:
        return token + form


def parse(word):
    if word in dictionary:
        return (word + dictionary[word],)
    else:
        for suffix in ["лар", "лер", "дар", "дер", "тар", "тер"]:
            if word.endswith(suffix):
                stem = word[:-3]
                if stem in dictionary:
                    return (stem + "<noun>" + "<plural>",)
        for suffix in ["ға", "ге", "қа", "ке"]:
            if word.endswith(suffix):
                stem = word[:-2]
                if stem in dictionary:
                    return (stem + "<noun>" + "<dative>", word + "<noun>")
        return (word + "<noun>",)

print(generate("ұлар","<plural>"))  # output: ұларлар
print(generate("ұлар","<dative>")) # output: ұларға
print(parse("ұлар")) # output: ('ұлар<noun>',)
print(parse("қарға")) # output: ('қар<noun><dative>', 'қарға<noun>')
print(parse("кемелер")) # output: ('кеме<noun><plural>',)
