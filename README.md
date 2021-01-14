# Luogu Auto Sign-in

洛谷自动打卡并返回打卡信息

## Install

需求 `python` 以及 `requests` 库

```
$ pip install requests
```

使用 git clone 下载到本地

```
& git clone https://github.com/TosakaUCW/Luogu-Auto-Sign-in.git
```

## Usage

在 `./luogu-auto-sign-in/` 下创建 `Cookies.txt` 并写入账号的 `Cookies`，支持多个账号打卡，每行一个 `Cookies`

For example :

```
UM_distinctid=xxx; __client_id=xxx; CNZZDATA5476811=xxx%xxx-xxx-%xxx%xxx; _uid=xxx
UM_distinctid=xxx; __client_id=xxx; CNZZDATA5476811=xxx%xxx-xxx-%xxx%xxx; _uid=xxx
UM_distinctid=xxx; __client_id=xxx; CNZZDATA5476811=xxx%xxx-xxx-%xxx%xxx; _uid=xxx
```

运行脚本

```
$ python main.py
```

## TODO

部署到 `github action` 实现云打卡（其实这才是一开始的目的，先暂时咕了，有空再学）

## License

[MIT © TosakaUCW](../LICENSE)