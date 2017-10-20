import random
import string
import sys
import time


def generate_random_byte_from_nanoseconds():
    random.seed()
    cur_time_str = str('%.9f' % time.time())
    nanoseconds = int(cur_time_str.split('.')[1])
    byte = nanoseconds.to_bytes(4, byteorder='big')[3]
    time.sleep(random.randint(0, 255)*1e-9)
    return byte


def generate_rand_pass(length):
    password = ''
    count = 0
    while count != length:
        byte = chr(generate_random_byte_from_nanoseconds())
        if byte in string.ascii_letters or byte in string.digits:
            password += byte
            count += 1
    print(password)


def main():
    if len(sys.argv) == 1:
        generate_rand_pass(sys.argv[1])
    else:
        sys.exit('You need to specify the password size as first argument')


if __name__ == "__main__":
    main()
