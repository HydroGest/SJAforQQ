# SJAforQQ

一个支持小码王社区作品SJA分析、作品相似度比对的QQ机器人。

本项目的姊妹项目：[木屋查QQ机器人](https://github.com/HydroGest/xmw-searchbot)

## 安装
本项目需要[Mirai](mamoe/mirai)以及[mirai-http-api](project-mirai/mirai-api-http)提供支持，请自行阅读[文档](https://github.com/mamoe/mirai/blob/dev/docs/ConsoleTerminal.md)进行配置。

本项目推荐使用Python3.6或Python3.7环境进行运行。

### 依赖

使用pip安装：

```shell
pip3 install yiri-mirai
pip3 install requests
pip3 install Beautifulsoup4
pip3 install urllib3
```
同时安装ASGI服务，只需要安装以下依赖中任意一个：
```shell
pip3 install uvicorn
# 或
pip3 install hypercorn
```

### 配置

进入`main.py`文件，修改第16行：
```python
bot=Mirai(
    qq=12345, # qq号
    adapter=WebSocketAdapter(
        verify_key='xxxxxx', # mirai-http-api 密钥
        host='localhost', # mirai-http-api 地址
        port=8088 # mirai-http-api 端口
    )
)
```
如果你不熟悉mirai-http-api，请阅读[mirai-http-api文档](https://github.com/project-mirai/mirai-api-http/blob/master/README.md)

### 运行

```shell
python3 main.pu
```
*请注意：结束程序QQ机器人将不会工作*

## 使用

在QQ群发送`/比对 <作品A ID或URL> <作品B ID或URL>`将会对作品A与B进行相似度比对；
发送`/SJA <作品 ID或URL>`对单个作品进行SJA分析。

## License
```
MIT License

Copyright (c) 2023 MarkChai

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
