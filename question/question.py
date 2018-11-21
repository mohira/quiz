import json
from pathlib import PosixPath


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
