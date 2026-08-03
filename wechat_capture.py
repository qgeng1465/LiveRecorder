#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信视频号 取流辅助脚本（配合 DouyinLiveRecorder 的"自定义 m3u8 直链录制"）

原理：把本机伪装成一台"电视"，手机微信视频号直播点【投屏】时，通过
DLNA/Chromecast 协议截获真实 m3u8 直播地址，并自动写入 config/URL_config.ini。
DouyinLiveRecorder 下一轮循环（默认 300 秒）会识别为"视频号直播"并开始录制。

依赖：Python 3.10+；首次运行会自动安装外部工具 wechat-finder-dlna（GPL-3.0，
独立运行，不进入录制程序本体，不影响其体积与内存）。

使用步骤：
  1. 双击/运行本脚本
  2. 手机与电脑连同一 WiFi
  3. 打开微信视频号直播 -> 右上角【投屏】-> 选择本机设备（默认名 MAGI）
  4. 捕获到地址后脚本自动写入 URL_config.ini，关闭本窗口即可
"""
import os
import sys
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_DIR = os.path.join(SCRIPT_DIR, 'config')
URL_CONFIG = os.path.join(CONFIG_DIR, 'URL_config.ini')

try:
    from wechat_finder_dlna import capture
except ImportError:
    print('[i] 未安装 wechat-finder-dlna，正在通过 pip 安装（仅此一次）...')
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', 'wechat-finder-dlna'])
    except Exception as e:
        print(f'[!] 自动安装失败：{e}')
        print('[!] 请手动执行：  python -m pip install wechat-finder-dlna')
        sys.exit(1)
    try:
        from wechat_finder_dlna import capture
    except ImportError:
        print('[!] wechat-finder-dlna 导入失败，请检查 Python 环境。')
        sys.exit(1)


def add_to_url_config(url: str, name: str) -> None:
    os.makedirs(CONFIG_DIR, exist_ok=True)
    existing = ''
    if os.path.exists(URL_CONFIG):
        with open(URL_CONFIG, 'r', encoding='utf-8-sig') as f:
            existing = f.read()
    if url in existing:
        print(f'[i] 该地址已在 URL_config.ini 中（无需重复添加）。')
        return
    line = f'{url},主播: {name}\n'
    with open(URL_CONFIG, 'a', encoding='utf-8-sig') as f:
        f.write(line)
    print(f'[✓] 已写入 {URL_CONFIG}')
    print(f'    内容: {line.strip()}')


def main() -> None:
    default_name = '视频号主播'
    name = input(f'主播名字（直接回车默认 [{default_name}]）: ').strip() or default_name

    print()
    print('=' * 56)
    print('  本机正伪装成投屏设备，请勿关闭本窗口')
    print('  设备名: MAGI（可改源码中 capture(name=...)）')
    print('  ---------------------------------------------')
    print('  手机操作：')
    print('    1. 手机与电脑连同一 WiFi')
    print('    2. 打开微信视频号直播')
    print('    3. 点右上角【投屏】，选择设备 MAGI')
    print('  （列表没看到就等几秒或下拉刷新）')
    print('=' * 56)
    print()

    try:
        url = capture(name='MAGI')
    except KeyboardInterrupt:
        print('\n已取消。')
        sys.exit(0)
    except Exception as e:
        print(f'[!] 取流失败：{e}')
        print('[!] 请确认：手机和电脑在同一局域网；防火墙放行了 9090/9091 端口；')
        print('     视频号直播当前正在播出且允许投屏。')
        sys.exit(1)

    url = (url or '').strip()
    if not url:
        print('[!] 未捕获到有效直播地址。')
        sys.exit(1)

    print()
    print(f'[✓] 捕获到直播地址: {url}')
    add_to_url_config(url, name)
    print()
    print('完成。现在运行 python main.py（或按 README 启动），下一轮循环（默认约 300 秒）')
    print('会自动以"视频号直播"平台录制。')
    print('注意：该地址通常带时效签名，若录制中断或失效，重新运行本脚本再投屏一次即可。')


if __name__ == '__main__':
    main()
