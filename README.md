<p align="center">
  <h1 align="center">🎬 LiveRecorder</h1>
  <p align="center"><strong>Multi-platform live stream recorder — record 50+ platforms 24/7, including WeChat Channels (视频号)</strong></p>

  <p align="center">
    <a href="https://github.com/qgeng1465/LiveRecorder/blob/main/README_CN.md"><strong>中文文档</strong></a> ·
    <a href="https://github.com/qgeng1465/LiveRecorder"><strong>English</strong></a>
  </p>

  <p align="center">
    <img src="https://img.shields.io/github/license/qgeng1465/LiveRecorder" alt="License">
    <img src="https://img.shields.io/badge/Python-3.10%2B-blue" alt="Python">
    <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS%20%7C%20Docker-lightgrey" alt="Platform">
    <img src="https://img.shields.io/github/stars/qgeng1465/LiveRecorder" alt="Stars">
    <img src="https://github.com/qgeng1465/LiveRecorder/actions/workflows/ci.yml/badge.svg" alt="CI">
    <img src="https://img.shields.io/github/last-commit/qgeng1465/LiveRecorder" alt="Last commit">
  </p>
</p>

<p align="center">
  <img src="assets/hero.svg" alt="LiveRecorder" width="100%">
</p>

**LiveRecorder** is an FFmpeg-based **24/7 live-stream recording tool**. Add a room URL to the config file and the program automatically polls for live status, records, reconnects after disconnects, segments long streams, and sends you notifications when a streamer goes live. It supports **50+ platforms** — Douyin/TikTok, Kuaishou, Huya, Douyu, Bilibili, Twitch, YouTube and more — plus **WeChat Channels (视频号)**, a feature the upstream project does not have.

