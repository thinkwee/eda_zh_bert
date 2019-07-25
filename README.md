# 介绍
-   原仓库[eda_nlp](https://github.com/jasonwei20/eda_nlp)，原论文[EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks](https://arxiv.org/abs/1901.11196)
-   改成了支持中文，并且默认处理成用于BERT模型输入格式，即句子对，可见样例```/data/original.csv```
-   用于增强数据，包含了同义词替换、随机插入、随机删除、打乱顺序，至少用在BERT+分类任务上是可行的。其他模型和任务未测试

# 依赖
-   synonyms
-   pandas
-   请手动安装

# 输入输出样例
-   见```./data/```

# 运行
-   ```./run_augment.sh```

