# Github Trends

Script is aimed to list 20 most trending repositories created within last 7 days.
Script prints these repositories urls sorted descending by stars with amount of open issues for each of repo. 

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.


# Code example
```
python github_trending.py  #alternatively try python3

https://github.com/ambv/black The uncompromising Python code formatter  | Open Issues: 15
https://github.com/iOS-Strikers/OCBarrage iOS 弹幕库 OCBarrage, 同时渲染5000条弹幕也不卡, 轻量, 可拓展, 高度自定义动画, 超高性能, 简单易上手; A barrage render-engine with high performance for iOS. At the same time, rendering 5000 barrages is also very smooth, lightweight, scalable, highly custom animation, ultra high performance, simple and easy to use!  | Open Issues: 0
https://github.com/normandipalo/faceID_beta An implementation of iPhone X's FaceID using face embeddings and siamese networks on RGBD images.  | Open Issues: 1
....
....
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
