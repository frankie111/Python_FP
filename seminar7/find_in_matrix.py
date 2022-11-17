def find(m, elem):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if m[i][j] == elem:
                return i, j

    return -1, -1


def neighbor(er, ec):
    return (er[0] == ec[0] and (er[1] == ec[1] - 1 or er[1] == ec[1] + 1)) or (
            er[1] == ec[1] and (er[0] == ec[0] - 1 or er[0] == ec[0] + 1))


def solution(m, word):
    last_pos = find(m, word[0])

    for i in range(1, len(word)):
        pos = find(m, word[i])
        if pos == (-1, -1):
            return False

        if not neighbor(last_pos, pos):
            return False

        last_pos = pos

    return True


mat = [
    ['A', 'B', 'C', 'D'],
    ['L', 'E', 'G', 'H'],
    ['Q', 'R', 'T', 'F']
]

string = "ALERT"

print(solution(mat, string))
