with open("story.txt", "r") as file:
    story = file.read()
start = -1
words = []
for i, char in enumerate(story):
    if char == "(":
        start = i
    elif char == ")" and start != -1:
        word = story[start:i+1]
        words.append(word)
        start = -1
for word in words:
    rep = input(f"Enter a word for {word}: ").strip()
    story = story.replace(word, rep)
print(story)
