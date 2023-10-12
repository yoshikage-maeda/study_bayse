# このスクリプトでは、ガウス分布のパラメータをベイズ推定する。
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(79798)
def parameter_estimate_gauss_var_fixed():
    """
    分散既知(l^-1)で平均(mu)未知のとき(都合上分散はl^-1とする。)
    事前分布は平均m、分散l_m^-1 の正規分布とする（うれしいことに、事前分布を正規分布とすると事後分布も正規分布となる！！）
    知りたいのは、p(mu|X)  xを与えられたときのパラメータmに関する事後分布
    p(mu|X) = p(X|mu)p(mu) = Π_i p(x_i|mu) p(mu)
    両辺対数をとると
    ln p(mu|X) = Σ_i ln p(x_i|mu)  + ln p(mu) = Σ_i -l(x_i -mu)^2/2  -l_m (mu - m)^2/2 + const = -1/2{ (Nl + l_m)mu^2 - 2(Σ_i x_i*l + ml_m)mu} + const
    よって、muに関する2次式がでてきた。平方完成することで、事後分布のパラメータ
    l_m' = Nl + l_m
    m' = (l Σ_i x_i + l_m m)/ l_m'
    """
    m = 0 # 事前分布の平均は0
    l_m = 1 # 事前分布の分散は1
    mu = np.random.normal(m, l_m) # 未知の平均パラメータをランダムに決める。
    
    for sample_num in [10, 100, 1000]: # サンプルを10, 100, 1000で試してみる
        l = 1
        sample = np.random.normal(mu, l, size=sample_num) # 既知の分散は1とする.
        l_m_prime = sample_num*l + l_m
        m_prime = (l * sum(sample) + l_m * m) /(l_m_prime)
        # 以下、可視化用
        view_sample = np.random.normal(m_prime, np.sqrt(1/l_m_prime), 10000)
        plt.hist(view_sample, bins=100,density=True)
        plt.title(f'ans:{mu}')
        plt.xlim(-2,2)
        plt.savefig(f'./../view/parameter_estimate_gauss/sigma_fix/{sample_num}.png')
        plt.close()

if __name__ == '__main__':
    parameter_estimate_gauss_var_fixed()
    