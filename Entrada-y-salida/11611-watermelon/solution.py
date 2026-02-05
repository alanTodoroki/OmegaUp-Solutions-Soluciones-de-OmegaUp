#11611. Watermelon
def solve() -> None:
    try:
        line = input()
        if not line:
            return
        
        w = int(line)
        if w > 2 and w % 2 == 0:
            print("SI")
        else:
            print("NO")
    except EOFError:
        pass

if __name__ == '__main__':
    solve()
