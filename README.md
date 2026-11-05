# 嵌入式软件学习库（公开网站）

基于 Obsidian 笔记库，用 **MkDocs Material** 生成的公开学习站点。

## 本地预览

```bash
cd 嵌入式学习网站
py -m pip install -r requirements.txt
py -m mkdocs serve
```

浏览器打开：http://127.0.0.1:8000

## 从 Obsidian 库同步

Obsidian 库路径：`../嵌入式软件学习库`

```bash
py sync_from_vault.py
py -m mkdocs serve
```

## 修改网站内容

推荐流程（Obsidian → 网站）：

1. 用 Obsidian 打开 `../嵌入式软件学习库`，编辑或新增 `.md` 笔记
2. 在本目录同步并本地预览：

```bash
py sync_from_vault.py
py -m mkdocs serve
```

3. 确认无误后提交推送（公开站才会更新）：

```bash
git add .
git commit -m "更新笔记内容"
git push
```

也可以直接改本目录下的 `docs/`（改完同样 `git add/commit/push`）。

## 发布为公开网站（GitHub Pages）

目标地址：https://jaydoneliu.github.io/embedded_notes/

仓库已创建：`https://github.com/jaydoneLiu/embedded_notes`

```bash
git add .
git commit -m "init: embedded learning site"
git branch -M main
git remote add origin https://github.com/jaydoneLiu/embedded_notes.git
git push -u origin main
```

然后：仓库 → **Settings → Pages → Source** 选 **GitHub Actions**  
等 Actions 成功后访问：https://jaydoneliu.github.io/embedded_notes/

## 目录说明

- `docs/`：网站正文（可由 Obsidian 库同步）
- `mkdocs.yml`：站点配置与导航
- `sync_from_vault.py`：Obsidian → docs 同步脚本
