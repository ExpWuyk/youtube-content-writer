# YouTube Content Writer - Claude Code Skill

一个 [Claude Code](https://claude.com/claude-code) 技能插件，自动为 YouTube 视频生成国内平台（B站、抖音等）搬运发布所需的全套文案。

## 功能

给 Claude Code 一个 YouTube 视频链接，自动生成：

- **视频核心信息解析**：主题定位、高光亮点、合规信息、关键词库
- **5组差异化爆款标题**（≤30字）：SEO关键词型、悬念钩子型、情绪共鸣型、痛点戳中型、数字干货型
- **3版作品简介**：完整版、精简版、极简版
- **20个分层级话题标签**：核心大词、垂类中词、长尾精准词、平台热门流量词

所有内容可直接复制粘贴到发布后台，包含合规的原素材来源标注。

## 前置要求

- [Claude Code](https://claude.com/claude-code) 已安装
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) 已安装（用于提取视频元数据）
- Python 3.8+

## 安装

### 方法一：手动安装（推荐）

1. 克隆仓库：
   ```bash
   git clone https://github.com/ExpWuyk/youtube-content-writer.git
   ```

2. 复制 skill 到 Claude Code 技能目录：
   ```bash
   cp -r skill/youtube-content-writer ~/.claude/skills/
   ```

3. 复制斜杠命令（可选）：
   ```bash
   mkdir -p ~/.claude/commands
   cp commands/yt-content.md ~/.claude/commands/
   ```

### 方法二：安装 .skill 文件

1. 下载 `youtube-content-writer.skill` 文件
2. 在 Claude Code 中运行：
   ```
   /install-skill youtube-content-writer.skill
   ```

## 使用方式

### 方式一：斜杠命令
```
/yt-content https://www.youtube.com/watch?v=VIDEO_ID
```

### 方式二：直接发送链接
直接在 Claude Code 中发送 YouTube 视频链接，skill 会自动识别并触发。

## 输出示例

```
## 第一步：视频核心信息解析
### 1. 核心定位
- 核心主题：...
- 所属垂类：...
- 核心受众：...

### 2. 高光亮点
### 3. 合规信息
### 4. 关键词库

## 第二步：全套可直接复制发布文案
### 1. 作品标题（5组，均≤30字）
### 2. 作品简介（完整版/精简版/极简版）
### 3. 话题标签（20个，带#，分层级）
```

## 项目结构

```
youtube-content-writer/
├── README.md
├── LICENSE
├── .gitignore
├── skill/
│   └── youtube-content-writer/
│       ├── SKILL.md                    # 核心技能指令
│       ├── references/
│       │   └── content-prompt.md       # 完整输出模板与规则
│       └── scripts/
│           └── fetch_video_meta.py     # yt-dlp 元数据提取脚本
├── commands/
│   └── yt-content.md                   # 斜杠命令定义
└── youtube-content-writer.skill        # 打包好的 .skill 文件
```

## License

MIT
