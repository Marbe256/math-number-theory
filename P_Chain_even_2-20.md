# 多項式差分の逆連鎖分割公式集 (c=2 ～ c=20)

本資料は、偶数次の非対称核 $P(c)$（$c$ は偶数）を奇数次の基底 $P(2m+1)$ に集約した公式集である。

### 定義
- $W = k(n-k)$
- $P(c) = k^c + (n-k)^c$
- $S_{0,j} = \sum_{k=1}^{n-1} k^{a+j} (n-k)^{a} = \frac12\sum_{k=1}^{n-1} W^a P(j)$
- 境界関係式: $\frac{n}{2} P(0) = P(1)$

### 一般式
$c\ge0$ を偶数とすると、

$$\frac{n}{2} P(c) = \sum_{m=0}^{c/2} R_{2m+1}\, n^{c-2m}\, P(2m+1),\qquad R_{2m+1} = \frac{1}{c+1}\binom{c+1}{2m+1} B_{c-2m}$$

が成り立つ（$B_h$ はベルヌーイ数）。両辺に $W^a$ を掛けて $k$ について和を取ると、$n S_{0,c} = \sum_{m=0}^{c/2} 2R_{2m+1}\, n^{c-2m}\, S_{0,2m+1}$ となる。

---

### 第 2 階層 (c=2)
$$\frac{n}{2} P(2) = \frac{1}{3} P(3) + \frac{1}{6}n^2 P(1) \quad \dots (1)$$

### 第 4 階層 (c=4)
$$\frac{n}{2} P(4) = \frac{1}{5} P(5) + \frac{1}{3}n^2 P(3) - \frac{1}{30}n^4 P(1) \quad \dots (2)$$

### 第 6 階層 (c=6)
$$\frac{n}{2} P(6) = \frac{1}{7} P(7) + \frac{1}{2}n^2 P(5) - \frac{1}{6}n^4 P(3) + \frac{1}{42}n^6 P(1) \quad \dots (3)$$

### 第 8 階層 (c=8)
$$\frac{n}{2} P(8) = \frac{1}{9} P(9) + \frac{2}{3}n^2 P(7) - \frac{7}{15}n^4 P(5) + \frac{2}{9}n^6 P(3) - \frac{1}{30}n^8 P(1) \quad \dots (4)$$

### 第 10 階層 (c=10)
$$\begin{aligned}
\frac{n}{2} P(10) = & \frac{1}{11} P(11) + \frac{5}{6}n^2 P(9) - n^4 P(7) + n^6 P(5) - \frac{1}{2}n^8 P(3) \\\\
&+ \frac{5}{66}n^{10} P(1) \quad \dots (5)
\end{aligned}$$

### 第 12 階層 (c=12)
$$\begin{aligned}
\frac{n}{2} P(12) = & \frac{1}{13} P(13) + n^2 P(11) - \frac{11}{6}n^4 P(9) + \frac{22}{7}n^6 P(7) - \frac{33}{10}n^8 P(5) \\\\
&+ \frac{5}{3}n^{10} P(3) - \frac{691}{2730}n^{12} P(1) \quad \dots (6)
\end{aligned}$$

### 第 14 階層 (c=14)
$$\begin{aligned}
\frac{n}{2} P(14) = & \frac{1}{15} P(15) + \frac{7}{6}n^2 P(13) - \frac{91}{30}n^4 P(11) + \frac{143}{18}n^6 P(9) - \frac{143}{10}n^8 P(7) \\\\
&+ \frac{91}{6}n^{10} P(5) - \frac{691}{90}n^{12} P(3) + \frac{7}{6}n^{14} P(1) \quad \dots (7)
\end{aligned}$$

### 第 16 階層 (c=16)
$$\begin{aligned}
\frac{n}{2} P(16) = & \frac{1}{17} P(17) + \frac{4}{3}n^2 P(15) - \frac{14}{3}n^4 P(13) + \frac{52}{3}n^6 P(11) - \frac{143}{3}n^8 P(9) \\\\
&+ \frac{260}{3}n^{10} P(7) - \frac{1382}{15}n^{12} P(5) + \frac{140}{3}n^{14} P(3) - \frac{3617}{510}n^{16} P(1) \quad \dots (8)
\end{aligned}$$

### 第 18 階層 (c=18)
$$\begin{aligned}
\frac{n}{2} P(18) = & \frac{1}{19} P(19) + \frac{3}{2}n^2 P(17) - \frac{34}{5}n^4 P(15) + 34n^6 P(13) - \frac{663}{5}n^8 P(11) \\\\
&+ \frac{1105}{3}n^{10} P(9) - \frac{23494}{35}n^{12} P(7) + 714n^{14} P(5) - \frac{3617}{10}n^{16} P(3) + \frac{43867}{798}n^{18} P(1) \quad \dots (9)
\end{aligned}$$

### 第 20 階層 (c=20)
$$\begin{aligned}
\frac{n}{2} P(20) = & \frac{1}{21} P(21) + \frac{5}{3}n^2 P(19) - \frac{19}{2}n^4 P(17) + \frac{1292}{21}n^6 P(15) - 323n^8 P(13) \\\\
&+ \frac{41990}{33}n^{10} P(11) - \frac{223193}{63}n^{12} P(9) + 6460n^{14} P(7) - \frac{68723}{10}n^{16} P(5) + \frac{219335}{63}n^{18} P(3) \\\\
&- \frac{174611}{330}n^{20} P(1) \quad \dots (10)
\end{aligned}$$
