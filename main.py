import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer

nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

input_text = """Python is a high-level, general-purpose programming language.
Its design philosophy emphasizes code readability with the use of significant indentation.
Python is dynamically typed and garbage-collected.
It supports multiple programming paradigms, including structured (particularly procedural),
object-oriented and functional programming. 
It is often described as a "batteries included" language due to its comprehensive standard library."""
with open('input_text.txt', 'w') as f:
    f.write(input_text)

with open('input_text.txt', 'r') as f:
    text = f.read()

tokens = word_tokenize(text)
print(f"Tokens: {tokens}")

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

lemmas = [lemmatizer.lemmatize(word) for word in tokens]
stems = [stemmer.stem(word) for word in tokens]
print(f"Lemmas: {lemmas}")
print(f"Stems: {stems}")

stop_words = set(stopwords.words('english'))
tokens_without_stopwords = [word for word in tokens if word.lower() not in stop_words]
print(f"Without stopwords: {tokens_without_stopwords}")

tokens_clean = [word for word in tokens_without_stopwords if word.isalpha()]
print(f"Without punctuation: {tokens_clean}")

with open('output_text.txt', 'w') as f:
    f.write(' '.join(tokens_clean))

print("The processed text is saved in 'output_text.txt'")
