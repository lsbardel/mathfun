from string import ascii_lowercase


def cipher(codes):
    while True:
        keys = {}
        while True:
            s = 0
            for c in ascii_lowercase:
                if c in keys:
                    continue
                key = ord(c)
                i = len(keys)
                for code in codes[i::3]:
                    b = code ^ key
                    if 31 < b < 127:
                        s += b
                    else:
                        s = 0
                        break
                if s:
                    keys[c] = s
                    break
    return s


if __name__ == '__main__':
    import requests
    codes = list(map(int, requests.get(
        'https://projecteuler.net/project/resources/p059_cipher.txt'
    ).text.split(',')))
    print(cipher(codes))
