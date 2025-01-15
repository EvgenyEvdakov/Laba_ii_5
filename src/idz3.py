#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from typing import Optional, Tuple


def generate_synthetic_tree(base_path: str, depth: int, breadth: int):
    """
    Генерация синтетического файлового дерева.
    :param base_path: Базовая директория для создания дерева.
    :param depth: Глубина дерева.
    :param breadth: Ширина (количество директорий или файлов на каждом уровне).
    """
    if depth == 0:
        return

    try:
        os.makedirs(base_path, exist_ok=True)
        for i in range(breadth):
            file_path = os.path.join(base_path, f"file_{i}.txt")
            with open(file_path, "w") as f:
                f.write("Sample content")

            dir_path = os.path.join(base_path, f"dir_{i}")
            generate_synthetic_tree(dir_path, depth - 1, breadth)
    except Exception as e:
        print(f"Ошибка при создании дерева: {e}")


def iterative_deepening_search(base_path: str, max_depth: int) -> Tuple[Optional[str], int]:
    """
    Поиск самого глубокого файла с использованием алгоритма итеративного углубления.
    :param base_path: Корневая директория для поиска.
    :param max_depth: Максимальная глубина поиска.
    :return: Кортеж с путем к самому глубокому файлу и его глубиной.
    """

    def dfs_limited(path: str, depth: int, limit: int) -> Tuple[Optional[str], int]:
        if depth > limit:
            return None, -1

        deepest_file = None
        deepest_level = -1

        try:
            for entry in os.scandir(path):
                if entry.is_file():
                    if depth > deepest_level:
                        deepest_file = entry.path
                        deepest_level = depth
                elif entry.is_dir():
                    file, level = dfs_limited(entry.path, depth + 1, limit)
                    if level > deepest_level:
                        deepest_file = file
                        deepest_level = level
        except PermissionError:
            pass  # Пропустить директории, к которым нет доступа

        return deepest_file, deepest_level

    if not os.path.exists(base_path):
        raise FileNotFoundError(f"Базовая директория {base_path} не существует.")

    deepest_file_overall = None
    deepest_level_overall = -1

    for depth_limit in range(1, max_depth + 1):
        file, level = dfs_limited(base_path, 0, depth_limit)
        if level > deepest_level_overall:
            deepest_file_overall = file
            deepest_level_overall = level

    return deepest_file_overall, deepest_level_overall


if __name__ == "__main__":
    synthetic_tree_path = "synthetic_tree"
    generate_synthetic_tree(synthetic_tree_path, depth=5, breadth=3)

    max_depth_to_search = 20
    deepest_file, deepest_level = iterative_deepening_search(synthetic_tree_path, max_depth_to_search)

    print(f"Самый глубокий файл: {deepest_file}, Глубина: {deepest_level}")
