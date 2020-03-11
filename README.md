# Little-Tools

Some simple tools.

## 1. 获取文件夹的目录结构 getFileList.py

- 操作系统 macOS (推测可用于 Linux)
- 使用 [Typora](https://www.typora.io/) && Markdown

效果如图

![IMG_6512](/images/IMG1_1.JPEG)

注：

- `[TOC]` 生成 md 文件的目录
- 小标题的不同层级表示了目录的不同层级
- 文件使用 `[名字](绝对地址)` 的方式生成超链接，点击可打开。
- 排除了 mac 系统生成的 `.DS_Store` 文件

**目的** ： 整理文件较多的目录

**使用方式**：

```shell
$ python3 "该工具的 .py 文件的绝对地址"
```

**TODO：**

1. 配合 Automator 使用定时更新
