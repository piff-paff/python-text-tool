def removing_extra_spaces(text: str) -> str:
    text = text.split()
    return " ".join(text)


def words_count(text: str) -> int:
    return len(text.split())


def text_reverse(text: str) -> str:
    return text[::-1]
