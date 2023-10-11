import random
import numpy as np
import matplotlib.pyplot as plt
# 赤玉と白玉が混じった袋の中から復元抽出試行を繰り返して、赤玉と白玉の比率を推定する。

a = 1
b = 2
theta = np.random.beta(a,  b) # 赤玉の比率をBeta(a=1,b=2)でサンプルする。(答えは未知)。ベータ分布にするのは、事後分布を解析的に求めるのに都合がいいから。

for sample_num in [10, 100, 1000]: # サンプルを10, 100, 1000で試してみる
    sample = np.random.choice([0, 1], size=sample_num, p=[1-theta, theta]) # 確率thetaで赤玉、確率1-thetaで白玉を得る試行をサンプル回数繰り返す
    
    # P(\theta | X) を知りたい
    # ベイズの定理から、
    # P(\theta | X) = P(X| \theta) p(\theta) / P(X) = Π_i P(x_i|\theta) p(theta) / P(X)
    # = Π_i P(x_i|\theta) p(theta) (分母は無視)
    # 両辺対数をとると、
    # ln P(\theta | X ) = (Σ_i ln P(x_i | \theta) ) + ln P(theta)
    # P(x_i | \theta) はベルヌーイ分布、P(theta)はベータ分布なので
    # 右辺 = (Σ_i x_i ln \theta  + (1-x_i) ln (1-\theta) ) + (a-1) ln \theta + (b-1) ln (1-\theta) + const (constは\thetaに関係ない部分)
    # = (Σ x_i +a -1) ln \theta  + (N - Σ x_i +b -1) ln (1-\theta)
    # グッと、両辺を見比べてみると、右辺はＢeta(Σ x_i +a, N - Σ x_i +b)になっている！！
    a_prime = sum(sample) + a # 事後分布のパラメータa'
    b_prime = sample_num - sum(sample) + b # 事後分布のパラメータb'
    
    # 以下、可視化用
    view_sample = np.random.beta(a_prime, b_prime, 10000)
    plt.hist(view_sample, bins=100,density=True)
    plt.title(f'ans:{theta}')
    plt.xlim(0,1)
    plt.savefig(f'./../view/parameter_estimate/{sample_num}.png')
    plt.close()
    
    