class EmojiConveter:
    def convert_happy_sad_face(self, words, emojis):
        output = ""
        for word in words:
            output += emojis.get(word, word) + " "
        print(output)


message = input("Enter a message with your mood: ")
words = message.split(" ")
emojis = {
    ":)":"😊",
    ":(":"😒",
    ":-D":"😁",
    ":’-(":"😢",
    ";-)":"😜",
    ":-/":"😑",
    ":-O":"😮",
    "X-(":"😡"
}
emoji_object = EmojiConveter()
emoji_object.convert_happy_sad_face(words, emojis)