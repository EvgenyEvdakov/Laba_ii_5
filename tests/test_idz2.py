#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from idz2 import TreeNode, iterative_deepening_search

class TestFileSearch(unittest.TestCase):
    def setUp(self):
        # Построение тестового дерева
        self.root = TreeNode("dir1")
        dir2 = TreeNode("dir2")
        dir3 = TreeNode("dir3")
        file4 = TreeNode("file4")
        file5 = TreeNode("file5")
        file6 = TreeNode("file6")

        self.root.add_children(dir2, dir3)
        dir2.add_child(file4)
        dir3.add_children(file5, file6)

    def test_file_exists(self):
        # Тест на существующий файл
        result = iterative_deepening_search(self.root, "file5")
        self.assertEqual(result, "dir1 -> dir3 -> file5")

    def test_file_not_exists(self):
        # Тест на отсутствующий файл
        result = iterative_deepening_search(self.root, "file7")
        self.assertEqual(result, "Целевой файл не найден")

    def test_search_in_root(self):
        # Тест, когда целевой узел - корень
        result = iterative_deepening_search(self.root, "dir1")
        self.assertEqual(result, "dir1")

    def test_search_in_nested_file(self):
        # Тест поиска вложенного файла
        result = iterative_deepening_search(self.root, "file4")
        self.assertEqual(result, "dir1 -> dir2 -> file4")

    def test_empty_tree(self):
        # Тест на пустое дерево
        empty_root = None
        result = iterative_deepening_search(empty_root, "file1")
        self.assertEqual(result, "Целевой файл не найден")

    def test_single_node_tree(self):
        # Тест дерева с единственным узлом
        single_node = TreeNode("file1")
        result = iterative_deepening_search(single_node, "file1")
        self.assertEqual(result, "file1")
        result_not_found = iterative_deepening_search(single_node, "file2")
        self.assertEqual(result_not_found, "Целевой файл не найден")


if __name__ == "__main__":
    unittest.main()