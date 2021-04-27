# BTM-VN-Algorithm
## BTM_VN重要代码以及基本实验方法介绍
### 数据预处理
btm_vn/data/data_util.py与/data/word_divide.py文件实现文档分词功能。</br>
btm_vn/data/data_file_save.py文件中包含文件预处理方法，三个方法分别可生成服务描述的序号分词结果txt，词对相似度矩阵txt，服务描述分词结果txt。</br>
btm_vn/data/data_file_load.py文件读取分词文档与词对相似度信息。</br>

### 聚类方法
btm_vn/cluster/kmeans.py 实现优化DPC与普通算法。</br>

### 模型实现
btm_vn/model/biterm.py定义词对结构。
btm_vn/model/btm_wvf_Adapter.py实现模型数据结构与训练过程。
btm_vn/model/word2vecAdapter.py实现词向量相关操作。

### 聚类准确度指标
btm_vn/judge/clustereffect.py实现五种聚类准确度评价指标
btm_vn/judge/model_effect.py实现pmi等主题模型质量评价指标

### 使用介绍
模型训练：/model/btm_wvf_Adapter.py中实现了一个main方法，修改其中参数即可进行训练，训练结果生成txt文件。</br>
实验：/test/biterm_select_test.py中实现词对筛选展示实验，对应论文5.3节。</br>
/test/topic_word_test.py中实现主题一致性实验，对应论文5.5节。</br>

### 主要对比算法或模型实现
TF-IDF+Word2vec: ServiceCluster/cluster/tf_idf_w2v_kmeans.py
LDA: ServiceCluster/cluster/lda_gibbs.py
LDA+Word2vec: ServiceCluster/cluster/lda_expand_kmeans.py
BTM: ServiceCluster/model/btmAdapter.py
DMM：采用[https://github.com/datquocnguyen/jLDADMM](https://github.com/datquocnguyen/jLDADMM)的DMM实现
