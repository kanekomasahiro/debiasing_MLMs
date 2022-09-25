import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    tp = lambda x:list(x.split(','))

    parser.add_argument('--input', type=str, required=True, help='Data')
    parser.add_argument('--output', type=str, required=True, help='Data')
    parser.add_argument('--dev_data_size', type=int, default=10000)

    args = parser.parse_args()

    return args


def split_data(input, dev_data_size):
    dev = input[:dev_data_size]
    train = input[dev_data_size:]

    return train, dev

def main(args):
    data = [l.strip() for l in open(args.input)]
    
    train_data, dev_data = split_data(data, 10000)

    train_fw = open(args.output + "_train.txt", "w")
    dev_fw = open(args.output + "_dev.txt", "w")

    for line in train_data:
        train_fw.write(line + "\n")
    
    for line in dev_data:
        dev_fw.write(line + "\n")


if __name__ == "__main__":
    args = parse_args()
    main(args)
