# 🎬 LiveRecorder 多平台直播录制工具

基于 FFmpeg 的**多平台直播循环值守录制工具**，支持抖音、快手、虎牙、斗鱼、B站、Twitch、YouTube 等 50+ 平台，并新增了**微信视频号**录制支持。

本仓库由 [DouyinLiveRecorder](https://github.com/ihmily/DouyinLiveRecorder)（原作者 Hmily，MIT 协议）二次开发而来：**完整保留原版全部录制功能**，新增微信视频号录制、常驻 Node 签名优化，并精简了运行时体积。

> ⚠️ 本项目仅供学习交流。录制他人直播前请先获得授权，尊重原作者著作权与个人信息。

---

## ✨ 特性

- 🎯 **50+ 平台录制**：抖音 / TikTok / 快手 / 虎牙 / 斗鱼 / YY / B站 / 小红书 / Twitch / YouTube 等
- 📱 **微信视频号录制**（本版新增）：通过"投屏伪装"方式取流，半自动录制
- 🔁 **循环值守**：`URL_config.ini` 一行一个直播间，自动轮询开播、录制、断线重连
- 🎞️ **格式灵活**：TS / MP4 / FLV，支持分段录制与 TS 转 MP4
- 📊 **画质可选**：默认原画/蓝光，可逐直播间指定录制画质
- 🔔 **开播推送**：Bark / 邮件 / Telegram / 钉钉 / 微信 / ntfy 等
- ⚡ **低占用**：JS 签名走常驻 Node 进程（不再反复启动新进程），运行时已精简
- 🌍 **海外平台**：支持代理配置，TikTok / SOOP / Twitch 等可正常录制

---

## 🚀 快速开始

1. 运行 `DouyinLiveRecorder.exe`
2. 在 `config/URL_config.ini` 中填入直播间地址，一行一个（可选 `画质，地址` 指定清晰度；行首加 `#` 暂停该行）
3. 录制视频自动保存到 `downloads/平台名/主播名/`
4. 停止录制：Windows 双击 `StopRecording.vbs`，或录制界面 `Ctrl+C`

### 📱 微信视频号录制（本版新增）

视频号没有公开取流接口，直播地址是带时效签名的短链接。本版通过"投屏伪装"方式获取地址后自动录制：

1. 运行 `DouyinLiveRecorder.exe`
2. 双击 `启动视频号取流.bat`，输入主播名
3. 手机与电脑连**同一 WiFi**
4. 手机微信视频号直播 → 右上角【投屏】→ 选择设备 **MAGI**
5. 脚本捕获到地址后自动写入配置，程序下一轮循环（默认约 300 秒）自动按"视频号直播"平台录制

录到 `downloads/视频号直播/主播名/`。地址带时效签名，录制中断或失效时重跑取流脚本、再投屏一次即可。详细步骤见 [使用说明-视频号.txt](使用说明-视频号.txt)。

### ⚙️ 常见配置

- 录制画质：`config/config.ini` 全局设置；也可在地址前加 `超清，` 逐直播间指定
- 海外平台代理：`config/config.ini` 开启代理并填 `代理地址`，如 `127.0.0.1:7890`
- 推荐录制格式：`TS + 分段录制`（默认即 TS 转 MP4），避免中断导致文件损坏

---

## 😺 已支持平台

- [x] 抖音
- [x] **微信视频号**（本版新增，半自动）
- [x] TikTok
- [x] 快手
- [x] 虎牙
- [x] 斗鱼
- [x] YY
- [x] B站
- [x] 小红书
- [x] bigo
- [x] blued
- [x] SOOP（原 AfreecaTV）
- [x] 网易cc
- [x] 千度热播
- [x] PandaTV
- [x] 猫耳FM
- [x] Look直播
- [x] WinkTV
- [x] TTingLive（原 Flextv）
- [x] PopkonTV
- [x] TwitCasting
- [x] 百度直播
- [x] 微博直播
- [x] 酷狗直播
- [x] TwitchTV
- [x] LiveMe
- [x] 花椒直播
- [x] 流星直播
- [x] ShowRoom
- [x] Acfun
- [x] 映客直播
- [x] 音播直播
- [x] 知乎直播
- [x] CHZZK
- [x] 嗨秀直播
- [x] vv星球直播
- [x] 17Live
- [x] 浪Live
- [x] 畅聊直播
- [x] 飘飘直播
- [x] 六间房直播
- [x] 乐嗨直播
- [x] 花猫直播
- [x] Shopee
- [x] Youtube
- [x] 淘宝
- [x] 京东
- [x] Faceit
- [x] 咪咕
- [x] 连接直播
- [x] 来秀直播
- [x] Picarto

---

## 📁 项目结构

```
.
└── LiveRecorder/
    ├── DouyinLiveRecorder.exe   → 主程序（含视频号功能）
    ├── _internal/               → 程序运行依赖
    ├── ffmpeg/                  → 录制用 ffmpeg
    ├── node/                    → JS 签名运行环境（node.exe）
    ├── config/
    │   ├── config.ini           → 全局配置（画质/代理/推送等）
    │   └── URL_config.ini       → 要录制的直播间地址，一行一个
    ├── downloads/               → 录制视频保存目录（分平台/主播）
    ├── logs/                    → 运行日志
    ├── backup_config/           → 配置备份
    ├── wechat_capture.py        → 视频号取流脚本（首次运行自动安装依赖）
    ├── 启动视频号取流.bat        → 视频号取流入口
    ├── StopRecording.vbs        → Windows 一键停止录制
    ├── README.md / 使用说明.txt / 使用说明-视频号.txt
    ├── LICENSE
    └── 源码（可删除）/          → 修改后的完整源码（不需要可整体删除）
```

---

## 🎁 本构建说明

本版在 v4.0.7 上游基础上：

- **新增微信视频号录制**：`main.py` 自定义 m3u8/flv 分支新增"视频号直播"平台识别，保存到 `downloads/视频号直播/主播名/`
- **常驻 Node 优化**：PyExecJS 每次调用都会新起 Node 进程，本版改为每个 JS 文件一个常驻 Node 子进程（复用调用 ~3ms，原 ~79ms），降低 CPU/内存抖动。抖音 x-bogus 等签名输出与上游逐字一致
- **运行时精简**：移除未使用的 ffplay/ffprobe 与 Node 附带组件（npm/corepack），体积减小约 35MB

### 🧰 从源码构建（可选）

需要 Python >= 3.10，安装依赖后运行：

```bash
pip install -r requirements.txt
python main.py          # Linux 用 python3 main.py
```

打包为单文件夹版（Windows）：

```bash
python -m PyInstaller --onedir --name DouyinLiveRecorder \
  --add-data "src/javascript;src/javascript" --add-data "i18n;i18n" main.py
```

> 注意：PyInstaller 需在 .spec 中设置 `sys.setrecursionlimit(getrecursionlimit()*5)`，
> 并对系统 Python 已装的数据科学库（tensorflow/torch/numpy/scipy/pandas 等）做 excludes，
> 否则产物会膨胀到数 GB。JS 数据会进入 `_internal/src/javascript`，locale 进入 `_internal/i18n`。

---

## 🎨 直播间链接示例

```
抖音:
https://live.douyin.com/745964462470
https://v.douyin.com/iQFeBnt/
https://live.douyin.com/yall1102  （链接+抖音号）
https://v.douyin.com/CeiU5cbX  （主播主页地址）

TikTok:
https://www.tiktok.com/@pearlgaga88/live

快手:
https://live.kuaishou.com/u/yall1102

虎牙:
https://www.huya.com/52333

斗鱼:
https://www.douyu.com/3637778?dyshid=
https://www.douyu.com/topic/wzDBLS6?rid=4921614&dyshid=

YY:
https://www.yy.com/22490906/22490906

B站:
https://live.bilibili.com/320

小红书（直播间分享地址）:
http://xhslink.com/xpJpfM

bigo直播:
https://www.bigo.tv/cn/716418802

blued直播:
https://app.blued.cn/live?id=Mp6G2R

SOOP:
https://play.sooplive.co.kr/sw7love

网易cc:
https://cc.163.com/583946984

千度热播:
https://qiandurebo.com/web/video.php?roomnumber=33333

PandaTV:
https://www.pandalive.co.kr/live/play/bara0109

猫耳FM:
https://fm.missevan.com/live/868895007

Look直播:
https://look.163.com/live?id=65108820&position=3

WinkTV:
https://www.winktv.co.kr/live/play/anjer1004

FlexTV(TTinglive):
https://www.flextv.co.kr/channels/593127/live

PopkonTV:
https://www.popkontv.com/live/view?castId=wjfal007&partnerCode=P-00117

TwitCasting:
https://twitcasting.tv/c:uonq

百度直播:
https://live.baidu.com/m/media/pclive/pchome/live.html?room_id=9175031377&tab_category

微博直播:
https://weibo.com/l/wblive/p/show/1022:2321325026370190442592

酷狗直播:
https://fanxing2.kugou.com/50428671?refer=2177&sourceFrom=

TwitchTV:
https://www.twitch.tv/gamerbee

LiveMe:
https://www.liveme.com/zh/v/17141543493018047815/index.html

花椒直播:
https://www.huajiao.com/l/345096174

流星直播:
https://www.7u66.com/100960

ShowRoom:
https://www.showroom-live.com/room/profile?room_id=480206  （主播主页地址）

Acfun:
https://live.acfun.cn/live/179922

映客直播:
https://www.inke.cn/liveroom/index.html?uid=22954469&id=1720860391070904

音播直播:
https://live.ybw1666.com/800002949

知乎直播:
https://www.zhihu.com/people/ac3a467005c5d20381a82230101308e9 （主播主页地址）

CHZZK:
https://chzzk.naver.com/live/458f6ec20b034f49e0fc6d03921646d2

嗨秀直播:
https://www.haixiutv.com/6095106

VV星球直播:
https://h5webcdn-pro.vvxqiu.com//activity/videoShare/videoShare.html?h5Server=https://h5p.vvxqiu.com&roomId=LP115924473&platformId=vvstar

17Live:
https://17.live/en/live/6302408

浪Live:
https://www.lang.live/en-US/room/3349463

畅聊直播:
https://live.tlclw.com/106188

飘飘直播:
https://m.pp.weimipopo.com/live/preview.html?uid=91648673&anchorUid=91625862&app=plpl

六间房直播:
https://v.6.cn/634435

乐嗨直播:
https://www.lehaitv.com/8059096

花猫直播:
https://h.catshow168.com/live/preview.html?uid=19066357&anchorUid=18895331

Shopee:
https://sg.shp.ee/GmpXeuf?uid=1006401066&session=802458

Youtube:
https://www.youtube.com/watch?v=cS6zS5hi1w0

淘宝（需 cookie）:
https://tbzb.taobao.com/live?liveId=532359023188
https://m.tb.cn/h.TWp0HTd

京东:
https://3.cn/28MLBy-E

Faceit:
https://www.faceit.com/zh/players/Compl1/stream

连接直播:
https://show.lailianjie.com/10000258

咪咕直播:
https://www.miguvideo.com/p/live/120000541321

来秀直播:
https://www.imkktv.com/h5/share/video.html?uid=1845195&roomId=1710496

Picarto:
https://www.picarto.tv/cuteavalanche
```

---

## 📜 更新日志

### 本仓库（LiveRecorder）

- **2026-08** · 首个 fork 版本（基于上游 v4.0.7）
  - 新增微信视频号录制（投屏伪装取流，半自动）
  - JS 签名改为常驻 Node 进程，降低 CPU/内存占用
  - 精简运行时（移除 ffplay/ffprobe、npm 等），体积减小约 35MB
  - 完整保留上游全部录制功能

### 上游 DouyinLiveRecorder

<details><summary>点击展开（作者 Hmily 的更新历史，完整版见原仓库）</summary>

- 20251024
  - 修复抖音风控无法获取数据问题
  - 新增 soop.com 录制支持
  - 修复 bigo 录制
- 20250127
  - 新增淘宝、京东、faceit 直播录制
  - 修复小红书直播流录制以及转码问题
  - 修复畅聊、VV星球、flexTV 直播录制
  - 修复批量微信直播推送
  - 新增 email 发送 ssl 和 port 配置
  - 新增强制转 h264 配置
  - 更新 ffmpeg 版本
  - 重构包为异步函数
- 20241130
  - 新增 shopee、youtube 直播录制
  - 新增支持自定义 m3u8、flv 地址录制
  - 新增自定义执行脚本，支持 python、bat、bash 等
  - 修复 YY直播、花椒直播和小红书直播录制
- 20241030
  - 新增嗨秀直播、vv星球直播、17Live、浪Live、SOOP、畅聊直播、飘飘直播、六间房直播、乐嗨直播、花猫直播等 10 个平台
  - 修复小红书直播录制，支持作者主页地址
  - 新增 ntfy 消息推送
  - 修复 LiveMe、twitch 直播录制
  - 新增 Windows 一键停止录制 VB 脚本
- 20241005
  - 新增邮箱和 Bark 推送
  - 新增直播注释停止录制
  - 优化分段录制
- 20240928
  - 新增知乎直播、CHZZK 直播录制
- 20240903
  - 新增抖音双屏录制、音播直播录制
- 20240701
  - 修复虎牙 2 分钟断流；新增自定义推送内容
- 20240621
  - 新增 Acfun、ShowRoom 录制；修复斗鱼 60 帧、TikTok 解析等
- 20240427
  - 新增 LiveMe、花椒直播录制
- 20240425
  - 新增 TwitchTV 直播录制
- 20240424
  - 新增酷狗直播；修复斗鱼回放问题
- 20240423
  - 新增百度直播、微博直播
- 20240311
  - 修复海外平台录制 bug，增加画质选择
- 20240209
  - 优化 AfreecaTV 登录；修复小红书直播域名
- 20240129
  - 新增猫耳FM直播录制
- 20240127
  - 新增千度热播、PandaTV；新增 telegram 推送
- 20231210
  - 新增 AfreecaTV；修复分段录制
- 20231207
  - 新增 blued、直播结束推送
- 20231206
  - 新增 bigo 直播录制
- 20231203
  - 新增小红书直播录制（全网首发）
- 20230930
  - 抖音改从官方接口获取直播流；快手改官方接口
- 20230814
  - 新增 B站直播录制；在线播放 M3U8/FLV 网页
- 20230805
  - 新增虎牙直播录制
- 20230804
  - 新增快手直播录制；抖音 cookie 自动化获取
- 20230803
  - 新增 TikTok 直播录制

</details>

---

## 📄 开源许可

本项目使用 [MIT](LICENSE) 协议。

- **上游项目**：[DouyinLiveRecorder](https://github.com/ihmily/DouyinLiveRecorder)，原作者 **Hmily**，MIT 协议
- **本 fork 维护**：qgeng1465，Copyright (c) 2026

感谢 Hmily 的开源贡献。使用本项目时请遵守 MIT 协议条款，保留版权声明。
