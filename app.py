from pathlib import Path

from question.test.question_test import Question


def main():
    question_fp = Path(__file__).parent / "question.json"

    question = Question(question_fp)

    print("===== クイズスタート ======")

    while question.now_idx < len(question.all_questions):
        user_answer = input(f"第{question.now_idx + 1}問: {question.q()} > ")

        if question.answer(user_answer):
            print("正解！\n")
        else:
            print("残念！\n")

    print(f"終了: あなたのスコアは {question.score} でした")


if __name__ == "__main__":
    main()
