def merge_the_tools(s, k):
    result = []

    for i in range(0, len(s), k):
        part = s[i:i+k]
        seen = ""

        for ch in part:
            if ch not in seen:
                seen += ch

        result.append(seen)

    return result
