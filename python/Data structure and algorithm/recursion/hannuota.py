def moveTower(height, fromPole, withPole, toPole):
    if height >= 1:
        moveTower(height - 1, fromPole, toPole, withPole)#倒数第二个盘子，由第一根柱子，经过中间柱子，到达最后一根柱子
        moveDisk(height, fromPole, toPole)#倒数第一个盘子，由第一根柱子，到达最后一根柱子
        moveTower(height - 1, withPole, fromPole, toPole)#倒数第二个盘子，由第二根柱子，经过第一根柱子，到达最后一根柱子)


def moveDisk(disk, fromPole, toPole):
    print(f"Moving disk[{disk}] from {fromPole} to {toPole}")


moveTower(2, "#1", "#2", "#3")