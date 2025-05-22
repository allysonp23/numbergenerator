LOREM_WORDS = [
    "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit",
    "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore", "magna", "aliqua"
]

def generate_lorem(length):
    """
    Generate a Lorem Ipsum text truncated to the specified number of characters.
    """
    if length <= 0:
        return ""
    text = ""
    idx = 0
    while len(text) < length:
        if text:
            text += " "
        text += LOREM_WORDS[idx % len(LOREM_WORDS)]
        idx += 1
    return text[:length]
