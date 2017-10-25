# base conversion quiz
import random
random.seed()


def dec2bin():
    d = random.randint(1,255)
    prompt = input("\nConvert {} decimal to binary:  ".format(d))
    b = '{:08b}'.format(d)
    b = b[:4] + ' ' + b[-4:]
    print("{} in decimal is {} in binary".format(d, b))

    
def dec2hex():
    d = random.randint(1,255)
    prompt = input("\nConvert {} decimal to hexadecimal:  ".format(d))
    h = '{:02X}'.format(d)
    print("{} in decimal is {} in hexadecimal".format(d, h))


def bin2dec():
    d = random.randint(1,255)
    b = '{:08b}'.format(d)
    b = b[:4] + ' ' + b[-4:]
    prompt = input("\nConvert {} binary to decimal:  ".format(b))
    print("{} in binary is {} in decimal".format(b, d))


def bin2hex():
    d = random.randint(1,255)
    b = '{:08b}'.format(d)
    b = b[:4] + ' ' + b[-4:]
    prompt = input("\nConvert {} binary to hexadecimal:  ".format(b))
    print("{} in binary is {:02X} in hexadecimal".format(b, d))

def hex2dec():
    d = random.randint(1,255)
    h = '{:02X}'.format(d)
    prompt = input("\nConvert {} hexadecimal to decimal:  ".format(h))
    print("{} in hexadecimal is {} in decimal".format(h, d))


def hex2bin():
    d = random.randint(1,255)
    b = '{:08b}'.format(d)
    b = b[:4] + ' ' + b[-4:]
    prompt = input("\nConvert {:02X} hexadecimal to binary:  ".format(d))
    print("{:02X} in hexadecimal is {} in binary".format(d, b))


def main():
    conversions = [dec2bin, dec2hex, bin2dec, bin2hex, hex2bin, hex2dec]

    while True:
        random.shuffle(conversions)

        for conversion in conversions:
            a = conversion()

        print()
        print('=' * 40)

if __name__ == '__main__':
    main()
