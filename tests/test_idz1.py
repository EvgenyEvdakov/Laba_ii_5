#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import unittest


sys.path.append("../src")
from idz1 import BinaryTreeNode, iterative_deepening_search


class TestIterativeDeepeningSearch(unittest.TestCase):
    def setUp(self):
        # Построение дерева для тестов
        self.root = BinaryTreeNode(1)
        left_child = BinaryTreeNode(2)
        right_child = BinaryTreeNode(3)
        self.root.add_children(left_child, right_child)
        right_child.add_children(BinaryTreeNode(4), BinaryTreeNode(5))

    def test_node_exists(self):
        # Тест на существующий узел
        self.assertTrue(iterative_deepening_search(self.root, 4))

    def test_node_not_exists(self):
        # Тест на отсутствующий узел
        self.assertFalse(iterative_deepening_search(self.root, 6))

    def test_root_node(self):
        # Тест, когда целевой узел - корень
        self.assertTrue(iterative_deepening_search(self.root, 1))

    def test_leaf_node(self):
        # Тест на листовой узел
        self.assertTrue(iterative_deepening_search(self.root, 5))

    def test_empty_tree(self):
        # Тест на пустое дерево
        empty_tree = None
        self.assertFalse(iterative_deepening_search(empty_tree, 1))


if __name__ == "__main__":
    unittest.main()
