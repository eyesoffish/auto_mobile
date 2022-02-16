#!/usr/bin/python
# -*- coding: utf-8 -*-
import uiautomator2 as u2

# d = u2.connect('10.10.105.9:7912') # connect to device
# print(d.info)
# ------- 横向滚动到最左/右侧
# d(scrollable=True).scroll.horiz.toBeginning()
# d(scrollable=True).scroll.horiz.toEnd()

# ------- 纵向滚动到最上/下
# d(scrollable=True).scroll.toEnd()
# d(scrollable=True).scroll.toBeginning()

#  返回
# d.swipe_ext("right",scale=0.9)
# d.swipe_ext("left",scale=0.9)
# d.swipe_ext("left",scale=0.9)

# d.swipe_ext("right")

# --------------- 监听弹窗
# btn = d(resourceId="com.tencent.qt.qtl:id/preference_imagebutton", text="退出登录(目生鱼)")
# btn.click()
# ctx = d.watch_context()
# ctx.when("取消").click()
# ctx.wait_stable() # 等待界面不在有弹窗了

# -------------- 自动搜索
# search = d(resourceId="com.tencent.qt.qtl:id/search_input")
# search.click()
# d.send_keys("你好")
# d.press('enter')


# ------------ 网络链接
# 手机和电脑同时连接到同一个wifi上
# 1、开启远程adb
# #开启远端adb,这一步需要手机通过USB连接到电脑
# adb tcpip 5555
# #结果如下：restarting in TCP mode port: 5555
# #然后断开USB
# adb connect 192.168.3.2:5555
# #其中192.168.3.2是手机的局域网IP地址
# adb devices
# 启动远程
# adb shell /data/local/tmp/atx-agent server
# #确认可以看到设备信息
# alias for u2.connect_wifi('10.0.0.1')
# d = u2.connect_wifi('10.10.105.9')
# search = d(resourceId="com.tencent.qt.qtl:id/search_input")
# search.click()
# d.send_keys("元宵节快乐")
# d.press('enter')
