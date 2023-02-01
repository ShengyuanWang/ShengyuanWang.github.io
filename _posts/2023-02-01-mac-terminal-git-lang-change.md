---
layout: post
title: "Mac terminal git Lang Change"
subtitle: "Language change from Chinese to English"
date: 2023-02-01
author: "SWang"
header-img: "img/post-bg-2015.jpg"
tags: [git]
---

## 方法 1

1. 打开终端，输入 `vim ~/.bash_profile` 进入功能模式. 输入`export LC_ALL=en_US.UTF-8`, `:wq`退出

2. `source ~/.bash_profile`

3. 编辑 `.zshrc` 档案

```shell
vim ~/.zshrc
```

找个顺眼的地方插入 `source ~/.bash_profile`
