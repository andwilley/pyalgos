def generateParenthesis(self, n: int) -> List[str]:
    if n == 0:
        return [""]
    if n < 0:
        return []
    return self.paren_builder(["("], n - 1, 1)

def paren_builder(self, curr, opens, closes):
    if opens == closes == 0:
        return [''.join(curr)]
    close = []
    opn = []
    if closes:
        close = self.paren_builder(curr + [")"], opens, closes - 1)
    if opens:
        opn = self.paren_builder(curr + ["("], opens - 1, closes + 1)
    return close + opn
