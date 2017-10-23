import random
import string
import sys
import time


def generate_random_bit_from_nanoseconds():
    random.seed()
    time.sleep(random.randint(0, 127)*1e-4)
    cur_time_str = str('%.9f' % time.time())
    nanoseconds = int(cur_time_str[-1])
    bit = 1 if nanoseconds & 1 else 0
    return bit


def generate_random_byte():
    byte = 0
    for i in range(0, 7):
        byte += pow(2, i)*generate_random_bit_from_nanoseconds()
    return byte


def generate_rand_pass(length):
    password = ''
    count = 0
    while count != length:
        byte = chr(generate_random_byte())
        if byte in string.ascii_letters or byte in string.digits:
            password += byte
            count += 1
    print(password)


def main():
    if len(sys.argv) == 2:
        generate_rand_pass(int(sys.argv[1]))
    else:
        sys.exit('You need to specify the password size as first argument')

if __name__ == "__main__":
    main()
