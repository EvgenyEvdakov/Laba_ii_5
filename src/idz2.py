#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Поиск в файловой системе


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, *args):
        for child in args:
            self.add_child(child)

    def repr(self):
        return f"<{self.value}>"


def depth_limited_search(node, goal, limit, path):
    if limit < 0:
        return "cutoff"
    if node is None:
        return None

    # Добавим текущий узел в путь
    path.append(node.value)

    if node.value == goal:
        return path[:]  # Возвращаем копию пути до текущего узла

    cutoff_occurred = False
    for child in node.children:
        result = depth_limited_search(child, goal, limit - 1, path)
        if result == "cutoff":
            cutoff_occurred = True
        elif result is not None:
            return result  # Возвращаем найденный путь

    # Удаляем узел из пути, если нет результата в его ветке
    path.pop()
    return "cutoff" if cutoff_occurred else None


def iterative_deepening_search(root, goal):
    max_depth = 10  # Максимальная глубина для поиска
    for limit in range(max_depth):
        path = []  # Путь от корня до целевого узла
        result = depth_limited_search(root, goal, limit, path)
        if result is not None and result != "cutoff":
            return " -> ".join(result)  # Форматируем вывод пути
    return "Целевой файл не найден"


if __name__ == "__main__":
    # Построение дерева
    root = TreeNode("dir1")
    root.add_child(TreeNode("dir2"))
    root.add_child(TreeNode("dir3"))
    root.children[0].add_child(TreeNode("file4"))
    root.children[1].add_child(TreeNode("file5"))
    root.children[1].add_child(TreeNode("file6"))

    # Цель поиска
    goal = "file5"

    # Проверка существования узла и получение пути
    path = iterative_deepening_search(root, goal)
    print(path)
