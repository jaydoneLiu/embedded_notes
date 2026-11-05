# -*- coding: utf-8 -*-
"""从 Obsidian 库同步 Markdown 到 MkDocs docs，并转换 wikilink。"""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VAULT = ROOT.parent / "嵌入式软件学习库"
DOCS = ROOT / "docs"

MODULES = [
    "01-Linux驱动与内核",
    "02-算法与LeetCode",
    "03-嵌入式基础",
    "04-RTOS与实时系统",
    "05-硬件与SoC",
    "06-通信协议与外设",
    "07-工具链与调试",
    "08-项目实战",
    "09-面试复习",
    "99-模板与资源",
]

# [[path|alias]] or [[path]]
WIKI_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|([^\]]+))?\]\]")


def wiki_to_md(text: str) -> str:
    def repl(m: re.Match) -> str:
        target = m.group(1).strip().replace("\\", "/")
        alias = (m.group(2) or target).strip()
        # _MOC -> index
        if target.endswith("/_MOC"):
            target = target[: -len("/_MOC")] + "/index"
        elif target.endswith("_MOC"):
            # e.g. 01-Linux驱动与内核/_MOC
            target = target[: -len("_MOC")] + "index"
        if not target.endswith(".md"):
            # folder index or file
            if "/" in target and not target.split("/")[-1].endswith(".md"):
                # leave as-is; mkdocs resolves .md
                pass
            target = target + ".md" if not target.endswith("index") else target + ".md"
            if target.endswith("index.md") is False and "/index.md" not in target:
                # already handled
                pass
        # normalize _MOC.md references
        target = target.replace("/_MOC.md", "/index.md").replace("_MOC.md", "index.md")
        if target.endswith("index.md") and not target.endswith("/index.md"):
            # "01-xxxindex.md" bug guard
            pass
        # fix patterns like 01-xxx/index.md
        if target.endswith("index.md") is False and target.endswith(".md") is False:
            target += ".md"
        return f"[{alias}]({target})"

    return WIKI_RE.sub(repl, text)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def sync() -> None:
    if not VAULT.exists():
        raise SystemExit(f"找不到 Obsidian 库: {VAULT}")

    home = VAULT / "00-首页.md"
    if home.exists():
        # 网站首页单独维护也可；这里用转换后的库首页作兜底
        text = wiki_to_md(home.read_text(encoding="utf-8"))
        # 站点首页用 docs/index.md 的定制版优先：仅当强制覆盖时使用
        # 这里仍同步一份到 _vault_home.md 便于对照
        write_text(DOCS / "_vault_home.md", text)

    for name in MODULES:
        src_dir = VAULT / name
        dst_dir = DOCS / name
        if not src_dir.exists():
            continue
        dst_dir.mkdir(parents=True, exist_ok=True)
        moc = src_dir / "_MOC.md"
        if moc.exists():
            write_text(dst_dir / "index.md", wiki_to_md(moc.read_text(encoding="utf-8")))
        for md in src_dir.glob("*.md"):
            if md.name == "_MOC.md":
                continue
            write_text(dst_dir / md.name, wiki_to_md(md.read_text(encoding="utf-8")))

    # 清理旧的空附件目录占位
    print(f"已同步: {VAULT} -> {DOCS}")


if __name__ == "__main__":
    sync()
