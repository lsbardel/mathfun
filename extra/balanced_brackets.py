

def isBalanced(S):
    close = {')': '(', ']': '[', '}': '{'}
    open = set(close.values())
    stack = []
    for c in S:
        if c in open:
            stack.append(c)
        elif c in close:
            if stack and stack.pop() == close[c]:
                continue
            return 'NO'
    return 'NO' if stack else "YES"


if __name__ == '__main__':
    print('%s=Yes' % isBalanced('{[()]}'))
    print('%s=No' % isBalanced('{[(])}'))
    print('%s=Yes' % isBalanced('{{[[(())]]}}'))
