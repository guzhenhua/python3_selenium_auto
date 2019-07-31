# python3_selenium_auto

1.安装Pillow包报错：  Could not find a version that satisfies the requirement Pillow (from versions: )
No matching distribution found for Pillow

解决办法如下：

查了一下，首先是因为 PIL 已经被 Pillow 所替代了，但是使用命令 pip install Pillow 仍旧不行，这个时候就需要我们手动去下载第三方库然后安装。

首先，去 https://www.lfd.uci.edu/~gohlke/pythonlibs/找到需要的库文件，比如 PIL

![1564588133357](C:\Users\顾贞华\AppData\Roaming\Typora\typora-user-images\1564588133357.png)



然后，使用命令 pip install path\文件名  安装即可

![img](https://upload-images.jianshu.io/upload_images/3012096-fc46139e0f599a54.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/800/format/webp)

path是指下载的.whl文件存放的路径

详细教程**PIL、Pillow安装使用方法**：https://blog.csdn.net/mp624183768/article/details/81023819





图片识别APi：https://www.showapi.com/