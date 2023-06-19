---
title : "[Algorithm] Algorithm Complexity"
categories:
- Algorithm
tags:
- c++
- algorithm
---

- input size가 아주 커질 때 가정(n→ $\infin$)
- notation
    - $O$ : Upper Bound, Worst Case
        
        O(g(n)) = {f(n) | 모든 n > $n_0$에서 **0 ≤ f(c) ≤ cg(n)**를 만족하는 positive constant인 $n_0$와 c가 존재}
        
    - $\Omega$ : Lower Bound, Best Case
        
        O(g(n)) = {f(n) | 모든 n > $n_0$에서 **0 ≤ cg(n) ≤ f(c)** 를 만족하는 positive constant인 $n_0$와 c가 존재}
        
    - $\theta$ : Upper Bound & Lower Bound,
        
        O(g(n)) = {f(n) | 모든 n > $n_0$에서 **0 ≤** $c_1$**g(n) ≤ f(c) ≤**  $c_2$**g(n)**를 만족하는 positive constant인 $n_0$와 c가 존재}
        

![Untitled](../../assets/images/2023-04-25-algorithm-complexity/Untitled.png)

- 특징
    
    ![Untitled](../../assets/images/2023-04-25-algorithm-complexity/Untitled%201.png)
    
- comparing
    
    ![Untitled](../../assets/images/2023-04-25-algorithm-complexity/Untitled%202.png)
    

- 예시
    - Insertion Sort
        
        ![Untitled](../../assets/images/2023-04-25-algorithm-complexity/Untitled%203.png)
        
        - complexity
            - best case : $O(n)$
            - worst case : $O(n^2)$