# 个人 Agent 配置与习惯

保存个人习惯、项目约定和必要的恢复资料。公共规则只维护一份，再生成 Codex 与 Claude 的完整入口文件。

## 文件索引

| 文件或目录 | 用途 |
| --- | --- |
| [rules/common.md](rules/common.md) | 中文回复、输出格式、不自动提交、测试清理、代码注释、配图习惯 |
| [rules/environment.md](rules/environment.md) | Shell 入口、凭据使用边界、飞书和数据库访问 |
| [rules/projects/wanxin.md](rules/projects/wanxin.md) | 玩心 Git 流程、PHP 7.0 和本地运行 |
| [rules/projects/wx-cli.md](rules/projects/wx-cli.md) | 保留单元测试的例外 |
| [rules/tools/codex.md](rules/tools/codex.md) | 图片会话命名及 Otty 标题同步 |
| [rules/tools/claude.md](rules/tools/claude.md) | Claude 项目记忆维护约定 |
| [generated/codex/AGENTS.md](generated/codex/AGENTS.md) | 可安装到 `~/.codex/AGENTS.md` 的完整规则 |
| [generated/claude/CLAUDE.md](generated/claude/CLAUDE.md) | 可安装到 `~/.claude/CLAUDE.md` 的完整规则 |
| [reference/workflows.md](reference/workflows.md) | 从旧记忆整理的操作经验，按需查阅 |
| [reference/claude-rules/](reference/claude-rules/) | 原有 PHP、Go 规范的原样备份，不默认安装 |
| [settings/](settings/) | 精选的非敏感配置片段，不默认安装 |
| [docs/sources.md](docs/sources.md) | 来源、范围和冲突处理记录 |
| [scripts/manage.py](scripts/manage.py) | 生成、检查和备份安装入口 |

## 日常维护

修改 `rules/`，不要直接改 `generated/`。下列命令均在本仓库根目录执行，要求 Python 3.8 或更新版本，无第三方依赖。

生成两个工具的入口文件，仅写入本仓库：

```bash
python3 scripts/manage.py build
```

检查生成文件与规则一致：

```bash
python3 scripts/manage.py check
```

生成文件也应纳入 Git，方便直接审阅和手动恢复。规则中的 `{{HOME}}`、`{{BASH_ROOT}}`、`{{WANXIN_ROOT}}` 会根据目标机器展开；已提交的生成文件反映生成时的本机路径。

## 安装与恢复

首次整理仅生成仓库文件，不自动改动当前工具配置。需要启用时，安装命令直接从源规则重新生成内容，再写入两个工具的全局入口：

```bash
python3 scripts/manage.py install
```

只安装一个工具：

```bash
python3 scripts/manage.py install --tool codex
```

安装前，已有且将被覆盖的入口文件会统一备份到 `~/.local/state/personal-agent-config/backups/<时间-随机后缀>/`，保留原相对路径；内容相同时不重复写入或备份。目标文件为符号链接或目录时拒绝覆盖。恢复旧规则时，从对应备份目录将文件复制回原位置。

换电脑时先克隆本仓库及独立维护的 Bash 仓库，再运行安装命令。默认路径是当前用户的 `~/Desktop/www/bash` 和 `~/Desktop/www/wanxin`。目录布局不同可指定：

```bash
python3 scripts/manage.py install --bash-root /实际路径/bash --wanxin-root /实际路径/wanxin
```

可使用 `--home /临时目录` 演练安装；这个参数会同时改变安装位置、备份位置和默认的本地项目路径。

安装只管理 `~/.codex/AGENTS.md` 和 `~/.claude/CLAUDE.md`，不会替换登录信息、模型配置、MCP 配置、旧项目记忆或语言规则。旧项目记忆中“测试没有例外”等过时表述仍需在相应工具中按新规则更新；本次原文件未改动。

## 独立依赖与备份范围

- Shell 入口、别名和标题同步脚本继续在旁边的 `bash` Git 仓库维护，本仓库只引用它们。
- 标题功能依赖 Bash 仓库的 `bin/codex-session-title.py`、Otty 及当前会话环境。恢复这份文字规则不会自动安装这些依赖。
- Skills 与插件需要另外安装；本仓库没有备份插件缓存。
- PHP、Go 的旧语言规范保存在 `reference/claude-rules/`，查阅该目录 README 后再决定是否恢复。
- `settings/*.example.*` 是部分配置片段，不是完整配置文件。按需合并，不能直接覆盖原来的配置；Claude 示例保留了本机已有的权限提示设置，但不会自动启用。
- Token、密码、数据库连接值、登录状态、会话记录和缓存不纳入仓库。`.gitignore` 仅是辅助，提交前仍需检查差异。
- 只有推送到远端才具备异地备份；本次整理不自动执行 commit 或 push。建议远端仓库保持私有。
