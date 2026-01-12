# 塔罗牌实验室 (LetFate Tarot Lab)

这是一个全面的塔罗牌资源库，包含塔罗牌数据库、图片资源以及各种实用工具。

## 📁 项目结构

```
letfate-tarot-lab/
├── TarotDB/               # 塔罗牌数据库
│   ├── cards.json        # 78张塔罗牌详细信息
│   └── spreads_db.json   # 牌阵数据库
├── SimpleTarotPng/       # 标准塔罗牌图片资源
│   ├── Major_Arcana/     # 大阿卡纳 (22张)
│   ├── Cups/            # 圣杯牌组 (14张)
│   ├── Swords/          # 宝剑牌组 (14张)
│   ├── Wands/           # 权杖牌组 (14张)
│   └── Pents/           # 金币牌组 (14张)
├── AkaxiTarot/          # Akaxi 风格塔罗牌图片
├── AkaxiLenormand/      # Akaxi 风格莱恩曼德牌图片
├── Pixel-Lenormand/     # 像素风格莱恩曼德牌图片
├── SimpleLenormand/     # 简化版莱恩曼德牌图片
└── Script/              # 实用脚本和资源
    ├── DownLoad.py      # 批量下载脚本
    ├── akaxi-tarot.txt  # Akaxi 塔罗牌 URL 列表
    ├── akaxi-lenormand.txt  # Akaxi 莱恩曼德牌 URL 列表
    ├── pixel-lenormand.txt  # 像素莱恩曼德牌 URL 列表
    └── simple-lenormand.txt  # 简化莱恩曼德牌 URL 列表
```

## 🗃️ 数据库结构

### TarotDB/cards.json

包含完整的 78 张塔罗牌信息：

```json
{
  "name": "牌名 (中英文)",
  "description": "详细的牌面描述和象征意义",
  "normal": "正位含义",
  "reversed": "逆位含义",
  "detail": "详细解读链接",
  "link": "对应的图片文件名"
}
```

### TarotDB/spreads_db.json

包含多种塔罗牌阵信息：

```json
{
  "name": "牌阵名称",
  "description": "牌阵用途和解读方法"
}
```

包含的牌阵类型：
- 三张牌占卜法
- 时间流牌阵
- 圣三角牌阵
- 四元素牌阵
- 恋人金字塔
- 爱情大十字
- 寻找对象牌阵
- 等等...

## 🖼️ 图片资源

### SimpleTarotPng/

标准塔罗牌图片资源，包含 78 张完整的塔罗牌：

- **大阿卡纳 (Major Arcana)**: 22 张，从愚人到世界
- **小阿卡纳 (Minor Arcana)**: 56 张，分为四个花色
  - **圣杯 (Cups)**: 代表情感、直觉、水元素
  - **宝剑 (Swords)**: 代表思维、沟通、风元素
  - **权杖 (Wands)**: 代表行动、意志、火元素
  - **金币 (Pents/Pentacles)**: 代表物质、稳定、土元素

### 其他风格

- **AkaxiTarot/**: 独特的 Akaxi 风格塔罗牌 (78 张)
- **AkaxiLenormand/**: Akaxi 风格的莱恩曼德牌 (36 张)
- **Pixel-Lenormand/**: 像素风格莱恩曼德牌
- **SimpleLenormand/**: 简化版莱恩曼德牌

## 🔧 工具和脚本

### DownLoad.py

Python 批量下载脚本，用于从提供的 URL 列表下载图片资源。

使用方法：
```bash
python Script/DownLoad.py <url_list_file>
```

支持的 URL 列表文件：
- `akaxi-tarot.txt`: 下载 Akaxi 塔罗牌 (78 张)
- `akaxi-lenormand.txt`: 下载 Akaxi 莱恩曼德牌 (36 张)
- `pixel-lenormand.txt`: 下载像素莱恩曼德牌
- `simple-lenormand.txt`: 下载简化莱恩曼德牌

## 📊 统计信息

- **塔罗牌总数**: 78 张
- **大阿卡纳**: 22 张
- **小阿卡纳**: 56 张
- **牌阵类型**: 20+ 种
- **图片资源**: 200+ 张不同风格的牌面图片

## 🎯 用途

这个项目可以用于：

- **塔罗牌占卜应用**: 提供完整的塔罗牌数据和图片
- **学习塔罗牌**: 详细的牌面含义和解读
- **牌阵练习**: 多种传统和现代牌阵
- **设计参考**: 不同风格的塔罗牌艺术作品
- **开发集成**: JSON 格式的数据易于集成到应用中

## 📝 数据来源

塔罗牌含义解释基于传统塔罗牌体系，结合现代解读方式。图片资源来自公开的塔罗牌艺术作品。

## 🔄 更新日志

- **v1.0** (2025-01-12)
  - 初始项目创建
  - 添加 78 张塔罗牌数据库
  - 添加多种牌阵数据库
  - 添加基础图片资源
  - 添加下载脚本

## 📄 许可证

本项目仅供学习和研究使用。图片资源版权归原作者所有。

## 🤝 贡献

欢迎提交问题报告和改进建议！

## 📧 联系方式

如有问题或建议，请通过以下方式联系：
- 项目仓库: [GitHub 地址]
- 邮箱: [联系邮箱]

---

**LetFate Tarot Lab** - 探索塔罗牌的奥秘 🌟
