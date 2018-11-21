import json
import unittest
from pathlib import Path, PosixPath


class Question:

    def __init__(self, question_fp: PosixPath):
        with open(question_fp) as f:
            self.all_questions = json.load(f)

        self.now_idx = 0
        self.score = 0

    def q(self) -> str:
        return self.all_questions[self.now_idx]["q"]

    def a(self) -> str:
        return self.all_questions[self.now_idx]["a"]

    def answer(self, user_answer: str) -> bool:
        is_collect = self.is_collect(user_answer)

        if is_collect:
            self.score += 1

        self.now_idx += 1

        return is_collect

    def is_collect(self, user_answer: str) -> bool:
        return self.a() == user_answer


class QuestionTest(unittest.TestCase):
    def setUp(self):
        question_fp = Path(__file__).parent / "fixture.json"

        self.question = Question(question_fp)

    def test_1問目を出題できる(self):
        self.assertEqual("東京都の県庁所在地は？", self.question.q())

    def test_1問目の解答を取得できる(self):
        self.assertEqual("新宿区", self.question.a())

    def test_問題を取得できる(self):
        expected = [
            {"q": "東京都の県庁所在地は？", "a": "新宿区"},
            {"q": "1+1=？", "a": "2"},
            {"q": "3+4=？", "a": "7"}
        ]

        self.assertEqual(expected, self.question.all_questions)

    def test_1問目に回答したら正解不正解が分かる(self):
        with self.subTest("正解の場合"):
            self.assertTrue(self.question.answer("新宿区"))

        with self.subTest("不正解の場合"):
            self.assertFalse(self.question.answer("中央区"))

    def test_1問目に回答したら2問目になる(self):
        self.question.answer("新宿区")

        self.assertEqual(1, self.question.now_idx)

    def test_正解数を記憶できる(self):
        self.question.answer("新宿区")
        self.question.answer("2")
        self.question.answer("7")

        self.assertEqual(3, self.question.score)


if __name__ == "__main__":
    unittest.main()
