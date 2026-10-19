# tdist-random

平均・分散・自由度・個数を指定して、t分布に従う乱数を返すシンプルなライブラリ（標準ライブラリのみ）。

## インストール

```
python -m pip install "git+https://github.com/sanrokurintaro/tdist-random.git"
```

## 使い方

```python
from tdist_random import t_random

xs = t_random(mean=10, variance=4, df=5, n=1000, seed=42)
```

- `mean` : 平均
- `variance` : 分散（分布そのものの分散。内部で `scale = sqrt(variance*(df-2)/df)` に変換）
- `df` : 自由度（t値のパラメータ）。分散が有限になるよう `df > 2` が必要
- `n` : 出力個数
- `seed` : 省略可（再現用）

## テスト

```
pip install pytest
pytest
```
