# 嵌入式软件学习库

个人嵌入式软件公开学习站。当前先搭好框架，具体内容后续按需填充。

## 学习导航

| 模块 | 说明 |
|------|------|
| [Linux 驱动与内核](01-Linux驱动与内核/index.md) | 内核机制、字符/块/网络驱动、设备树 |
| [算法与 LeetCode](02-算法与LeetCode/index.md) | 数据结构、刷题路线、嵌入式常见题 |
| [嵌入式基础](03-嵌入式基础/index.md) | C/C++、内存、启动流程、裸机 |
| [RTOS 与实时系统](04-RTOS与实时系统/index.md) | FreeRTOS / RT-Thread 等 |
| [硬件与 SoC](05-硬件与SoC/index.md) | 芯片架构、全志 T113、外设 |
| [通信协议与外设](06-通信协议与外设/index.md) | UART/I2C/SPI/USB/以太网等 |
| [工具链与调试](07-工具链与调试/index.md) | 交叉编译、GDB、JTAG、性能分析 |
| [项目实战](08-项目实战/index.md) | 真实项目笔记与复盘 |
| [面试复习](09-面试复习/index.md) | 八股、场景题、项目讲述 |

## 使用说明

1. **写笔记**：用 Obsidian 打开同级目录 `嵌入式软件学习库`，或直接改本站 `docs/`
2. **同步到网站**：在 `嵌入式学习网站` 目录运行 `py sync_from_vault.py`
3. **本地预览**：`py -m mkdocs serve` → http://127.0.0.1:8000
4. **公开更新**：`git add .` → `git commit` → `git push`，稍后访问 https://jaydoneliu.github.io/embedded-notes/

## 待办方向

- [ ] 补齐各模块子目录与首批笔记
- [ ] 建立标签体系
- [ ] 按项目（如 T113）挂接实战笔记
- [x] 推送到 GitHub 仓库 `jaydoneLiu/embedded-notes` 并开启 Pages
