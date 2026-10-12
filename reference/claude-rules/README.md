# 原有 Claude 语言规则备份

这里的 `php/` 和 `golang/` 各五份文件原样复制自 2026-10-12 的 `~/.claude/rules/`，分别包含 coding-style、hooks、patterns、security、testing。

这些属于已有通用技术规范，未将其全部提升为个人偏好。默认生成和安装流程不加载本目录。

恢复或采用前留意：

- 原文链接到 `../common/*.md`，但本机原目录中没有对应的 common 规则；因此这些引用保持原样作为历史记录，并不保证可用。
- 原文提到的 Skills 未必已经安装；`hooks.md` 只描述建议配置，不意味着相关自动格式化 Hooks 已启用。
- PHP 规范提到的 typed property、readonly 和部分工具不适用于 PHP 7.0。玩心项目以 `rules/projects/wanxin.md` 的版本兼容要求为准。
- 原测试规范不能覆盖“助手临时测试测完删除、wx-cli 单元测试保留”的用户偏好。

需要恢复时先核对项目版本、缺失的依赖和引用，再将选中的文件合入 `~/.claude/rules/`；不建议不加核对地覆盖整个目录。
