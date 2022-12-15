def splitInto(text, numPortions):
    """Splits the given text into the given number of portions.
    Returns a list of strings, each of which is a portion of the text.
    """
    portions = []
    portionSize = len(text) // numPortions
    for i in range(numPortions):
        start = i * portionSize
        end = (i + 1) * portionSize
        portions.append(text[start:end])

    if len(text) % numPortions != 0:
        portions.append(
            text[end:]
        )  # adds the last portion if numPortions doesn't divide text
        # so shouldn't really be needed

    return portions


def splitIntoChunks(text, chunkSize):
    """Splits the given text into chunks of the given size.
    Returns a list of strings, each of which is a chunk of the text.
    """
    return [text[i : i + chunkSize] for i in range(0, len(text), chunkSize)]


def splitEvery(text, numChars):
    """Splits the given text into groups of every numChars letters.
    Returns a list of strings.
    """
    return [
        "".join([text[ii] for ii in range(i, len(text), numChars)])
        for i in range(numChars)
    ]


def splitListInto(text, numChars):
    """Splits the given text into groups of every numChars letters.
    Returns a list of strings.
    """
    return [[text[ii] for ii in range(i, len(text), numChars)] for i in range(numChars)]


def splitListIntoChunks(text, chunkSize):
    """Splits the given text into chunks of the given size.
    Returns a list of strings, each of which is a chunk of the text.
    """
    return [text[i : i + chunkSize] for i in range(0, len(text), chunkSize)]


def cleanTextIntoLetters(inp: str):
    """Strips the given text of all punctuation, line breaks and
       spaces. 
    """
    inp = "".join(inp.strip().split()).upper()
    out = ""
    for i in inp:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            out += i
    return out
    

if __name__ == "__main__":
    text = "abcdefghijklmnopqrstuvwxyz"

    print(splitInto(text, 3))
    print(splitIntoChunks(text, 3))
    print(splitEvery(text, 3))
    print(splitInto(splitInto(text, 3), 2))
