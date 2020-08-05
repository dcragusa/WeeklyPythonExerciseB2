import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType(), help='The file to process')
    parser.add_argument('-s', '--start', default=3, type=int, help='How many lines to show from the start')
    parser.add_argument('-e', '--end', default=3, type=int, help='How many lines to show from the end')
    args = parser.parse_args()

    if args.start < 0 or args.end < 0:
        raise ValueError('Lines cannot be negative.')

    with args.file as f:
        lines = f.readlines()
        for line in lines[:args.start]:
            print(line, end='')
        if args.end:
            for line in lines[-args.end:]:
                print(line, end='')
