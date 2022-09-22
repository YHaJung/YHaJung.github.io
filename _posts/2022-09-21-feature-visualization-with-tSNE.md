---
title : "t-SNE를 이용한 Feature 시각화"
categories:
    - 시각화
tags:
    - 시각화
    - python
---

## t-SNE의 의미

- t-distributed stochastic neighbor embedding
- 비선형적 **차원 숙소**
- **복잡한 데이터의 시각화**가 목적. 높은 차원의 데이터를 2차원 또는 3차원으로 축소시켜 시각화.
- 높은 차원 공간에서 **비슷한 데이터** 구조는 낮은 차원 공간에서 **가깝게 대응**하며, 비슷하지 않은 데이터 구조는 멀리 떨어져 대응
- 예시
    ![image](https://user-images.githubusercontent.com/49065638/191737983-4902804e-ffae-47cc-a2ca-1b8f7c20ee17.png)
    

## t-SNE의 원리

- 원본의 높은 차원에서 정규분포로 유사도를 계산하여 $p_{ij}$ 분포로 나타낸다. $p_{ij}$는 데이터 포인트 $x_i, x_j$의 유사도를 나타낸다.
- 대응하는 낮은 차원의 데이터를 t-분포로 유사도를 계산하여 $q_{ij}$ 분포로 나타낸다.
- $p_{ij}$와 $q_{ij}$ 가 되도록 같은 분포가 되도록 $y_{ij}$를 갱신한다.
    - 유사도가 큰 상태
    의 관계를 재현할 때는 낮은 차원 공간에서 데이터 포인트를 더 가까이
     배치
    - 유사도가 작은 상태의 관계
    를 재현할 때에는 낮은 차원 공간에서 데이터 포인트를 더 멀리 배치
    - 두가지 분포의 `KL divergence`
    를 최소화
- t-분포를 사용
    - 정규분포대신 t-분포 사용
    - 일반적인 정규분포보다 끝단이 두껍기 때문
        <details>
        <summary>t-분포란?</summary>
        <div markdown="1">       

        ![image](https://user-images.githubusercontent.com/49065638/191738148-a08e1c0b-d062-421f-a113-e0f7c250e63c.png)

        - • t-분포는 표준 정규분포와 유사하게 0을 중심으로 좌우 대칭 형태를 이루며 표준 정규분포보다 평평하고 기다른 꼬리 형태를 가집니다. 즉, **양쪽 꼬리 형태가 두터운 형태**를 가집니다. 이와 같은 형태를 가지는 이유는 **표준 정규분포보다 분산이 크기 때문**입니다.
        - 정규분포는 평균과 분산을 통하여 그 형태가 달라지게 됩니다. 반면 t-분포는 ’자유도’
        에 따라 다른 모양을 나타냅니다.
            
            `자유도 = 표본의 수 -1`
            
        - 자유도가 점점 더 커질수록 표준 정규분포에 가까워진다.
            - 30 이하이면 표준정규분포 보다 분산이 커져서 평평한 모양(t 분포 사용)
            - 30이 넘으면 표준 정규분포와 비슷(정규분포 사용)
            - 120 이상이 되면 표준정규분포와 완전히 같아짐(정규분포 사용)

        </div>
        </details>


## python에서 t-SNE 구현법

- sklearn에 구현된 T-SNE를 많이 사용
- 매뉴얼 : [https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html)

### 필수 요소

```python
# 불러오기
from sklearn.manifold import TSNE

# 축소할 자원 설정
n_components = 2

# t-sne 모델 생성
model = TSNE(n_components=n_components)

# 학습한 결과 2차원 공간 값 출력
print(model.fit_transform(data.data))
```

### 예시

```python
import numpy as np
from sklearn.manifold import TSNE

n_components = 2                             # 축소 시 차원
model = TSNE(n_components=n_components)
transformed = model.fit_transform(data_all[[i for i in range(10816)]])  # label 제외하고 입력
```

- 이렇게 추출한 결과를 시각화하고 싶을 땐 아래와 같이 `matplotlib`을 활용할 수 있다.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

xs = transformed[:,0]
ys = transformed[:,1]
scatter = ax.scatter(xs,ys, c=data_all['label'])

legend1 = ax.legend(*scatter.legend_elements(), loc="lower left", title="Classes")
ax.add_artist(legend1)

plt.savefig(save_path+'.png')
plt.close()
```

### 추가 주요 옵션

- `perplexity`
- 데이터 타입 : float
- 기본값 : 30.0
- 의미 : 다른 manifold learning의 nearest neighbors 갯수에 사용되는 값을 뜻합니다. 일반적으로 더 큰 데이터 셋은 보통 더 큰 `perplexity` 값을 필요로 합니다. 이 값을 정할 때, 5 ~ 50 사이의 값을 선택해 보고 더 좋은 결과를 얻기 위해서 값을 변경해 가면서 조정할 필요가 있습니다.

- `early_exaggerattion`
- 데이터 타입 : float
- 기본값 : 12.0
- 의미 : 기존 공간에서 데이터의 클러스터 간 거리가 타겟 공간에서 얼만큼 조밀하거나 먼 지 나타내는 파라미터 입니다. 이 값을 큰 값으로 설정할 경우 기존 공간의 클러스터 사이의 공간이 타겟 공간에서 더 커지도록 학습됩니다. 이 매개 변수의 선택은 크게 중요하지는 않으나 학습 초기에 비용 함수가 증가하면 early_exaggeration 또는 initial learning rate가 너무 높을 수 있으니 이 경우 살펴 보면 됩니다.

- `learning_rate`
- 데이터 타입 : float
- 기본값 : 200.0
- 의미 : 학습을 할 때 사용하는 learning rate 이며 일반적으로 10 ~ 1000 사이의 값을 가집니다. learning rate가 너무 높으면 데이터가 가장 가까운 이웃과 거의 같은 거리에있는 ‘공’처럼 보일 수 있습니다. 반면 learning rate가 너무 낮으면 대부분의 포인트가 특이치가 거의 없는 조밀 한 클라우드에서 압축 된 것처럼 보일 수 있습니다.

- `n_iter`
- 데이터 타입 : int
- 기본값 : 1000
- 의미 : 최적화를 위한 최대 반복 횟수입니다. 이 값은 최소 250 이상이어야 학습하는 데 지장이 없습니다.

- `n_iter_without_progress`
- 데이터 타입 : int
- 기본값 : 300
- 의미 : 성능 개선 없이 학습이 지속되면 학습을 중지하는 옵션이며 카운트는 50의 배수 단위로 카운트 됩니다.

## 참고자료

- [https://gaussian37.github.io/ml-concept-t_sne/](https://gaussian37.github.io/ml-concept-t_sne/)