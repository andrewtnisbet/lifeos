KEYWORDS = {
    "resume": {
        "priority": 8,
        "energy": "high",
        "minutes": 45
    },

    "doctor": {
        "priority": 7,
        "energy": "low",
        "minutes": 10
    },

    "woodshop": {
        "priority": 5,
        "energy": "medium",
        "minutes": 30
    }
}


def classify_text(text: str):

    text = text.lower()

    for keyword, metadata in KEYWORDS.items():

        if keyword in text:

            return metadata

    return {
        "priority": 5,
        "energy": "medium",
        "minutes": 15
    }