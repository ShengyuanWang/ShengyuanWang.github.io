# 刷题记录

##  Codeforce

### 4A

#### Watermelon

题目内容： 把一个整数分成两个相同的正整数，并使这两个正整数都是二的倍数

分析： 既然分成两个正整数且都是二的倍数那么这个一定是 num = 2(a+b)   (a, b > 0)

代码：

C++

```c++
#include <bits/stdc++.h>
using namespace std;

void solve() {
    int a;
    cin >> a;
    if (a == 2) {
        cout << "NO" << endl;
        return;
    }
    if (a % 2 == 0) {
        cout << "YES" << endl;
        return;
    } else {
        cout << "NO" << endl;
        return;
    }
}

int main() {
    solve();
}
```



Python3

```python
n = int(input())
def solve(n):
    if n == 2:
        print("NO")
        return
    if n % 2 == 0:
        print("YES")
        return
    print("NO")

solve(n)
```



Java

```java
import java.util.*;


class A_Watermelon{
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        solve(n);

    }

    static void solve(int n) {
        if (n == 2) {
            System.out.println("NO");
            return;
        }
        if (n % 2 == 0) {
            System.out.println("YES");
            return;
        } else {
            System.out.println("NO");
            return;
        }

    }
}
```

