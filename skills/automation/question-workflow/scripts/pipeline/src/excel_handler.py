"""
Excel Handler - 處理 Excel 檔案的讀寫
使用 pandas 載入驗證用的知識樹、讀取難易度配分，並匯出結果
"""
import pandas as pd
from typing import List, Optional, Dict, Tuple
from pathlib import Path

from .models import Question


class ExcelHandler:
    """處理 Excel 檔案的讀寫"""

    def __init__(self, knowledge_path: str, difficulty_path: str):
        """
        初始化 Excel 處理器

        Args:
            knowledge_path: 知識樹架構 Excel 檔案路徑
            difficulty_path: 難度評分 Excel 檔案路徑
        """
        self.knowledge_path = knowledge_path
        self.difficulty_path = difficulty_path

        # 載入知識樹
        self.knowledge_df = None
        if knowledge_path:
            self.knowledge_df = pd.read_excel(knowledge_path)

        # 載入難度評分
        self.difficulty_data = {}  # 格式: {year: {number: score}}
        self.difficulty_df = None
        if difficulty_path:
            self.difficulty_df = pd.ExcelFile(difficulty_path)
            self._load_difficulty_data()

    def _load_difficulty_data(self):
        """載入難度評分資料"""
        for sheet_name in self.difficulty_df.sheet_names:
            try:
                df = pd.read_excel(self.difficulty_df, sheet_name=sheet_name)
                year = sheet_name
                year_data = {}

                for _, row in df.iterrows():
                    # 跳過標題行
                    if row["題號"] == "Number":
                        continue

                    # 跳過 NaN 題號
                    if pd.isna(row["題號"]) or row["題號"] == "Number":
                        continue

                    try:
                        number = int(row["題號"])
                        score = row["最終評分"]
                        if not pd.isna(score):
                            year_data[number] = score
                    except (ValueError, TypeError):
                        continue

                if year_data:
                    self.difficulty_data[year] = year_data
            except Exception as e:
                print(f"載入 Sheet {sheet_name} 時發生錯誤: {e}")
                continue

    def find_knowledge(self, subject: str, raw_category: str) -> Tuple[str, str, str]:
        """
        根據科目和原始分類查找知識樹

        Args:
            subject: 科目（國文/英語）
            raw_category: 原始分類字串

        Returns:
            (level_1, level_2, level_3)
        """
        if self.knowledge_df is None:
            return "", "", ""

        # 過濾該科目的資料
        subject_df = self.knowledge_df[self.knowledge_df["Subject"] == subject]

        if subject_df.empty:
            return "", "", ""

        # 嘗試根據原始分類字串進行模糊匹配
        # 提取原始分類中的關鍵字
        import re

        # 提取【...】中的內容
        category_match = re.search(r'【(.*?)】', raw_category)
        if category_match:
            main_category = category_match.group(1)

            # 在 L1 中尋找包含此類別的行
            matching_rows = subject_df[subject_df["L1"].str.contains(main_category, na=False, case=False)]

            if not matching_rows.empty:
                # 返回第一個匹配的 L1, L2, L3
                row = matching_rows.iloc[0]
                return row["L1"], row["L2"], row["L3"]

        return "", "", ""

    def get_difficulty(self, year: str, number: int) -> Optional[float]:
        """
        獲取題目的難度分數

        Args:
            year: 年度
            number: 題號

        Returns:
            難度分數，如果找不到則返回 None
        """
        if year not in self.difficulty_data:
            return None

        return self.difficulty_data[year].get(number)

    def enrich_questions(self, questions: List[Question]) -> List[Question]:
        """
        豐富題目資料，添加知識樹和難度資訊

        Args:
            questions: 題目列表

        Returns:
            豐富後的題目列表
        """
        for question in questions:
            # 獲取難度分數
            difficulty = self.get_difficulty(question.year, question.number)
            if difficulty is not None:
                question.difficulty = float(difficulty)

            # 如果題目沒有 L1, L2, L3，嘗試從知識樹查找
            if not question.level_1 and not question.level_2 and not question.level_3:
                level_1, level_2, level_3 = self.find_knowledge(
                    question.subject_category, question.raw_category
                )
                if level_1:
                    question.level_1 = level_1
                    question.level_2 = level_2
                    question.level_3 = level_3

        return questions

    def export_to_excel(self, questions: List[Question], output_path: str):
        """
        將題目匯出為 Excel

        Args:
            questions: 題目列表
            output_path: 輸出檔案路徑
        """
        # 轉換為字典列表
        data = [question.to_dict() for question in questions]

        # 建立 DataFrame
        df = pd.DataFrame(data)

        # 確保欄位順序正確
        columns = [
            "subject_category", "year", "number", "level_1", "level_2", "level_3",
            "question_stem", "option_a", "option_b", "option_c", "option_d",
            "answer", "explanation", "explanation_a", "explanation_b", "explanation_c", "explanation_d",
            "difficulty", "question_type", "category"
        ]

        # 重新排列欄位
        df = df[[col for col in columns if col in df.columns]]

        # 匯出 Excel
        df.to_excel(output_path, index=False)

        print(f"已匯出 {len(questions)} 題到 {output_path}")

    def export_to_csv(self, questions: List[Question], output_path: str):
        """
        將題目匯出為 CSV

        Args:
            questions: 題目列表
            output_path: 輸出檔案路徑
        """
        # 轉換為字典列表
        data = [question.to_dict() for question in questions]

        # 建立 DataFrame
        df = pd.DataFrame(data)

        # 確保欄位順序正確
        columns = [
            "subject_category", "year", "number", "level_1", "level_2", "level_3",
            "question_stem", "option_a", "option_b", "option_c", "option_d",
            "answer", "explanation", "explanation_a", "explanation_b", "explanation_c", "explanation_d",
            "difficulty", "question_type", "category"
        ]

        # 重新排列欄位
        df = df[[col for col in columns if col in df.columns]]

        # 匯出 CSV（使用 UTF-8 with BOM 以確保 Excel 正確顯示中文）
        df.to_csv(output_path, index=False, encoding="utf-8-sig")

        print(f"已匯出 {len(questions)} 題到 {output_path}")
