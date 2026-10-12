# 本机环境与资源访问

## Shell 与凭据

- 用户 Bash 入口是 `{{BASH_ROOT}}/main.bash`。
- 查用户已有命令时先读 `main.bash`，再读 `alias/.alias.bash`；后者自动加载全部 `alias/.alias.*.bash`。不要仅凭旧文档片段猜测命令。
- PHP 别名在 `{{BASH_ROOT}}/alias/.alias.php.bash`。
- 本地凭据位于 Bash 仓库的 `token/*.bash`，由 `main.bash` 加载。需要时在执行命令的同一 Shell 中加载；禁止将值输出到终端、回复、日志或版本库。
- 默认 Shell 中变量缺失时，检查加载链，必要时用 Bash 登录 Shell 重试。验证敏感变量时只检查是否存在，不回显值。

## 飞书与数据库

- 飞书文档和资源默认通过 `lark-cli` 访问；只有缺少特定能力时才回退到飞书 MCP。
- 只读数据库默认 project 为 `ad`；用户指定其他项目时以用户要求为准。
- 玩心生产数据库仅通过 `ad-readonly-database:readonly-db-guide` 技能及其只读数据库工具查询。
- 玩心测试环境连接从 `ad-admin-new/.env.local` 直接加载，不能用于生产查询，不输出连接凭据。