This project is a fork of [DouyinLiveRecorder](https://github.com/ihmily/DouyinLiveRecorder) (by Hmily, MIT licensed): **all of the original recording features are fully preserved**, with the following additions:

- 📱 **WeChat Channels recording** — via a "cast-impersonation" approach (semi-automatic)
- ⚡ **Persistent Node.js runtime** for JS signing — no more spawning a new process per call (much lower CPU/memory usage)
- 🪶 **Slimmer runtime** — unused ffmpeg components and Node modules removed

> ⚠️ For learning and personal use only. Before recording someone's live stream, please get their permission and respect the streamer's copyright and personal information.

> ⭐ If LiveRecorder is useful to you, please give it a **star** — it helps other people discover the project. Issues and PRs are always welcome!

---

## ✨ Features

- 🎯 **50+ platforms**: Douyin / TikTok / Kuaishou / Huya / Douyu / YY / Bilibili / Xiaohongshu (RED) / Twitch / YouTube / WeChat Channels and more
- 📱 **WeChat Channels recording** (new in this fork): capture the stream via "cast impersonation", semi-automatic
- 🔁 **24/7 guardian loop**: one room per line in `URL_config.ini`, auto-poll, record, reconnect
- 🎞️ **Flexible formats**: TS / MP4 / FLV, with segment recording and automatic TS→MP4 conversion
- 📊 **Per-room quality**: default original/Blu-ray quality, or set quality per room
- 🔔 **Go-live notifications**: Bark / email / Telegram / DingTalk / WeChat / ntfy / PushPlus
- ⚡ **Low footprint**: JS signing runs on a persistent Node process; runtime trimmed
- 🌍 **Proxy support**: TikTok / SOOP / Twitch and other overseas platforms work behind a proxy
- 📦 **Cross-platform**: Windows / Linux / macOS / Docker

---

## 🐱 Supported Platforms

- [x] Douyin
- [x] **WeChat Channels (视频号)** — new in this fork, semi-automatic
- [x] TikTok
- [x] Kuaishou
- [x] Huya
- [x] Douyu
- [x] YY
- [x] Bilibili
- [x] Xiaohongshu (RED)
- [x] bigo
- [x] blued
- [x] SOOP (formerly AfreecaTV)
- [x] NetEase CC
- [x] Qiandu Rebo
- [x] PandaTV
- [x] Missevan FM
- [x] Look
- [x] WinkTV
- [x] TTingLive (formerly FlexTV)
- [x] PopkonTV
- [x] TwitCasting
- [x] Baidu Live
- [x] Weibo Live
- [x] Kugou
- [x] TwitchTV
- [x] LiveMe
- [x] Huajiao
- [x] Liuxing
- [x] ShowRoom
- [x] Acfun
- [x] Inke
- [x] Yinbo
- [x] Zhihu Live
- [x] CHZZK
- [x] Haixiu
- [x] VV Planet
- [x] 17Live
- [x] Lang Live
- [x] Changliao
- [x] PiaoPiao
- [x] 6.cn
- [x] LeHai
- [x] HuaMao
- [x] Shopee
- [x] YouTube
- [x] Taobao
- [x] JD
- [x] Faceit
- [x] Migu
- [x] Lianjie
- [x] LaiXiu
- [x] Picarto

---

## 📌 Requirements

| Dependency | Requirement | Notes |
|---|---|---|
| **Python** | **3.10 or higher** | Required (code uses `str \| None` and other new syntax) |
| ffmpeg | auto-installed | Detected and downloaded on first run; Windows auto-download, macOS via Homebrew, Linux via `yum`/`apt` |
| Node.js | auto-installed | Used for JS signing (Douyin etc.); detected and downloaded on first run |

> If auto-download fails (e.g. due to network issues), install ffmpeg and Node.js yourself and add them to `PATH` — the program will detect them.

---

## 🚀 Quick Start

### Install & run (Windows / Linux / macOS)

```bash
git clone https://github.com/qgeng1465/LiveRecorder.git
cd LiveRecorder
pip install -r requirements.txt
python main.py          # use python3 on Linux/macOS if needed
```

> **In mainland China?** pip may fail to reach PyPI. Use a mirror:
> ```bash
> pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
> ```

On the **first run**, the program automatically:

1. Checks for ffmpeg and Node.js — downloads and installs them if missing
2. Generates `config/config.ini` (auto-fills any missing keys)
3. If `config/URL_config.ini` is empty, prompts you to enter your first room URL

**Stop recording**: press `Ctrl+C`. On Windows you can also double-click `StopRecording.vbs`.

### Docker

```bash
docker build -t liverecorder .
docker run -it --name liverecorder \
  -v $(pwd)/config:/app/config \
  -v $(pwd)/downloads:/app/downloads \
  liverecorder
```

Or with docker-compose (builds from this repo's `Dockerfile`):

```bash
docker compose up -d
```

---

## ⚙️ Configuration

The program reads two config files, both in `config/`:

### 1. `config/URL_config.ini` — which rooms to record

One room URL per line. Rules (verified from the actual code):

| Syntax | Meaning |
|---|---|
| `https://live.douyin.com/xxx` | Record with the default quality |
| `超清，https://live.douyin.com/xxx` | Set the quality for this room only |
| `https://xxx.m3u8` / `https://xxx.flv` | Record a custom stream URL directly |
| `https://xxx，主播: 名字` | Custom streamer name for the saved folder (WeChat Channels format) |
| Line starting with `#` | Pause this line — won't be recorded |

- Both English comma `,` and Chinese comma `，` are accepted as separators — you can mix them
- Quality values: `原画` (original) `蓝光` (Blu-ray) `超清` (ultra HD) `高清` (HD) `标清` (SD) `流畅` (smooth)
- Each line can set its own quality; leave it blank to use the global default
- Example URLs at the bottom of this document

### 2. `config/config.ini` — global settings

The program auto-fills any missing sections/keys. **All yes/no items only accept `是` (yes) or `否` (no).**

#### [录制设置] (Recording Settings)

> The keys are the Chinese strings shown below — copy them exactly as they appear in the generated `config.ini`.

| Key (as in config.ini) | Description | Default |
|---|---|---|
| `language(zh_cn/en)` | UI language | `zh_cn` |
| `是否跳过代理检测(是/否)` | Set to `是` to skip system-proxy detection on startup (faster start) | `否` |
| `直播保存路径(不填则默认)` | Root save directory; leave blank for `downloads/` | blank |
| `保存文件夹是否以作者区分` | Create a subfolder per streamer | `是` |
| `保存文件夹是否以时间区分` | Create a subfolder per date | `否` |
| `保存文件夹是否以标题区分` | Create a subfolder per stream title | `否` |
| `保存文件名是否包含标题` | Include the stream title in the file name | `否` |
| `是否去除名称中的表情符号` | Strip emoji from names (avoids illegal Windows file names) | `是` |
| `视频保存格式ts\|mkv\|flv\|mp4\|mp3音频\|m4a音频` | Container format: `ts` / `mkv` / `flv` / `mp4` / `mp3音频` / `m4a音频` | `ts` |
| `原画\|超清\|高清\|标清\|流畅` | Global default quality (can be overridden per room in URL_config.ini) | `原画` |
| `是否使用代理ip(是/否)` | Enable proxy | `是` |
| `代理地址` | Proxy address, e.g. `127.0.0.1:7890` or `http://127.0.0.1:7890` | blank |
| `同一时间访问网络的线程数` | Concurrent parse/request threads | `3` |
| `循环时间(秒)` | Interval between live-status polls | `300` |
| `排队读取网址时间(秒)` | Interval for processing the URL list | `0` |
| `是否显示循环秒数` | Show the countdown to the next loop in the terminal | `否` |
| `是否显示直播源地址` | Print the stream URL in the terminal | `否` |
| `分段录制是否开启` | Segment long streams by time | `是` |
| `是否强制启用https录制` | Force HTTPS for pulling streams | `否` |
| `录制空间剩余阈值(gb)` | Stop recording when free disk space (GB) drops below this | `1.0` |
| `视频分段时间(秒)` | Length of each segment | `1800` |
| `录制完成后自动转为mp4格式` | Auto-convert to MP4 after recording | `是` |
| `mp4格式重新编码为h264` | Re-encode to h264 when converting (better compatibility) | `否` |
| `追加格式后删除原文件` | Delete intermediate files after conversion | `是` |
| `生成时间字幕文件` | Generate a timed subtitle file | `否` |
| `是否录制完成后执行自定义脚本` | Run a custom script after recording | `否` |
| `自定义脚本执行命令` | Script command (python / bat / bash ...) | blank |
| `使用代理录制的平台(逗号分隔)` | Platforms forced through the proxy | `tiktok, sooplive, ...` |
| `额外使用代理录制的平台(逗号分隔)` | Extra platforms on top of the above | blank |

#### [推送配置] (Push Notifications)

`直播状态推送渠道` (push channels) supports **multiple selection** — separate them with commas, e.g. `bark,tg` or `bark,tg,微信` (case-insensitive). Available channels: `微信` (WeChat) `钉钉` (DingTalk) `邮箱` (email) `TG` (Telegram) `BARK` `NTFY` `PUSHPLUS`.

| Key (as in config.ini) | Description |
|---|---|
| `直播状态推送渠道` | Push channels, e.g. `bark,tg` |
| `钉钉推送接口链接` | DingTalk bot Webhook URL |
| `微信推送接口链接` | WeChat (Server Chan etc.) push URL |
| `bark推送接口链接` | Bark URL, e.g. `https://api.day.app/your-key` |
| `bark推送中断级别` | `active` / `timeSensitive` / `passive` |
| `bark推送铃声` | Bark ringtone name; blank = default |
| `钉钉通知@对象(填手机号)` | DingTalk @ a person by phone number |
| `钉钉通知@全体(是/否)` | DingTalk @ everyone |
| `tgapi令牌` | Telegram Bot Token |
| `tg聊天id(个人或者群组id)` | Telegram chat id to receive pushes |
| `smtp邮件服务器` | SMTP server, e.g. `smtp.qq.com` |
| `是否使用SMTP服务SSL加密(是/否)` | Enable SMTP SSL |
| `SMTP邮件服务器端口` | e.g. `465` (SSL) / `587` (STARTTLS) |
| `邮箱登录账号` | Sender email account |
| `发件人密码(授权码)` | SMTP authorization code (**not** the login password) |
| `发件人邮箱` | Sender email address |
| `发件人显示昵称` | Display name shown to recipients |
| `收件人邮箱` | Recipient email |
| `ntfy推送地址` | Default `https://ntfy.sh/your-topic` |
| `ntfy推送标签` | ntfy tag (emoji) |
| `ntfy推送邮箱` | Attach an email account to the ntfy topic |
| `pushplus推送token` | PushPlus WeChat push token |
| `自定义推送标题` | Push message title template |
| `自定义开播推送内容` | Go-live push content template |
| `自定义关播推送内容` | Stream-end push content template |
| `只推送通知不录制(是/否)` | Monitor & notify only, don't record | 
| `直播推送检测频率(秒)` | Notification monitor interval | `1800` |
| `开播推送开启(是/否)` | Go-live push switch | `是` |
| `关播推送开启(是/否)` | Stream-end push switch | `否` |

#### [Cookie]

| Key | Description |
|---|---|
| `抖音cookie` | **Required for recording Douyin** (see how to get it below) |
| other platform `xxx_cookie` | Only needed when that platform requires login state |

#### [Authorization]

| Key | Description |
|---|---|
| `popkontv_token` | PopkonTV login token |

#### [账号密码] (Accounts & Passwords)

| Key | Description |
|---|---|
| `sooplive账号` / `sooplive密码` | SOOP (formerly AfreecaTV) login |
| `flextv账号` / `flextv密码` | FlexTV login |
| `popkontv账号` / `partner_code` / `popkontv密码` | PopkonTV login & channel code |
| `twitcasting账号类型` / `twitcasting账号` / `twitcasting密码` | TwitCasting login (type `normal` / `rss` ...) |

### 3. Getting your Douyin cookie

Recording Douyin requires a login cookie:

1. Log in at https://www.douyin.com in your browser
2. Press `F12` to open DevTools → `Network` tab
3. Reload the page, click any request, and find the `Cookie:` line under `Request Headers`
4. Copy the **entire value** after `Cookie:` into `config/config.ini` → `[Cookie]` → `抖音cookie =`
5. Save and restart the program

> Cookies expire — just fetch a new one when it stops working. A cookie is sensitive personal information — **never commit it to a public repository**.

### 4. Proxy configuration

- In `[录制设置]`, set `是否使用代理ip` to `是` and `代理地址` to e.g. `127.0.0.1:7890`
- Overseas platforms (TikTok / SOOP / Twitch ...) are already in the `使用代理录制的平台` list; if your proxy rules can't distinguish them, add platforms to `额外使用代理录制的平台`
- On startup the program auto-detects the system proxy (set `是否跳过代理检测` to `是` to skip)

---

## 📱 WeChat Channels (视频号) Recording — new in this fork

WeChat Channels has **no public streaming API**, and live addresses are short links with time-limited signatures. This fork obtains the address via "cast impersonation" and then records automatically:

1. Start the recorder: `python main.py`
2. **Windows**: double-click `启动视频号取流.bat` · **Linux/macOS**: run `python wechat_capture.py`, then enter the streamer's name
3. Connect your phone and PC to the **same Wi-Fi**
4. On your phone, open the WeChat Channels live stream → tap **投屏** (Cast) at the top-right → choose the **MAGI** device
5. The script captures the address and writes it to `config/URL_config.ini`; the program picks it up on the next loop (~300s by default) and records it under the `视频号直播` platform

Recordings are saved to `downloads/视频号直播/主播名/`. Because addresses carry time-limited signatures, if a recording breaks or expires, just re-run the capture script and cast once more.

> On first run the capture script auto-installs `wechat-finder-dlna` (GPL-3.0, a standalone tool used only to capture the address — it does not enter the recorder's runtime). If auto-install fails, run `python -m pip install wechat-finder-dlna` manually.

---

## 🧰 Building a single-folder release from source (optional)

Requires Python >= 3.10 and PyInstaller:

```bash
pip install pyinstaller
python -m PyInstaller --onedir --name LiveRecorder \
  --add-data "src/javascript;src/javascript" --add-data "i18n;i18n" main.py
```

> **Notes**:
> - Add `sys.setrecursionlimit(getrecursionlimit() * 5)` to the `.spec`, otherwise packaging fails with `RecursionError`
> - If your system Python has data-science libraries installed (tensorflow/torch/numpy/scipy/pandas...), exclude them in `Analysis.excludes` or the output will bloat to several GB
> - After packaging, place `config/` next to the exe

---

## ❓ FAQ

**Q: It says ffmpeg / Node.js is missing?**
Auto-download usually fails because of network issues. Install ffmpeg and Node.js yourself and add them to `PATH`:
- ffmpeg: `ffmpeg.org/download.html` or `apt install ffmpeg` / `brew install ffmpeg`
- Node.js: `nodejs.org` or `brew install node`

**Q: What Python version is required?**
**3.10 or higher**. Older versions will throw syntax errors.

**Q: Douyin recording fails?**
1. Check that `抖音cookie` under `[Cookie]` is filled in and not expired
2. Check your network proxy (some networks need a proxy to reach Douyin)

**Q: No audio / format problems?**
Use the default `ts` format (auto-converts to MP4 after recording). `ts` segment recording is the most fault-tolerant against stream drops. Directly remuxing to `flv`/`mp4` can produce no audio or corrupted files on some platforms.

**Q: The WeChat Channels address expired?**
Channel addresses carry time-limited signatures. Re-run the capture script and cast once more — no need to restart the main program.

**Q: Do I need to restart after editing config?**
Changes to `config/URL_config.ini` take effect on the next loop automatically; changes to `config/config.ini` are best applied after a restart.

**Q: Where are recordings saved?**
By default `downloads/平台名/主播名/`; change it with `直播保存路径` under `[录制设置]`.

---

## 📁 Project Structure

```
LiveRecorder/
├── main.py                 → Main program entry
├── wechat_capture.py       → WeChat Channels capture script (optional, semi-auto)
├── 启动视频号取流.bat        → Windows one-click launcher for the capture script
├── StopRecording.vbs       → Windows one-click stop-recording script
├── ffmpeg_install.py       → ffmpeg auto-detect / install
├── msg_push.py             → Notifications (WeChat/DingTalk/tg/email/bark/ntfy/pushplus)
├── i18n.py / i18n/         → Localization
├── src/
│   ├── spider.py           → Stream resolution for 50+ platforms
│   ├── stream.py           → Recording logic
│   ├── room.py             → Douyin room info
│   ├── utils.py            → Persistent Node.js signing executor
│   ├── initializer.py      → Node.js auto-detect / install
│   ├── javascript/         → JS signing scripts (x-bogus etc.)
│   └── ...
├── config/
│   ├── config.ini          → Global config (quality/proxy/push/cookie)
│   └── URL_config.ini      → Room URLs to record, one per line
├── downloads/              → Recorded videos (auto-created)
├── Dockerfile / docker-compose.yaml
├── requirements.txt
└── LICENSE
```

---

## 🎨 Example Room URLs

```
Douyin:
https://live.douyin.com/745964462470
https://v.douyin.com/iQFeBnt/
https://live.douyin.com/yall1102      (URL + Douyin ID)
https://v.douyin.com/CeiU5cbX         (streamer profile page)

TikTok:
https://www.tiktok.com/@pearlgaga88/live

Kuaishou:
https://live.kuaishou.com/u/yall1102

Huya:
https://www.huya.com/52333

Douyu:
https://www.douyu.com/3637778?dyshid=
https://www.douyu.com/topic/wzDBLS6?rid=4921614&dyshid=

YY:
https://www.yy.com/22490906/22490906

Bilibili:
https://live.bilibili.com/320

Xiaohongshu (share link):
http://xhslink.com/xpJpfM

bigo:
https://www.bigo.tv/cn/716418802

blued:
https://app.blued.cn/live?id=Mp6G2R

SOOP:
https://play.sooplive.co.kr/sw7love

NetEase CC:
https://cc.163.com/583946984

Qiandu Rebo:
https://qiandurebo.com/web/video.php?roomnumber=33333

PandaTV:
https://www.pandalive.co.kr/live/play/bara0109

Missevan FM:
https://fm.missevan.com/live/868895007

Look:
https://look.163.com/live?id=65108820&position=3

WinkTV:
https://www.winktv.co.kr/live/play/anjer1004

FlexTV (TTinglive):
https://www.flextv.co.kr/channels/593127/live

PopkonTV:
https://www.popkontv.com/live/view?castId=wjfal007&partnerCode=P-00117

TwitCasting:
https://twitcasting.tv/c:uonq

Baidu Live:
https://live.baidu.com/m/media/pclive/pchome/live.html?room_id=9175031377&tab_category

Weibo Live:
https://weibo.com/l/wblive/p/show/1022:2321325026370190442592

Kugou:
https://fanxing2.kugou.com/50428671?refer=2177&sourceFrom=

TwitchTV:
https://www.twitch.tv/gamerbee

LiveMe:
https://www.liveme.com/zh/v/17141543493018047815/index.html

Huajiao:
https://www.huajiao.com/l/345096174

Liuxing:
https://www.7u66.com/100960

ShowRoom:
https://www.showroom-live.com/room/profile?room_id=480206    (streamer profile page)

Acfun:
https://live.acfun.cn/live/179922

Inke:
https://www.inke.cn/liveroom/index.html?uid=22954469&id=1720860391070904

Yinbo:
https://live.ybw1666.com/800002949

Zhihu Live:
https://www.zhihu.com/people/ac3a467005c5d20381a82230101308e9    (streamer profile page)

CHZZK:
https://chzzk.naver.com/live/458f6ec20b034f49e0fc6d03921646d2

Haixiu:
https://www.haixiutv.com/6095106

VV Planet:
https://h5webcdn-pro.vvxqiu.com//activity/videoShare/videoShare.html?h5Server=https://h5p.vvxqiu.com&roomId=LP115924473&platformId=vvstar

17Live:
https://17.live/en/live/6302408

Lang Live:
https://www.lang.live/en-US/room/3349463

Changliao:
https://live.tlclw.com/106188

PiaoPiao:
https://m.pp.weimipopo.com/live/preview.html?uid=91648673&anchorUid=91625862&app=plpl

6.cn:
https://v.6.cn/634435

LeHai:
https://www.lehaitv.com/8059096

HuaMao:
https://h.catshow168.com/live/preview.html?uid=19066357&anchorUid=18895331

Shopee:
https://sg.shp.ee/GmpXeuf?uid=1006401066&session=802458

YouTube:
https://www.youtube.com/watch?v=cS6zS5hi1w0

Taobao (cookie required):
https://tbzb.taobao.com/live?liveId=532359023188
https://m.tb.cn/h.TWp0HTd

JD:
https://3.cn/28MLBy-E

Faceit:
https://www.faceit.com/zh/players/Compl1/stream

Lianjie:
https://show.lailianjie.com/10000258

Migu:
https://www.miguvideo.com/p/live/120000541321

LaiXiu:
https://www.imkktv.com/h5/share/video.html?uid=1845195&roomId=1710496

Picarto:
https://www.picarto.tv/cuteavalanche
```

---

## 📜 Changelog

### This fork (LiveRecorder)

- **2026-08** · Initial fork (based on upstream v4.0.7)
  - Added WeChat Channels recording (cast-impersonation capture, semi-automatic)
  - JS signing moved to a persistent Node.js process — lower CPU/memory usage
  - Slimmed the runtime (removed ffplay/ffprobe, npm, etc.) — ~35 MB smaller
  - All upstream recording features fully preserved

### Upstream DouyinLiveRecorder

See the [original repository](https://github.com/ihmily/DouyinLiveRecorder) for the full history by Hmily.

---

## 📄 License

This project is released under the [MIT](LICENSE) license.

- **Upstream**: [DouyinLiveRecorder](https://github.com/ihmily/DouyinLiveRecorder), by **Hmily**, MIT licensed
- **This fork**: maintained by qgeng1465, Copyright (c) 2026

Thanks to Hmily for the original work. When using this project, please comply with the MIT license and retain the copyright notice.
