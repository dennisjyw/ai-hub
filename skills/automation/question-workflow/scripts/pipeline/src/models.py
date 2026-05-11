"""
資料模型定義
使用 dataclass 定義題目的完整屬性
"""
from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class Question:
    """單一題目的完整資訊"""
    # 來源資訊
    year: str = ""  # 年度
    number: int = 0  # 題號
    subject_category: str = ""  # 類科/子科目

    # 分類（來自知識樹）
    level_1: str = ""  # 第一層分類（父分類）
    level_2: str = ""  # 第二層分類（子分類）
    level_3: str = ""  # 第三層分類（孫分類）

    # 題目內容
    question_stem: str = ""  # 題幹
    option_a: str = ""  # 選項 A
    option_b: str = ""  # 選項 B
    option_c: str = ""  # 選項 C
    option_d: str = ""  # 選項 D

    # 答案與解析
    answer: str = ""  # 正確答案（如 "A", "B", "C", "D"）
    explanation: str = ""  # 題目解析
    explanation_a: str = ""  # 選項 A 的解析
    explanation_b: str = ""  # 選項 B 的解析
    explanation_c: str = ""  # 選項 C 的解析
    explanation_d: str = ""  # 選項 D 的解析

    # 難度資訊
    difficulty: Optional[float] = None  # 難度分數

    # 其他屬性
    question_type: str = "單選"  # 題型（單選、問答、複選、手寫、計算、混合題）
    category: str = "純文字"  # 內容類別（純文字、圖片、文字+圖片、文字+公式、文字+圖片+公式）

    # 圖片資訊
    has_question_image: bool = False  # 題幹是否有圖片
    has_option_images: bool = False  # 選項是否有圖片
    image_filename: Optional[str] = None  # 圖片檔名

    # 原始分類字串（用於匹配知識樹）
    raw_category: str = ""

    def to_dict(self):
        """轉換為字典"""
        return {
            "subject_category": self.subject_category,
            "year": self.year,
            "number": self.number,
            "level_1": self.level_1,
            "level_2": self.level_2,
            "level_3": self.level_3,
            "question_stem": self.question_stem,
            "option_a": self.option_a,
            "option_b": self.option_b,
            "option_c": self.option_c,
            "option_d": self.option_d,
            "answer": self.answer,
            "explanation": self.explanation,
            "explanation_a": self.explanation_a,
            "explanation_b": self.explanation_b,
            "explanation_c": self.explanation_c,
            "explanation_d": self.explanation_d,
            "difficulty": self.difficulty,
            "question_type": self.question_type,
            "category": self.category,
            "has_question_image": self.has_question_image,
            "has_option_images": self.has_option_images,
            "image_filename": self.image_filename,
        }
