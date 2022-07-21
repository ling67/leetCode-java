快速选择原理如下，选择第k大的数字：

我们在快速选择的时候，也同样用了划分的思想，随机选择一个中轴，双指针i, j，指针i从左往右扫描，指针j从右往左扫描，如果i < j 则进行交换，并且继续循环，直到遇到中轴，这时候我们的i和j均为中轴（理由：因为i，j相等），如果数字在中轴的左边，则向左递归，如果数字在中轴的右边则向右递归。

分析复杂度分析，刚开始的一个循环找中轴，用掉了n次，第二次循环只能找左边的中轴或者右边的中轴，用了n/2次，无限循环下去，直到极限，表达式如下

𝑛+𝑛/2+𝑛/4+𝑛/8...令𝑆𝑛=𝑛+𝑛/2+𝑛/4+𝑛/8...则1/2∗𝑆𝑛=𝑛/2+𝑛/4+𝑛/8...上述两式子相减得到1/2∗𝑆𝑛=𝑛,则𝑆𝑛=2𝑛
时间复杂度推导出T(2n)，结果为O(n)的复杂度。

Refer: https://www.acwing.com/blog/content/8597/

```python
int quick_select(int *q, int l, int r, int k) {
    if (l == r) return q[l];
    int i = l - 1, j = r + 1, x = q[l + r >> 1];
    while (i < j) {
        do i++ ; while (q[i] < x);
        do j-- ; while (q[j] > x);
        if (i < j) swap(q[i], q[j]);
    }
    if (k <= j - l + 1) return quick_select(q, l, j, k);
    return quick_select(q, j + 1, r, k - (j - l + 1));
}
```