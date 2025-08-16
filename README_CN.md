# 🧾 Red Cross Certificate Printing Agent

🌐 **多语言支持 / Multi-language Support**  
[English](README_EN.md) | [中文](README.md)

这是一个用于批量打印美国红十字会（Red Cross）培训证书的自动化系统。程序可自动识别最新的 Excel 学员名单文件，批量搜索证书并完成筛选、勾选和下载操作，适合 Enrollware / Red Cross 平台配合使用。

## 👨‍💻 作者信息

**Boyi Wang（王博一）**  
📞 电话：3148572744  
📧 邮箱：1084693481@qq.com  
---

## ✅ 功能亮点

### 证书打印阶段
- 📂 自动识别当前文件夹中**最新的 Excel 表格**
- 📧 依据 `First Name` 排序批量处理学员邮箱
- 🧠 智能筛选符合以下条件的证书：
  - 状态必须为 `Valid`
  - 完成时间必须为 **2025年及以后**
  - 课程名称不包含 `online`
- 📥 自动勾选 + 尺寸选择（11'' x 8.5''）+ 点击下载
- ⏯ 支持断点续打（中断后可继续）
- ❌ 打印失败记录将自动导出为 `failed_certificates.xlsx`



---

## 🗂 项目结构说明

redcross_agent/
├── print_certificates.py # 证书打印主程序
├── filter_successful.py # 生成成功打印名单
├── 任意命名的学员表格.xlsx # 每周更新（程序将自动选取最新文件）
├── printed_emails.txt # 自动生成：已成功打印邮箱
├── failed_certificates.xlsx # 自动生成：未成功打印的邮箱名单
├── successful_certificates.xlsx # 自动生成：成功打印的学员名单
├── .gitignore # Git 忽略上传的缓存文件
├── README.md # 项目说明文件（当前）

---

## 🚀 完整使用流程

### 🧰 环境准备

1. 安装 Python：https://www.python.org/
2. 安装依赖：
```bash
pip install -r requirements.txt
```
3. 下载 ChromeDriver
放入本地路径，并修改代码中：
```python
chrome_driver_path = r"C:\路径\chromedriver.exe"
```

### 📝 证书打印阶段

1. 将本周的学员 Excel 表格放入项目文件夹
2. 确保该 Excel 文件是"最后修改"的（或只留当前文件在目录中）
3. 打开终端，运行证书打印程序：
```bash
python print_certificates.py
```
4. 程序将自动：
   - 识别最新 Excel
   - 按 First Name 顺序处理
   - 批量执行证书打印
   - 生成失败名单（failed_certificates.xlsx）
5. 可随时按 Ctrl + C 中断，系统将保存当前进度并跳过已完成邮箱

### 📊 成功名单生成

1. 运行成功名单生成程序：
```bash
python filter_successful.py
```
2. 程序将自动：
   - 读取最新的 Excel 文件
   - 对比失败名单
   - 生成成功打印学员名单（successful_certificates.xlsx）

### ♻️ 重置说明

如果你想开始打印新的表格（而不是接着上次失败名单）：

1. 删除或重命名以下文件：
   - printed_emails.txt（删除或重命名为历史记录）
   - failed_certificates.xlsx（可选）
   - successful_certificates.xlsx（可选）

2. 替换新表格并重新运行程序即可完成"重置打印"

### 🧯 文件说明

- ✅ printed_emails.txt：所有成功处理过的邮箱（系统自动跳过）
- ❌ failed_certificates.xlsx：未能成功打印的学员（可再次运行处理）
- ✅ successful_certificates.xlsx：成功打印的学员名单

---

由 Boyi Wang 开发，用于 Gosvea Inc. 实习项目，提升 Red Cross 证书打印流程自动化效率。

---





