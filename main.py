from functions import parse_args, load_terms_list, load_text, generate_three_word_phrases, vectorize_text
from sklearn.metrics.pairwise import cosine_similarity

def main():
    args = parse_args()
    terms_list = load_terms_list()
    text = load_text(args.text_path)

    three_word_phrases = generate_three_word_phrases(text)
    combined_text = three_word_phrases + terms_list

    combined_vectors, vector_model = vectorize_text(combined_text)

    three_word_phrase_vectors = combined_vectors[:len(three_word_phrases)]
    term_vectors = combined_vectors[len(three_word_phrases):]

    substitutions = False

    # Compare each three word phrase with standardised terms
    for i, phrase in enumerate(three_word_phrases):
        phrase_vector = three_word_phrase_vectors[i]
        for j, term in enumerate(terms_list):
            term_vector = term_vectors[j]
            similarity = cosine_similarity(phrase_vector, term_vector)[0][0]
            if similarity > args.threshold:
                substitutions = True
                print(f"Suggest to substitute '{phrase}' with '{term}'")

    if not substitutions:
        print("No substitutions were made")


if __name__ == '__main__':
    main()