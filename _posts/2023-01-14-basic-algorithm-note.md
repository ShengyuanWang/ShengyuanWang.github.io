---
layout: post
title: "Basic Algorithm Note"
subtitle: "Personal Reflection From COMP221@MAC"
date: 2023-01-14
author: "SWang"
header-img: "img/post-bg-2015.jpg"
tags: [Algorithm]
---

## QuickSort

```cpp
void quick_sort(int q[], int l, int r)
{
	if (l >= r) return;
//第一步：分成子问题
	int i = l - 1, j = r + 1, x = q[l + r >> 1];
	while (i < j) {
		do i ++; while (q[i] < x);
		do j ++; while (q[j] > x);
		if (i < j) swap(q[i], q[j]);
	}
//第二步：递归处理子问题
	quick_sort(q, l, j), quick_sort(q, j + 1, r);
//第三步：子问题合并.快排这一步不需要操作，但归并排序的核心在这一步骤
}
```

## MergeSort

```cpp
void merge_sort(int q[], int l, int r)
{
    //递归终止的情况
    if (l >= r) return;

    //分成子问题
    int mid = l + r >> 1;

    //处理子问题
    merge_sort(q, l, mid);
    merge_sort(q, mid+1, r);

    //合并子问题
    int k = 0, i = l, j = mid + 1, tmp[r - l + 1];
    while (i <= mid && j <= r)
    {
        if (q[i] <= q[j]) tmp[k++] = q[i++];
        else tmp[k++] = q[j++];
    }
    while (i <= mid) tmp[k++] = q[i++];
    while (j <= r) tmp[k++] = q[r++];
    for (k = 0, i = l; i <= r; k++, i++) q[i] = tmp[k];
}

```

> 边界分析，为什么不用 mid-1 作为分界线呢， 即 merge_sort(q, l, mid-1), merge_sort(q, mid, r). 因为 mid=l+r>>1 是乡下去争，mid 可能取到 l 造成无限划分

## 整数二分算法

`寻找右分界点`

```cpp
int bsearch_1(int l, int r)
{
    // 第二步递归子问题,用while loop实现
    while (l < r)
    {
        // 第一步：分解成子问题
        int mid = l + r >> 1;
        if (check(mid)) r = mid;  // 向左边找， if判断mid是否满足性质， 注意该性质会划分数组的右边部分
        else l = mid + 1; // 向右边找
    }
    return l; //l就是寻找的右分界点，如果数组中没有要找的点， l==r， 但是这种情况是错误的
}
```

> 边界分析
> 问题： 为什么 mid 是向下取整得到的 `mid=l + r >> 1` 而不是 `mid = l + r + 1 >> 1`
> 答案： mid 向下取整是为了缩小范围，避免无限划分
> 证明：
> 对于 r = mid = l + r >> 1 向下取整一定小于原来的 r
> 对于 l = mid + 1 一定大于原来的 l
> 所有 mid 向下取整的话就不会造成无限划分

`寻找左分界点`

```cpp
int bsearch_2(int l, int r)
{
    while (l < r)
    {
        int mid = l + r + 1 >> 1; //mid向上取整
        if (check(mid)) l = mid;
        else r = mid - 1;
    }
    return l;
}
```

`浮点数二分`

`右分界点`

```cpp
double bsearch_3(double l, double r)
{
    while (r - l > 精度)
    {
        double mid = (l + r) / 2;
        if (check(mid)) r = mid;
        else l = mid;
    }
    return l;

}
```

`左分界点`

```cpp
double bsearch(double l, double r)
{
    while (r - l > 精度)
    {
        double mid = (l + r) / 2;
        if (check(mid)) l = mid;
        else r = mid;
    }
}
```

## 高精度加减乘除法

`高精度加法`

```cpp
vector<int> add(vector<int> &A, vector<int> &B)
{
    if (A.size() < B.size()) return add(B, A);
    vector<int> C;
    int t = 0;
    for (int i = 0; i < A.size(); i++)
    {
        t += A[i];
        if (i < B.size()) t += B[i];
        C.push_back(t % 10);
        t /= 10;
    }
    if (t) C.push_back(t);
    return C;
}
```

`高精度减法`

```cpp
vector<int> sub(vector<int> &A, vector<int> &B)
{
    vector<int> C;
    for (int i = 0, t = 0; i < A.size(); i++)
    {
        t = A[i] - t;
        if (i < B.size()) t -= B[i];
        C.push_back((t + 10) % 10);
        if (t < 0) t = 1;
        else t = 0;
    }
    while (C.size() > 1 && C.back()==0) C.pop_back();
    return C;
}
```

`高精度乘法`

```cpp
vector<int> mul(vector<int> &A, int b)
{
    vector<int> C;
    int t = 0;
    for (int i = 0; i < A.size() || t; i ++)
    {
        if (i < A.size()) t += A[i] * b;
        C.push_back(t % 10);
        t /= 10;
    }
    while (C.size() > 1 && C.back() == 0) C.pop_back();
    return C;
}
```

`高精度除法`

```cpp
vector<int> div(vector<int> &A, int b, int &r)
{
    vector<int> C;
    r = 0;
    for (int i = A.size() - 1; i >= 0; i -- )
    {
        r = r * 10 + A[i];
        C.push_back(r / b);
        r %= b;
    }
    reverse(C.begin(), C.end());
    while (C.size() > 1 && C.back() == 0) C.pop_back();
    return C;
}
```
