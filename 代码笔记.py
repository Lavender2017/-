#coding=utf-8
# **********1、计算代码执行时间***********
import datetime
starttime = datetime.datetime.now()
endtime = datetime.datetime.now()
print starttime，endtime，(endtime - starttime)
# **********2、引用其他文件夹的文件***********
import sys
sys.path.append(r'文件所在路径')
from 文件名 import 类名
# **********3、pandas 去除一列中的重复行***********
import pandas as pd
df = pd.read_csv("/Users/br_2019/Desktop/test/sample-100000.csv")
data = df.os_type#取出其中一列
print data.drop_duplicates()
# **********4、定时执行任务***********
crontab -e
/usr/bin/python /opt/rongshu_data/wz/anti-cheating/test.py > /opt/rongshu_data/wz/anti-cheating/test.py.log 2>&1
查看定时任务状态ps -ef | grep predict.py 
终止定时任务 kill -9 37346
# **********5、切换用户***********
sudo su - hermesdata
端口冲突
sudo lsof -i:XXXX
# **********6、进入/退出Python虚拟环境***********
conda activate python2
conda deactivate