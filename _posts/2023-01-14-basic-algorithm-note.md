---
layout: post
title: "Basic Algorithm Note"
subtitle: "Personal Reflection From COMP221@MAC"
date: 2023-01-14
author: "SWang"
header-img: "img/post-bg-2015.jpg"
tags: [Algorithm]
---

Select Language：
[Chinese](#1) ｜ [English](#0)

<h1 id="0"></h1>

## QuickSort

```cpp
void quick_sort(int q[], int l, int r)
{
	if (l >= r) return;

// Step 1: Divide the Large Problem into sub problems
	int i = l - 1, j = r + 1, x = q[l + r >> 1];
	while (i < j) {
		do i ++; while (q[i] < x);
		do j ++; while (q[j] > x);
		if (i < j) swap(q[i], q[j]);
	}

// Step 2: use recursion to solve the sub problems
	quick_sort(q, l, j), quick_sort(q, j + 1, r);

// Step 3: merge sub problems
}
```

## MergeSort

```cpp
void merge_sort(int q[], int l, int r)
{
    //The situation we need to stop the recursion
    if (l >= r) return;

    // Divide into sub problems
    int mid = l + r >> 1;

    // Solve sub problems
    merge_sort(q, l, mid);
    merge_sort(q, mid+1, r);

    // Merge sub problems
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

> Boundary Analysis: Why here we use "mid" as boundary instead of "mid - 1", for example, merge_sort(q, l, mid-1), merge_sort(q, mid, r). That's because "mid = l + r >> 1" is floor rounding, if l = mid, the code chunk will run forever.

## Integer Binary Search

`Find Right Boundary`

```cpp
int bsearch_1(int l, int r)
{
    // Step 2: Use while loop to do recursion for sub problems
    while (l < r)
    {
        // Step 1: Divide into sub problems
        int mid = l + r >> 1;
        if (check(mid)) r = mid; // find towards left, if will judge whether mid will meet our expectation, be aware that this property will cancel out the right part of the array.
        else l = mid + 1; // find towards right
    }
    return l; // l is the right boundary we want to find. If the array does not include the integer we want, which will make l == r, and this will be the wrong case.
}
```

> Boundary Analysis
> Q: Why `mid = l + r >> 1` not `mid = l = r + 1 >> 1`?
> A: Because we want to avoid infinitely division
> P:
> for all r = mid = l = r >> 1, floor rounding will smaller that original r.
> for all l = mid + 1, l will be greater than original l
> With floor rounding of mid, we will never have infinity division situation.

`Find Left Boundary`

```cpp
int bsearch_2(int l, int r)
{
    while (l < r)
    {
        int mid = l + r + 1 >> 1; //mid -> ceiling rounding
        if (check(mid)) l = mid;
        else r = mid - 1;
    }
    return l;
}
```

`Float Binary Search`

`Right Boundary Search`

```cpp
double bsearch_3(double l, double r)
{
    while (r - l > Acc)
    {
        double mid = (l + r) / 2;
        if (check(mid)) r = mid;
        else l = mid;
    }
    return l;

}
```

`Left Boundary Search`

```cpp
double bsearch(double l, double r)
{
    while (r - l > Acc)
    {
        double mid = (l + r) / 2;
        if (check(mid)) l = mid;
        else r = mid;
    }
}
```

## High Accuracy Add Sub Mul Div

`Add`

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

`Sub`

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

`Mul`

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

`Div`

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

<h1 id="1"></h1>

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

## 前缀和

Q: 什么事前缀和
A:
原始数组 a[1], a[2], a[3], ... , a[n]
前缀和： Si 为数组前 i 项和， 即 S[i] = a[1] + a[2] + a[3] + ... + a[i]
注意： 前缀和的下标最好从 1 开始，避免进行下标的转换

> s[0] = 0
> s[1] = a[1]
> s[2] = a[1] + a[2]

前缀和的作用
快速求出数组中某段区间的和

一维数组求解前缀和(Si)
1. for 循环求出 每个S[i] (将S[i]定义为0， 避免下标的转换)
2. 求出[l, r]中的和, 即S[r] - S[l-1]

```java
static void main(String[] args)
{
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), m = in.nextInt();
    int[] arr = new int[N];
    for (int i = 1; i <= n; i++)
    {
        arr[i]  =in.nextInt();
    }
    int s[]
}
```