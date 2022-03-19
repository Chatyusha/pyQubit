import numpy as np
import bisect

# 累積和配列生成
def cumulative_sum(sample):
    sum = 0
    cuml = []
    for i in sample:
        sum += i
        cuml.append(sum)
    return np.array(cuml)


# 二分探索で重み付きサンプリング
def weighted_random_samplings_binary_search(sample):
    gen = np.random.Generator(np.random.MT19937())
    at = gen.random()
    return bisect.bisect(cumulative_sum(sample),at)


