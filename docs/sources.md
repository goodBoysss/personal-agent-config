# 来源与整理记录

整理日期：2026-10-12。这里只记录来源位置、内容范围及取舍，不存储凭据值。`~` 表示原机器用户主目录 `/Users/zhanglinxiao`。

## 全局配置来源

| 原位置 | 收录内容 | 新位置 |
| --- | --- | --- |
| `~/.codex/AGENTS.md` | 回复格式、注释规范、测试清理 | `rules/common.md` |
| 同上 | Shell 入口、测试/生产数据库访问 | `rules/environment.md` |
| 同上 | 图片会话标题完整约定 | `rules/tools/codex.md` |
| 同上 | PHP 7.0、玩心分支和 MR 流程 | `rules/projects/wanxin.md` |
| 同上 | wx-cli 单元测试例外 | `rules/common.md`、`rules/projects/wx-cli.md` |
| `~/.claude/CLAUDE.md` | 飞书优先 lark-cli、数据库默认 project=ad | `rules/environment.md` |
| `~/.claude/rules/php/*.md` | 原有 5 份 PHP 规范 | `reference/claude-rules/php/`，原样备份 |
| `~/.claude/rules/golang/*.md` | 原有 5 份 Go 规范 | `reference/claude-rules/golang/`，原样备份 |
| `~/.codex/config.toml` | 仅模型及推理强度 | `settings/codex.example.toml` |
| `~/.claude/settings.json` | 仅 skipDangerousModePermissionPrompt | `settings/claude.example.json` |

## Claude 项目记忆来源

以下项目目录均在 `~/.claude/projects/` 下，列出的文件位于各自的 `memory/` 子目录。原 `MEMORY.md` 只是索引，本表替代其备份用途。

| 项目目录 | 记忆文件 | 整理去向 |
| --- | --- | --- |
| `-Users-zhanglinxiao` | `feedback_lark_cli_docs.md` | `reference/workflows.md`：飞书文档 |
| 同上 | `feedback_tool_optional_params.md` | `rules/common.md`：工具参数 |
| `-Users-zhanglinxiao-Desktop` | `feedback_mcp_config_location.md` | `reference/workflows.md`：MCP 配置旧记录，标注未复核 |
| `-Users-zhanglinxiao-Desktop-www` | `feedback_flow_docs_visuals.md` | `rules/common.md`：说明文档配图 |
| `-Users-zhanglinxiao-Desktop-www-wanxin` | `clean-up-scratch-files.md` | `rules/common.md`，修正旧的无例外表述和过度清理范围 |
| 同上 | `shell-env-entry.md` | `rules/environment.md`、`reference/workflows.md` |
| 同上 | `local-credentials-location.md` | `rules/environment.md`、`reference/workflows.md`，仅位置 |
| 同上 | `gamesh-sidecar-required-for-media.md` | `rules/projects/wanxin.md`、`reference/workflows.md` |
| 同上 | `prod-artisan-ad-admin-new.md` | `reference/workflows.md`：线上 PHP CLI |
| `-Users-zhanglinxiao-Desktop-www-wanxin-ad-admin-front-3-0` | `no-auto-commit.md` | `rules/common.md`：原文记录用户要求“用户层记一下”，提升为通用偏好 |
| `-Users-zhanglinxiao-Desktop-www-wanxin-ad-admin-new` | `reply-in-chinese.md` | `rules/common.md`：中文回复 |
| 同上 | `php_method_contracts.md` | `rules/common.md`：PHP 类型与注释 |
| 同上 | `php_method_spacing_review.md` | `rules/common.md`：方法间空行 |
| 同上 | `bash-login-shell-env.md` | `rules/environment.md`；去掉会回显敏感变量的旧示例 |
| 同上 | `apifox-update-docs-from-code.md` | `reference/workflows.md`：文档更新流程，仅保留必要非敏感线索 |

## 统一与修正

1. **测试清理：** 以本次用户提供且现存于 Codex 全局规则中的要求为准；保留 `wx-cli` 单元测试、用户原有测试和用户明确要求保留的测试。旧记忆的“没有例外”不再继承。
2. **清理范围：** 旧记忆要求“未跟踪文件必须为空”，可能误删正式新增文件。整理为仅清理助手产生的临时验证产物；不删除用户文件，不停止原有服务。
3. **中文回复、不自动提交、流程图：** 从分散的项目记忆提升为公共个人习惯，两个工具使用相同内容。
4. **PHP 类型：** 保留参数类型、返回类型和 PHPDoc 要求，同时明确 PHP 7.0 兼容性。现代 PHP 的 typed property、readonly 不能直接用于 `ad-admin-new`。
5. **敏感变量检查：** 旧记忆中的 `echo` 敏感变量示例不保留；只检查是否设置，不输出值。
6. **操作经验与强制规则分开：** 飞书旧参数、MCP 位置、Apifox API、线上路径属于历史经验，需按当前工具及部署核验，默认不拼入全局指令。
7. **工具维护约定：** `rules/tools/claude.md` 中同步跨项目偏好的要求，以及仓库根 `AGENTS.md`，是本次整理新增的维护约定，并非声称原来就有的用户习惯。

## 未收录的内容

- 认证文件、凭据脚本正文、完整 env/MCP/provider 配置、会话正文和 SQLite 状态库。
- `~/.codex/rules/default.rules`：当前是三条历史命令放行记录，不作为通用偏好迁移。
- `~/.codex/hooks.json`：由 Otty 集成管理，包含本机运行时路径，恢复时由 Otty 配置。
- Codex 的 `memories/` 目录在整理时为空；未读取记忆数据库或从会话历史推断新偏好。
- 已安装 Skills、插件缓存，以及 Bash 仓库内独立维护的脚本源码。

本次仅写入本仓库，未修改原始全局规则、项目记忆或现有工具配置。安装脚本以后也不会自动改写旧项目记忆。
