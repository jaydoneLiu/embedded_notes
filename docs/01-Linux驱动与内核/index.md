---
title: Linux 驱动与内核
tags:
  - moc
  - linux
  - driver
  - kernel
---

# Linux 驱动与内核

> 框架占位：后续按小节填充笔记。

## 目录框架

### 1. 内核基础
- [ ] 内核架构与启动流程

- [ ] 进程 / 线程 / 调度

  进程是资源调度的最小单位

  线程是cpu调度的最小单位

- [ ] 内存管理（页表、kmalloc、vmalloc）

- [ ] 中断与软中断 / tasklet / workqueue

- [ ] 同步机制（自旋锁、互斥、信号量、RCU）

### 2. 驱动模型
- [ ] 字符设备驱动
- [ ] 平台设备与 Platform Driver
- [ ] 设备树（Device Tree）
- [ ] 总线 / 设备 / 驱动模型
- [ ] sysfs / proc / debugfs

### 3. 常用子系统
- [ ] GPIO / Pinctrl
- [ ] I2C / SPI 驱动框架
- [ ] 输入子系统（Input）
- [ ] 帧缓冲 / DRM 显示
- [ ] 网络驱动基础
- [ ] USB 驱动概览

### 4. 进阶
- [ ] DMA 与连续内存
- [ ] 电源管理（Runtime PM）
- [ ] 内核调试（printk、ftrace、kgdb）
- [ ] 内核模块编写与加载

## 笔记列表

（后续在此链接具体笔记）

## 相关模块

- [嵌入式基础](03-嵌入式基础/index.md)
- [硬件与 SoC](05-硬件与SoC/index.md)
- [工具链与调试](07-工具链与调试/index.md)
