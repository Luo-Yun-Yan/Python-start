def hanoi(n, source, temp, target):
    """
    递归解决汉诺塔问题
    n: 盘子数量
    source: 起始柱
    temp: 辅助柱
    target: 目标柱
    """
    # 终止条件：1个盘子直接从 source 移到 target
    if n == 1:
        print(f"移动盘子 {n} 从 {source} 到 {target}")
    else:
        # 步骤1：将 n-1 个盘子从 source 移到 temp（用 target 辅助）
        hanoi(n - 1, source, target, temp)

        # 步骤2：将第 n 个盘子从 source 移到 target
        print(f"移动盘子 {n} 从 {source} 到 {target}")

        # 步骤3：将 n-1 个盘子从 temp 移到 target（用 source 辅助）
        hanoi(n - 1, temp, source, target)


# 测试：移动 3 个盘子 (A->C, 用 B 辅助)
hanoi(3, 'A', 'B', 'C')