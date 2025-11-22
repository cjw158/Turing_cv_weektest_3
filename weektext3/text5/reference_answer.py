"""
题目5参考答案：Pandas 数据分析基础
创建 DataFrame、数据操作、统计分析和可视化
"""

import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 1. 创建 DataFrame
data = {
    '姓名': ['张三', '李四', '王五', '赵六', '孙七'],
    '数学': [85, 92, 78, 95, 88],
    '英语': [90, 85, 82, 88, 95],
    'Python': [88, 90, 85, 92, 87]
}

df = pd.DataFrame(data)

# 2. 打印原始 DataFrame
print("=== 1-2. 学生成绩表 ===")
print(df)
print()

# 3. 计算总分和平均分
df['总分'] = df['数学'] + df['英语'] + df['Python']
df['平均分'] = df['总分'] / 3

print("=== 3. 添加总分和平均分后 ===")
print(df)
print()

# 4. 数据统计
print("=== 4. 数据统计 ===")

# 每门课程的平均分
print("各科平均分：")
print(f"数学平均分: {df['数学'].mean():.2f}")
print(f"英语平均分: {df['英语'].mean():.2f}")
print(f"Python平均分: {df['Python'].mean():.2f}")
print()

# 总分最高的学生
max_score_idx = df['总分'].idxmax()
best_student = df.loc[max_score_idx]
print("总分最高的学生：")
print(best_student)
print()

# 平均分最低的学生
min_avg_idx = df['平均分'].idxmin()
lowest_avg_student = df.loc[min_avg_idx]
print("平均分最低的学生：")
print(lowest_avg_student)
print()

# 5. 绘制条形图
plt.figure(figsize=(10, 6))

# 绘制条形图
bars = plt.bar(df['姓名'], df['总分'], color='skyblue', edgecolor='navy', alpha=0.7)

# 在柱子上添加数值标签
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}',
             ha='center', va='bottom', fontsize=12)

# 添加标题和标签
plt.title('学生总分对比', fontsize=16, fontweight='bold')
plt.xlabel('学生姓名', fontsize=14)
plt.ylabel('总分', fontsize=14)

# 添加网格
plt.grid(True, axis='y', linestyle='--', alpha=0.5)

# 调整布局
plt.tight_layout()

# 保存图像
output_file = 'scores_chart.png'
plt.savefig(output_file, dpi=200, bbox_inches='tight')
print(f"条形图已保存为 {output_file}")

plt.close()

# 额外统计信息
print("\n=== 额外统计信息 ===")
print(f"班级总分平均: {df['总分'].mean():.2f}")
print(f"班级平均分平均: {df['平均分'].mean():.2f}")
print(f"总分标准差: {df['总分'].std():.2f}")

print("\n任务完成！")
