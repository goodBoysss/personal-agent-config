#!/usr/bin/env python3
"""生成、检查并备份安装个人规则，仅使用 Python 标准库。"""

import argparse
from datetime import datetime
import difflib
import os
from pathlib import Path
import shutil
import sys
import tempfile


ROOT = Path(__file__).resolve().parent.parent
COMMON = (
    "rules/common.md",
    "rules/environment.md",
    "rules/projects/wanxin.md",
    "rules/projects/wx-cli.md",
)
TARGETS = {
    "codex": ("AGENTS.md", ".codex/AGENTS.md"),
    "claude": ("CLAUDE.md", ".claude/CLAUDE.md"),
}


def render(tool, home, bash_root, wanxin_root):
    """合并公共和工具规则，并为目标机器展开本地路径占位符。"""
    sections = [
        "<!-- 由 personal-agent-config/scripts/manage.py 生成；请修改仓库 rules/ 后重新生成。 -->",
    ]
    for name in (*COMMON, "rules/tools/{}.md".format(tool)):
        sections.append((ROOT / name).read_text(encoding="utf-8").strip())
    content = "\n\n".join(sections) + "\n"
    for token, path in (
        ("{{HOME}}", home),
        ("{{BASH_ROOT}}", bash_root),
        ("{{WANXIN_ROOT}}", wanxin_root),
    ):
        content = content.replace(token, str(path))
    if "{{" in content or "}}" in content:
        raise ValueError("规则中存在未解析的路径占位符")
    return content


def write_atomic(path, content):
    """通过同目录临时文件原子替换文本，保留已有文件的权限。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = path.stat().st_mode & 0o777 if path.exists() else 0o644
    fd, name = tempfile.mkstemp(prefix=".personal-agent-config-", dir=path.parent)
    temporary = Path(name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            stream.write(content)
        temporary.chmod(mode)
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def check_generated(contents):
    """比较生成文件和规则源文件；缺失或不一致时返回非零状态。"""
    valid = True
    for tool, content in contents.items():
        path = ROOT / "generated" / tool / TARGETS[tool][0]
        if not path.is_file():
            print("缺少生成文件：{}".format(path), file=sys.stderr)
            valid = False
            continue
        current = path.read_text(encoding="utf-8")
        if current != content:
            valid = False
            print("".join(difflib.unified_diff(
                current.splitlines(keepends=True),
                content.splitlines(keepends=True),
                fromfile=str(path),
                tofile="按当前规则生成的内容",
            )), end="")
    if valid:
        print("检查通过：生成文件与规则源文件一致。")
    return 0 if valid else 1


def install(contents, home):
    """先备份全部待覆盖入口，再安装规则；不改动其他配置和项目记忆。"""
    changes = []
    for tool, content in contents.items():
        path = home / TARGETS[tool][1]
        if path.is_symlink() or (path.exists() and not path.is_file()):
            raise ValueError("目标不是普通文件，拒绝覆盖：{}".format(path))
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            changes.append((path, content))
    if not changes:
        print("规则已是最新，无需安装。")
        return 0

    existing = [path for path, _ in changes if path.exists()]
    if existing:
        backup_root = home / ".local/state/personal-agent-config/backups"
        backup_root.mkdir(parents=True, exist_ok=True)
        backup = Path(tempfile.mkdtemp(
            prefix=datetime.now().strftime("%Y%m%d-%H%M%S-"), dir=backup_root,
        ))
        for path in existing:
            destination = backup / path.relative_to(home)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, destination)
        print("原文件已备份：{}".format(backup))

    for path, content in changes:
        write_atomic(path, content)
        print("已安装：{}".format(path))
    return 0


def main():
    """解析生成、校验和安装命令；默认仅生成仓库内的入口文件。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("build", "check", "install"))
    parser.add_argument("--tool", choices=("all", "codex", "claude"), default="all")
    parser.add_argument("--home", type=Path, default=Path.home(), help="目标用户主目录")
    parser.add_argument("--bash-root", type=Path, help="Bash 仓库位置")
    parser.add_argument("--wanxin-root", type=Path, help="玩心项目根目录")
    args = parser.parse_args()
    home = args.home.expanduser().resolve()
    bash_root = (args.bash_root or home / "Desktop/www/bash").expanduser().resolve()
    wanxin_root = (args.wanxin_root or home / "Desktop/www/wanxin").expanduser().resolve()
    tools = TARGETS if args.tool == "all" else (args.tool,)
    contents = {
        tool: render(tool, home, bash_root, wanxin_root) for tool in tools
    }
    if args.action == "check":
        return check_generated(contents)
    if args.action == "install":
        return install(contents, home)
    for tool, content in contents.items():
        path = ROOT / "generated" / tool / TARGETS[tool][0]
        write_atomic(path, content)
        print("已生成：{}".format(path))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError) as error:
        print("操作失败：{}".format(error), file=sys.stderr)
        sys.exit(1)
