# HandsOn-Data-Analysis-and-ML

Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, you will use data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.


## Day:1

In this project, Students will make use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. You will write code to import the data and answer interesting questions about it by computing descriptive statistics. They will also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics. Technologies that will be covered are Numpy, Pandas, Matplotlib, Seaborn, Jupyter notebook. We will be giving the students a deep dive into the Data Analytical process


## Day:2

We will be giving the students an insight into one of the major fields of Machine Learning ie. Time Series forcasting we will be taking them through the relevant theory and make them understand of the importance and different techniques that are available to deal with it. After that we will be working hands on the bike share data set implementing different algorithms and understanding them to the core



> We aim to provide students an insight into what exactly is the job of a data analyst and get them familiarise to how does the entire data analysis process work.

The session will be hosted by Shaurya Sinha a data analyst at Jio and Parag Mittal Software engineer at Microsoft.

# 可重复性研究作业 - 共享单车数据分析项目复现
课程：D2RS-2026spring 可重复性研究
成员：祝佳琦 2025303110127

---

## 一、项目目标
本项目基于公开共享单车使用数据集，结合时间、气象等特征，完成从数据预处理、分析可视化到建模预测的完整流程，并验证项目的可复现性。
原项目来源：https://github.com/Devtown-India/HandsOn-Data-Analysis-and-ML

---

## 二、数据预处理
### 1. 数据源说明
- 数据集：`hour.csv`
- 内容：包含17379条记录，17个字段，记录了美国共享单车系统每小时的租赁数据，包含时间、季节、天气、温度、湿度、风速及租赁量等信息。
- 完整性：无缺失值，无需额外清洗。

### 2. 预处理步骤
1.  数据加载：使用`pandas`读取CSV文件，转换为DataFrame格式
2.  特征工程：
    - 将时间特征（年、月、日、小时）拆分，提取工作日/周末、高峰时段等信息
    - 对分类特征（季节、天气状况）进行编码，便于后续分析
3.  数据划分：将数据集划分为训练集和测试集，用于模型训练与验证

---

## 三、数据分析与可视化
通过`matplotlib`和`seaborn`完成了以下分析：
1.  **时间特征分析**：工作日早8点、晚17-18点为租赁高峰，周末租赁量更平缓，无明显高峰
2.  **气象特征分析**：温度与租赁量呈正相关，湿度、风速与租赁量呈负相关，舒适的天气更能促进骑行需求
3.  **相关性分析**：温度、体感温度与租赁量的相关性最高，天气状况的影响次之

---

## 四、模型与结果解读
### 1. 模型选择
采用线性回归模型，以时间、气象特征为自变量，以租赁量为因变量进行预测。

### 2. 模型结果
- 模型评估指标：R²≈0.25
- 结果解读：模型能捕捉到主要影响因素，但受限于线性模型的简单性，预测精度有限，说明共享单车租赁量受多种非线性因素影响，后续可尝试更复杂的模型优化。

---

## 五、可复现性说明
### 1. 环境配置
- Python版本：3.10+
- 依赖包：`pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`
- 依赖配置文件：`requirements.txt`

### 2. 运行步骤
1.  安装依赖：`pip install -r requirements.txt`
2.  运行验证脚本：`python test_env.py`，验证环境与数据加载
3.  打开`BIKE_SHARE_WORKBOOK.ipynb`，按顺序运行所有代码块，即可复现分析过程与结果

---

## 六、项目文件结构
