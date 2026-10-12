# 本机操作经验归档

从已有 Claude 记忆整理于 2026-10-12。这些是历史操作线索，不代表当前工具参数、服务部署或授权范围已经重新验证；执行前按当前环境核对。

## Shell 命令与凭据位置

Bash 仓库默认为 `~/Desktop/www/bash`。从 `main.bash` → `alias/.alias.bash` → `alias/.alias.*.bash` 查真实命令定义。

| 文件 | 用途 |
| --- | --- |
| `alias/.alias.php.bash` | php81、php70、Composer、Gamesh 启动 |
| `alias/.alias.git.bash` | 分支、提交、MR、worktree 快捷命令 |
| `alias/.alias.codex.bash` | Codex 启动、恢复与分叉 |
| `alias/.alias.claude.bash` | Claude 启动与更新 |
| `alias/.alias.wanxin.bash` | 玩心子项目目录跳转 |
| `alias/.alias.go.bash` | Go 运行及依赖管理 |
| `alias/.alias.npm.bash` | 前端环境启动 |

`main.bash` 加载 `token/*.bash`。历史记录提到 `wx-admin-new.bash`、`gitlab.bash`、`apifox.bash`；这里不备份文件内容。Shell 状态不一定跨工具调用保存，需要时在执行命令的同一 Shell 中加载。环境变量缺失时可检查登录 Shell 加载链，禁止回显敏感值。

## 本地 PHP 与媒体接口

`ad-admin-new` 使用 `php70` Docker 别名，当前目录挂载到 `/www`。交互别名可能带 `-it`，自动化执行时注意 TTY 要求。

本地真实媒体调用经 Gamesh RPC 和 OutboundGateway 转发，不能把裸跑 tinker/artisan 的失败直接判为业务代码错误。历史环境需要通过 `php artisan gamesh start` 启动 sidecar，才会消费 `SIDECAR_BASE_LINE_REMOTE` 等回落配置。

历史故障线索：缺少 sidecar 时可能报 `GatewayTransport.php`、`server not found`。当时 `ad-campaign` 的 `Group::action()` 在 `finally` 中仍会保存状态，因此失败的真实调用也可能留下数据库变更。验证前检查当前代码及副作用；这条经验不是修改生产数据的授权。

## 线上 ad-admin-new artisan

历史线上环境使用 `www` 用户及宿主机 PHP 7.0.27，而不是本地 Docker 别名。原记忆记录的入口为：

```bash
sudo -u www /usr/local/php-7.0.27/bin/php /data/web/yaf/tg3.hzwxbz2.cn/artisan <command>
```

`<command>` 必须替换成当前任务明确需要的命令；执行前确认主机和部署路径。使用正确的运行用户可避免日志、缓存属主意外变成 root。

## 飞书文档

优先使用 lark-cli。旧记忆记录读取文档使用 v2 API：

```bash
lark-cli docs +fetch --doc '<飞书URL或token>' --api-version v2 --format pretty
```

获取大纲以定位块：

```bash
lark-cli docs +fetch --doc '<飞书URL或token>' --api-version v2 --scope outline --format json
```

旧版本更新接口要求 `--command` 搭配 `--content`；追加使用 `append`，插入到指定块后使用 `block_insert_after` 并提供 `--block-id`。历史试错中，位置参数 URL，以及把 `--mode`、`--markdown`、`--selection-by-title` 混入该流程，曾导致参数错误。当前用法以已安装技能及 CLI 版本为准，不把历史参数当作永久接口。

## 根据后端代码更新 Apifox

旧记忆涉及 `ad-admin-new` 的 Apifox 项目 `581462`、默认模块。

1. 从路由、Controller、Logic 查明真实接口与参数。
2. 生成相应路径的 OpenAPI 3.0 内容。
3. 当时的 Apifox MCP 只有读取和刷新能力；需要用户授权的文档更新时，可核实当前开放 API 是否支持 `import-openapi`。
4. 旧导入 API 的 `input` 是 OpenAPI 文档的 JSON 字符串；`endpointOverwriteBehavior=OVERWRITE_EXISTING` 会覆盖同路径接口，须与本次更新范围一致。
5. 更新后刷新并读回文档，确认结果。Apifox 内部接口 ID 未必存在于导出的 OpenAPI 中，可按 path/summary 定位。

凭据通过现有本地配置安全加载，本仓库不复制 Token。旧记忆中的凭据存储位置和权限不能保证长期有效，也不构成调用授权。

## MCP 配置位置的旧记录

桌面项目记忆曾要求把其使用的 MCP 配置放到 `~/.mcp.json`，不要误写到 `~/.claude/.mcp.json`。这只是该次环境接入的历史记录；本次没有验证不同客户端和版本的加载规则，不将它提升为全局强制规则。操作前检查当前客户端实际采用的配置入口。
