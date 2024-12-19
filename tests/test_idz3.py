#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
import unittest
from idz3 import generate_synthetic_tree, iterative_deepening_search


class TestSyntheticTree(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Создаем тестовую директорию перед всеми тестами.
        """
        cls.test_dir = "test_synthetic_tree"
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)  # Удаляем, если уже существует
        os.makedirs(cls.test_dir)

    @classmethod
    def tearDownClass(cls):
        """
        Удаляем тестовую директорию после всех тестов.
        """
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)

    def setUp(self):
        """
        Очищаем содержимое тестовой директории перед каждым тестом.
        """
        for item in os.listdir(self.test_dir):
            item_path = os.path.join(self.test_dir, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)

    def test_generate_synthetic_tree(self):
        """
        Тестируем функцию генерации дерева.
        """
        generate_synthetic_tree(self.test_dir, depth=3, breadth=2)

        # Проверяем, что дерево создано
        dir_path = os.path.join(self.test_dir, "dir_0", "dir_0")
        file_path = os.path.join(self.test_dir, "dir_0", "file_0.txt")

        self.assertTrue(os.path.exists(dir_path))
        self.assertTrue(os.path.isfile(file_path))

    def test_no_files_in_tree(self):
        """
        Тестируем, если в дереве вообще нет файлов.
        """
        os.makedirs(os.path.join(self.test_dir, "empty_dir"))

        # Ищем в дереве без файлов
        deepest_file, deepest_level = iterative_deepening_search(self.test_dir, max_depth=10)

        self.assertIsNone(deepest_file)
        self.assertEqual(deepest_level, -1)

    def test_permission_error_handling(self):
        """
        Тестируем обработку ошибки PermissionError.
        """
        # Создаем директорию без доступа
        restricted_dir = os.path.join(self.test_dir, "restricted")
        os.makedirs(restricted_dir)
        os.chmod(restricted_dir, 0)  # Убираем права доступа

        try:
            # Пытаемся выполнить поиск
            deepest_file, deepest_level = iterative_deepening_search(self.test_dir, max_depth=10)

            # Проверяем, что ошибка доступа не нарушила работу
            self.assertIsNone(deepest_file)
            self.assertEqual(deepest_level, -1)
        finally:
            # Возвращаем права доступа, чтобы можно было удалить директорию
            os.chmod(restricted_dir, 0o777)
            shutil.rmtree(restricted_dir)


if __name__ == "__main__":
    unittest.main()