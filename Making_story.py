with open("Mad Libs Story.txt", "r") as f:
    story = f.read()

words = set()
start_words = -1
start = "<"
end = ">"

for i, char in enumerate(story):
    if char == start:
        start_words = i
    if char == end and start_words != -1:
        word = story[start_words : i+1]
        words.add(word)
        start_words = -1

answers = {}

for word in words:
    answer = input("Enter a word for a " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])


print(story)

