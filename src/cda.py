from re import template


import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, required=True)
    parser.add_argument('--output', type=str, required=True)
    args = parser.parse_args()

    return args


def main(args):
    feminine_words = [line.strip() for line in open("word_lists/female.txt")]
    masculine_words = [line.strip() for line in open("word_lists/male.txt")]

    data = []

    for line in open(args.input):
        words = line.strip().split()
        data.append(" ".join(words))
        lowered_words = [word.lower() for word in words]

        for idx, feminine_word in enumerate(feminine_words):
            if feminine_word in lowered_words:
                words = [masculine_words[idx] if lowered_word == feminine_word else word for word, lowered_word in zip(words, lowered_words)]
        for idx, masculine_word in enumerate(masculine_words):
            if masculine_word in lowered_words:
                words = [feminine_words[idx] if lowered_word == masculine_word else word for word, lowered_word in zip(words, lowered_words)]
                data.append(" ".join(words))

    fw = open(args.output, "w")

    for line in data:
        fw.write(line + "\n")


if __name__ == "__main__":
    args = parse_args()
    main(args)
