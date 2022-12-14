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

    portions.append(
        text[end:]
    )  # adds the last portion if numPortions doesn't divide text
    # so shouldn't really be needed

    return portions


def splitEvery(text, numChars):
    """Splits the given text into portions of the given number of characters.
    Returns a list of strings, each of which is a portion of the text.
    """
    portions = []
    for i in range(0, len(text), numChars):
        portions.append(text[i : i + numChars])
    return portions


if __name__ == "__main__":
    text = "abcdefghijklmnopqrstuvwxyz"
    print(splitInto(text, 3))
