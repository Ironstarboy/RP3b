# 项目介绍。
智能系统中的嵌入式应用，使用raspberry3b,alphabot2小车

实现了自动避障。循迹和遥控的代码也已编写完成。

# 运行方法

下载该项目

然后进入car目录，在命令行中输入`python3 parse.py`即可。默认初始速度是10，蜂鸣器开启，彩灯关闭。

如果想修改默认参数，可以输入命令`python3 parse.py -s 15 -b 0 -l 1`

-s代表参数--speed，速度可以是0-100的任何数字，比如这里是15。建议速度不要太高，因为代码设置的障碍检测频率并不是太高。

-b 代表蜂鸣器Buzzer,0代表开启。默认是1，即开启。

-l 是彩灯LED，1代表开启。默认是0，即关闭。

# 视频演示

<iframe src="//player.bilibili.com/player.html?aid=636389729&bvid=BV14b4y177gK&cid=505585171&page=1" width="700px"  height="500px" runat="server"></iframe>





[偶然发现的大佬源码](https://github.com/XPengZhao/rpi-alphabot2)

