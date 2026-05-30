[English](README.md) | [中文](README_CN.md)

# 📊 repo-stats

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-orange.svg)]()

> 分析GitHub仓库并生成美观的统计报告

## ✨ 功能特性

- 📈 **全面分析** - Star、Fork、Issue、贡献者、语言统计
- 🎨 **美观输出** - 终端表格和彩色格式化
- 📊 **JSON导出** - 导出数据用于进一步分析
- 🔍 **详细洞察** - 贡献者排名、最近提交、语言占比
- ⚡ **快速** - 直接从GitHub API获取数据
- 🔧 **CLI界面** - 命令行操作简单便捷
- 📦 **Pip安装** - 一键安装

## 📦 安装

### 通过PyPI安装（推荐）

```bash
pip install repo-stats
```

### 从源码安装

```bash
git clone https://github.com/Alex-2Code/repo-stats.git
cd repo-stats
pip install -e .
```

## 🔧 配置

1. 从 [github.com/settings/tokens](https://github.com/settings/tokens) 获取GitHub API令牌

2. 设置令牌（可选但推荐，可获得更高API限额）：

```bash
export GITHUB_TOKEN="ghp_your-token-here"
```

## 🚀 使用方法

### 基本用法

```bash
# 分析仓库
repo-stats owner/repo

# 使用GitHub URL分析
repo-stats https://github.com/owner/repo

# 导出为JSON
repo-stats owner/repo --format json --output report.json
```

### 命令选项

```bash
repo-stats [OPTIONS] REPO

选项:
  --version                显示版本
  -t, --token TEXT         GitHub API令牌 (或设置 GITHUB_TOKEN 环境变量)
  -f, --format [text|json] 输出格式 (默认: text)
  -c, --contributors INT   显示的贡献者数量 (默认: 10)
  -n, --commits INT        显示的最近提交数量 (默认: 5)
  -o, --output TEXT        输出文件路径 (用于JSON格式)
  --help                   显示帮助信息
```

## 📖 使用示例

### 示例 1: 基本分析

```bash
$ repo-stats facebook/react

📊 仓库: facebook/react

┌─────────────────┬──────────────────────────────────────────┐
│ 属性            │ 值                                       │
├─────────────────┼──────────────────────────────────────────┤
│ 描述            │ The library for web and native user      │
│                 │ interfaces.                              │
│ ⭐ Star          │ 230.5K                                   │
│ 🍴 Fork          │ 47.2K                                    │
│ 👀 关注者        │ 6.8K                                     │
│ 📋 Open Issues   │ 756                                      │
│ 📦 大小          │ 22.5 MB                                  │
│ 🌐 语言          │ JavaScript                               │
│ 📜 许可证        │ MIT License                              │
│ 📅 创建时间      │ 2013-05-24                               │
│ 🔄 更新时间      │ 2026-05-28                               │
└─────────────────┴──────────────────────────────────────────┘

💻 语言统计

┌──────────────┬────────────┬────────────┐
│ 语言         │        字节│    占比     │
├──────────────┼────────────┼────────────┤
│ JavaScript   │    3,245K  │     62.3%  │
│ TypeScript   │    1,892K  │     36.3%  │
│ CSS          │       45K  │      0.9%  │
└──────────────┴────────────┴────────────┘

👥 贡献者排名

┌─────┬─────────────┬───────────────────┐
│   # │ 用户名      │      贡献次数     │
├─────┼─────────────┼───────────────────┤
│   1 │ gaearon     │             1,234 │
│   2 │ sophiebits  │               892 │
└─────┴─────────────┴───────────────────┘
```

### 示例 2: JSON导出

```bash
$ repo-stats facebook/react --format json --output react-stats.json

报告已保存到 react-stats.json
```

### 示例 3: 自定义数量

```bash
$ repo-stats facebook/react --contributors 20 --commits 10

# 显示前20个贡献者和10条最近提交
```

## 📊 输出格式

### 文本格式（默认）

带颜色和表格的美观终端输出。

### JSON格式

```json
{
  "repository": {
    "name": "facebook/react",
    "description": "The library for web and native user interfaces.",
    "stars": 230500,
    "forks": 47200,
    "language": "JavaScript",
    "license": "MIT License",
    "url": "https://github.com/facebook/react"
  },
  "languages": {
    "JavaScript": 62.3,
    "TypeScript": 36.3
  },
  "top_contributors": [
    {"username": "gaearon", "contributions": 1234}
  ]
}
```

## 🔑 API限额

GitHub API有限额：
- **未认证**: 60次请求/小时
- **已认证**: 5,000次请求/小时

为获得最佳体验，请设置 `GITHUB_TOKEN` 环境变量。

## 🤝 贡献

欢迎贡献！请随时提交Pull Request。

## 📄 许可证

本项目基于MIT许可证 - 详见 [LICENSE](LICENSE) 文件

## 📧 联系方式

- GitHub: [@Alex-2Code](https://github.com/Alex-2Code)

---

由 [Alex-2Code](https://github.com/Alex-2Code) 用 ❤️ 制作

---
<!-- last-updated -->
*最后更新: 2026-05-30*<!-- /last-updated -->
