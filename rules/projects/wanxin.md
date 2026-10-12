# 玩心项目约定

## PHP 与本地运行

- `ad-admin-new` 位于 `{{WANXIN_ROOT}}/ad-admin-new`，运行 PHP 7.0。使用 `.alias.php.bash` 中的 `php70`，通过 `dnmp-php70` Docker 镜像运行，当前目录挂载到 `/www`。
- 别名包含 `-it` 时，非交互式执行需按实际情况移除交互参数，避免 TTY 错误。
- 代码类型声明和语法必须兼容 PHP 7.0，不能直接套用现代 PHP 的 typed property、readonly 等语法。
- 本地验证真实媒体调用前，需要通过 `php artisan gamesh start` 启动包含 sidecar 的服务；具体启动方式先查看现有别名。

## Git 分支规范

- 适用于玩心（Wanxin）项目；以 `ad-admin-new` 现有分支实践为准。
- 新功能分支命名为 `feature/<业务描述>_<YYYYMMDD>`；问题修复分支统一使用 `hotfix/<问题描述>_<YYYYMMDD>`。描述使用小写英文和下划线，日期使用创建当天的实际日期。
- 新业务分支从最新的 `origin/master` 创建；业务开发和后续修复均提交到原始业务分支。
- 合入 `dev` 或 `release` 时，先检查原始业务分支与最新目标分支是否冲突；无冲突时直接用原始业务分支申请 MR，不提前创建环境合并分支。此规则优先于技能中默认创建环境合并分支的流程。
- 仅在有冲突时，从原始业务分支创建同名加 `_dev` 或 `_release` 后缀的环境合并分支，在该分支合并最新 `origin/dev` 或 `origin/release` 并解决冲突，再提交 MR 到对应环境。
- 需要处理环境冲突且对应环境合并分支已存在时复用，将原始业务分支的新提交同步过去；环境冲突仅在对应环境合并分支处理。
- 合入 `master` 使用原始业务分支；不要将 `dev`、`release` 或其环境合并分支反向合入原始业务分支，避免带入其他需求。
- 推送业务分支时设置其跟踪远端同名分支，不要将 `origin/master` 设为业务分支的 upstream。
- 提交信息使用具体中文描述，避免仅写 `modify`；解决环境合并冲突时可使用“合并dev解决冲突”或“合并release解决冲突”。
- 示例：`feature/ubmax_rule_control_20260920`、`feature/ubmax_rule_control_20260920_dev`、`feature/ubmax_rule_control_20260920_release`。
- 历史分支可能存在 `fix/`、连字符或无日期等不统一形式；新建分支按上述规则执行，不自动重命名历史分支。
