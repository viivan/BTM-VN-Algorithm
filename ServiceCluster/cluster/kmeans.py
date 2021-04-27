# 计划提供两种实现，一种直接第三方库，一种自己写

import numpy as np
from sklearn.cluster import KMeans


def kMeansByFeature(k=3, metrix=[]):
    # 使用kMeans库，将特征矩阵进行聚类处理(如lda分布),参数为对应矩阵信息
    # 构造聚类器
    data = np.array(metrix)
    estimator = KMeans(n_clusters=k)
    estimator = KMeans(n_clusters=k, n_init=1, init="random")
    estimator = estimator.fit(data)
    return estimator