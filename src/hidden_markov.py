import pandas as pd
import numpy as np

def load_data(path):
    data = pd.read_csv(path)
    data = data[(data['Store'] == 1) & (data['Dept'] == 1)]
    X = data['Weekly_Sales'].values
    return X

def main():
    X = load_data('./../data/train.csv')
    #　設定
    K = 5 #　クラス数

    # Aのパラメータ
    A_para = np.ones((K, K))/K # 遷移確率を生成するディリクレ分布のハイパパラメータ。わからないので等確率となるようなパラメータとして設定
    # lambdaの事前分布のパラメタ
    a = 1
    b = 1
    # muの事前分布のパラメータ
    m = 1
    beta = 1
    # piの事前分布のパラメータ
    alpha = np.ones(K)/K
    N = len(X)
    #アルゴリズム
    '''
    q(μ,λ), q(π)、q(A)を初期化
    for i in 1:MAXITER:
        for n in 1:N:
            q(s_n)を更新
        for k in 1:K:
            q(μ_k, λ_k)を更新
        q(π)を更新
    '''

    # 潜在変数の近似事後分布の期待値を初期化
    E_s_nk = np.random.uniform(low=0.0, high=11.0, size=(N, K))
    E_s_nk /= np.sum(E_s_nk, axis=1, keepdims=True) # Datanum*K
    # 初期値によるmuの近似事後分布のパラメータを計算
    beta_hat_k = np.sum(E_s_nk, axis=0) + beta # shape is K 正規分布の平均muのパラメータ
    m_hat_k = (np.dot(E_s_nk.T, X) + beta * m) / beta_hat_k # Shape is K　正規分布の平均muのパラメータ
    # 初期値によるlambdaの近似事後分布のパラメータを計算
    a_hat_k = np.sum(E_s_nk, axis=0)/2 + a
    b_hat_k = (np.dot(E_s_nk.T, (X- ))
    sample_num = 100 # サンプル回数
    for _ in range(sample_num):
    # for n in range(N):
    print(1)    

    

if __name__ == '__main__':
    main()