from nltk.corpus import wordnet
import string

# important: make sure you have NLTK's data
# if you dont, just run nltk.download("punkt")

# alphabet = [
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
#     'p', 'w', 'q', 'u', 'v', 's', 't', 'r', 'x', 'y', 'z'
# ]

# instead of above list
alphabet = list(string.ascii_lowercase)

# make sure all characters are there
print(len(alphabet)) 

def corrector(word):
    # reutrn the word if its correct
    if wordnet.synsets(word):
        return word

    else:
        result = []
        for i in range(0, len(word) + 1):
            before = str(word[0:i])
            after = str(word[i:len(word)])
            for alpha in alphabet:
                # replacing all of alphabet with all of the word characters
                # to finding words in wordnet
                new = before + alpha + after
                if wordnet.synsets(new):
                    result.append(new)
        return set(result)


if __name__ == "__main__":
    word = input('Enter a wrong word (Example: hllo): ')
    print(corrector(word))
