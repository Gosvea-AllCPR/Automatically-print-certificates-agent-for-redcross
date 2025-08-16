import pandas as pd
import os

# === 获取最新的 Excel 文件 ===
excel_files = [f for f in os.listdir() if f.endswith(".xlsx") and not f.startswith("~") and "failed" not in f and "successful" not in f]
if not excel_files:
    print("❌ 未找到任何可用的 Excel 文件，请将学员名单放在当前文件夹并确保为 .xlsx 格式。")
    exit()

original_file = max(excel_files, key=os.path.getmtime)
print(f"📥 当前使用的 Excel 文件：{original_file}")

failed_file = "failed_certificates.xlsx"
output_file = "successful_certificates.xlsx"

# === 读取数据 ===
df_original = pd.read_excel(original_file)
df_failed = pd.read_excel(failed_file)

# === 提取失败邮箱列表 ===
failed_emails = df_failed["Email"].dropna().tolist()

# === 过滤成功的学员 ===
df_success = df_original[~df_original["Email"].isin(failed_emails)]

# === 导出成功名单 ===
df_success.to_excel(output_file, index=False)
print(f"✅ 已成功导出 {len(df_success)} 位已完成打印的学员到：{output_file}")
