# 📚 Paper Research Skills — 学术论文选题工作流 Skills

一套面向 Claude Code 的学术论文选题工作流 Skills，帮助研究者从模糊想法到可开题定题，覆盖选题核心流程、文献去重检索、开题答辩模拟三个阶段。

## 包含的 Skills

| Skill | 说明 | 触发场景 |
|-------|------|---------|
| `paper-topic-selection` | 论文选题核心流程 | 选题、开题、题目太大、创新性不足、研究空白识别 |
| `paper-novelty-check` | 去重选题与增量文献检索 | 选题去重、文献增量检索、新颖性验证 |
| `paper-proposal-defense` | 开题答辩模拟与风险评估 | 开题答辩、答辩模拟、答辩问题准备 |

## 安装

将三个 Skill 目录复制到你的 Claude Code Skills 目录：

```bash
# 克隆仓库
git clone https://github.com/AlexYangge/paper-research-skills.git

# 复制到 Claude Code Skills 目录（Windows）
cp -r paper-research-skills/paper-topic-selection ~/.claude/skills/
cp -r paper-research-skills/paper-novelty-check ~/.claude/skills/
cp -r paper-research-skills/paper-proposal-defense ~/.claude/skills/
```

重启 Claude Code 后 Skills 自动生效。

## 使用流程

```
┌─────────────────────────────────────────────────────────────┐
│                    论文选题完整工作流                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [SKILL 1] paper-topic-selection                            │
│    Step 0: 文献检索初始化（强制）                              │
│    Step A: 边界定义（时间/资源/能力/规范）                     │
│    Step B: 三源并行生成候选题（8-12个）                        │
│    Step C: 四维漏斗筛选（价值×创新×可行×匹配）                 │
│    Step D: 题目收敛为可研究问题（RQ）                          │
│    Step E: 最小可行性预验证（MVP）                             │
│    Step F: 输出一页式定题卡                                    │
│         │                                                   │
│         │ 输出: 一页式定题卡 + References Ledger              │
│         ▼                                                   │
│  [SKILL 2] paper-novelty-check                              │
│    加载文献台账 → 增量检索 → 去重比对 → 新颖性评估              │
│         │                                                   │
│         │ 输出: 新颖性判定报告 + 更新后的 Ledger               │
│         ▼                                                   │
│  [SKILL 3] paper-proposal-defense                           │
│    评委视角解读 → 常见问题预回答 → 模拟 Q&A → 风险评估          │
│         │                                                   │
│         ▼                                                   │
│    输出: 答辩准备清单 + 48小时冲刺计划 + PPT大纲               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 触发示例

```text
# 触发 SKILL 1
"帮我选一个硕士论文题目，方向是自然语言处理"
"我的题目太大了，帮我缩小一下"
"开题被打回，说创新性不足怎么办"

# 触发 SKILL 2
"帮我验证一下这个选题有没有人做过"
"在已有文献基础上做增量检索"

# 触发 SKILL 3
"帮我准备开题答辩"
"模拟一下答辩可能会被问到什么问题"
```

## 目录结构

```
paper-research-skills/
├── paper-topic-selection/          # SKILL 1: 选题核心流程
│   ├── SKILL.md                    # 主文件
│   ├── references/
│   │   ├── search-strategies.md    # 检索策略模板
│   │   └── scoring-rubric.md       # 四维评分量规
│   └── assets/
│       └── topic-brief-template.md # 一页式定题卡模板
│
├── paper-novelty-check/            # SKILL 2: 去重检索
│   ├── SKILL.md                    # 主文件
│   └── scripts/
│       └── dedupe.py               # 文献去重脚本
│
├── paper-proposal-defense/         # SKILL 3: 答辩模拟
│   ├── SKILL.md                    # 主文件
│   ├── references/
│   │   └── defense-question-bank.md # 答辩问题库
│   └── assets/
│       └── defense-ppt-outline.md  # PPT 大纲模板
│
├── LICENSE
├── .gitignore
└── README.md
```

## 依赖

- [Claude Code](https://claude.ai/code) (CLI 或桌面版)
- Web 搜索能力（内置 WebSearch 工具）
- 可选：学术数据库访问（Google Scholar、Semantic Scholar、arXiv、PubMed 等）

## License

[MIT](LICENSE) — 自由使用、修改和分发。
