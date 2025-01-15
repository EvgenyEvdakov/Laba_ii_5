#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Поиск элемента в дереве с использованием алгоритма итеративного углубления


class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def add_children(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.value}>"


def depth_limited_search(node, goal, limit):
    if limit < 0:
        return "cutoff"
    if node is None:
        return None
    if node.value == goal:
        return True

    left_result = depth_limited_search(node.left, goal, limit - 1)
    if left_result is True:
        return True
    elif left_result == "cutoff":
        cutoff = "cutoff"
    else:
        cutoff = None

    right_result = depth_limited_search(node.right, goal, limit - 1)
    if right_result is True:
        return True
    elif right_result == "cutoff":
        cutoff = "cutoff"

    return cutoff


def iterative_deepening_search(root, goal):
    max_depth = 10  # Максимальная глубина для поиска
    for limit in range(max_depth):
        result = depth_limited_search(root, goal, limit)
        if result is True:
            return True
        elif result is None:
            break  # Если результат None, то узел не найден
    return False  # Если ничего не найдено


if __name__ == "__main__":
    # Построение дерева
    root = BinaryTreeNode(1)
    left_child = BinaryTreeNode(2)
    right_child = BinaryTreeNode(3)
    root.add_children(left_child, right_child)
    right_child.add_children(BinaryTreeNode(4), BinaryTreeNode(5))

    # Целевое значение
    goal = 4

    # Проверка существования узла
    exists = iterative_deepening_search(root, goal)
    print(exists)
