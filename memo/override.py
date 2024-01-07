from sys import stdin

class spot:
    def __init__(self, xy):
        self.x = xy[0]
        self.y = xy[1]

    # 비교 : <
    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        else:
            return self.x < other.x

    # 비교 : ==
    def __eq__(self, other):
        return self.x == other.x

    def __str__(self):
        return f"{self.x} {self.y}"

if __name__ == "__main__":
    size = int(stdin.readline())
    spotList = []

    for _ in range(size):
        newSpot = spot(list(map(int, stdin.readline().split())))
        spotList.append(newSpot)

    spotList.sort()

    for s in spotList:
        print(s)