def hannuota(A, B, C, n):  # A借用B移动n个盘子到C
    if n == 1:
        print(A + '->' + C)
        return

    hannuota(A, C, B, n - 1)
    print(A + '->' + C)
    hannuota(B, A, C, n - 1)


if __name__ == '__main__':
    # 汉诺塔
    hannuota('A', 'B', 'C', n=5)
