from collections import Counter


# Read the training text
with open("input.txt", "r", encoding="utf-8") as file:
    input_text = file.read()

# Target vocabulary size
vocab_size = 5000


def train(input_text, vocab_size):
    """
    Train a simple Byte Pair Encoding (BPE) tokenizer.
    """

    # Split the input text into individual character tokens
    tokens = list(input_text)

    # Initialize the vocabulary with unique characters
    vocab = sorted(set(tokens))

    # Store all merge operations
    merges = []

    # Continue merging until the target vocabulary size is reached
    while len(vocab) < vocab_size:

        # Count the frequency of every adjacent token pair
        count = Counter()

        for i in range(len(tokens) - 1):
            pair = (tokens[i], tokens[i + 1])
            count[pair] += 1

        # Stop if there are no more pairs to merge
        if not count:
            break

        # Select the most frequent pair
        best_pair, best_count = count.most_common(1)[0]

        # Merge every occurrence of the best pair
        tokens = merge(tokens, best_pair)

        # Create the merged token
        new_token = best_pair[0] + best_pair[1]

        # Save the merge rule
        merges.append((best_pair, new_token))

        # Add the new token to the vocabulary
        vocab = sorted(set(vocab + [new_token]))

    return vocab, merges


def merge(tokens, pair):
    """
    Merge every occurrence of the given token pair into a single token.
    """

    result = []
    i = 0

    # Traverse the token sequence
    while i < len(tokens):

        # Merge if the current and next token match the target pair
        if (
            i < len(tokens) - 1
            and tokens[i] == pair[0]
            and tokens[i + 1] == pair[1]
        ):
            result.append(pair[0] + pair[1])
            i += 2

        # Otherwise, keep the current token unchanged
        else:
            result.append(tokens[i])
            i += 1

    return result


# Train the tokenizer
vocab, merges = train(input_text, vocab_size)

print(f"Vocabulary Size: {len(vocab)}")
print(f"Number of Merges: {len(merges)}")
