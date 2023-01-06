def get_keys_with_top_values(myDict):
    keysWithTopValues = []
    for key, value in myDict.items():
        if value == max(myDict.values()):
            keysWithTopValues.append(key)

    return keysWithTopValues