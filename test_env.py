# -*- coding: utf-8 -*-
import os
import pandas as pd
import re

# ===================== 固定配置 =====================
ROOT_DIR = r"D:\2018王昊组\原始数据\中国地面气候资料日值数据集(V3.0)"
# 改为CSV格式，无行数限制！
OUTPUT_FILE = r"D:\2018王昊组\气象数据整合表.csv"

# 最终输出列顺序（严格按你的要求）
OUTPUT_COLS = [
    "站点", "年", "月", "日",
    "平均气压", "平均风速", "平均气温", "最高气温", "最低气温",
    "相对湿度", "降水", "小型蒸发", "大型蒸发", "日照时数"
]

all_data = []

# ===================== 解析单个TXT文件 =====================
def parse_txt(file_path):
    try:
        # 读取空格分隔的文本文件
        df = pd.read_csv(file_path, sep=r"\s+", header=None, dtype=str)
        if len(df) == 0:
            return

        # 从文件名提取要素类型
        filename = os.path.basename(file_path)
        match = re.search(r'-([A-Z]+)-', filename)
        if not match:
            return
        elem = match.group(1)

        # 固定基础列：站点、年、月、日
        base = df[[0, 4, 5, 6]].copy()
        base.columns = ["站点", "年", "月", "日"]

        # ===================== 按要素解析 =====================
        if elem == "PRS":
            base["平均气压"] = df[7]
        elif elem == "WIN":
            base["平均风速"] = df[7]
        elif elem == "TEM":
            base[["平均气温", "最高气温", "最低气温"]] = df[[7, 8, 9]]
        elif elem == "RHU":
            base["相对湿度"] = df[7]
        elif elem == "PRE":
            pre_cols = df[[7, 8, 9]].astype(float)
            pre_cols = pre_cols.replace([32700, 32766], 0)
            base["降水"] = pre_cols.sum(axis=1)
        elif elem == "EVP":
            base[["小型蒸发", "大型蒸发"]] = df[[7, 8]]
        elif elem == "SSD":
            base["日照时数"] = df[7]

        all_data.append(base)
        print(f"✅ 解析成功：{filename}")
    except Exception as e:
        print(f"❌ 解析失败：{file_path}")

# ===================== 遍历所有年份文件夹 =====================
def traverse_data():
    print("="*60)
    print(f"📂 根目录：{ROOT_DIR}")
    print("="*60)

    if not os.path.exists(ROOT_DIR):
        print("❌ 根目录不存在！")
        return

    for folder_name in os.listdir(ROOT_DIR):
        folder_path = os.path.join(ROOT_DIR, folder_name)
        if not os.path.isdir(folder_path):
            continue
        if not re.match(r'\d{4}年逐日数据', folder_name):
            continue

        print(f"\n📁 处理：{folder_name}")
        for file_name in os.listdir(folder_path):
            if file_name.lower().endswith(".txt"):
                file_path = os.path.join(folder_path, file_name)
                parse_txt(file_path)

# ===================== 合并数据 + 导出CSV（无行数限制） =====================
def merge_and_export():
    if not all_data:
        print("\n❌ 未读取到任何数据！")
        return

    print("\n正在合并数据...")
    df_merge = pd.concat(all_data, ignore_index=True)
    df_final = df_merge.groupby(["站点", "年", "月", "日"], as_index=False).first()
    df_final = df_final.reindex(columns=OUTPUT_COLS)

    # 导出CSV，支持超大数据量
    df_final.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")
    print(f"\n🎉 导出完成！文件保存在：\n{OUTPUT_FILE}")
    print(f"📊 总数据行数：{len(df_final)}")

# ===================== 运行主程序 =====================
if __name__ == "__main__":
    traverse_data()
    merge_and_export()