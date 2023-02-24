import sys
from bitmap import BITMAP

COLOR_TEXT = '\u001b[31m'


def main():
    print('Enter the message to display with the bitmap.')
    message = input('> ')
    print(COLOR_TEXT)
    if not message:
        sys.exit()

    for line in BITMAP.splitlines():
        for i, bit in enumerate(line):
            if bit == ' ':
                print(' ', end='')
            else:
                print(message[i % len(message)], end='')
        print()


if __name__ == '__main__':
    main()
