from string import ascii_lowercase, ascii_uppercase


def simple_encrypt(S, K):
    stack = []
    for s in S:
        ascii = ascii_lowercase
        idx = ascii.find(s)
        if idx == -1:
            ascii = ascii_uppercase
            idx = ascii.find(s)
        if idx > -1:
            idx = (idx + K) % len(ascii)
            s = ascii[idx]
        stack.append(s)
    return ''.join(stack)


if __name__ == '__main__':
    print(simple_encrypt('middle-Outz', 2))
