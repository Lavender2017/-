#!/bin/bash
# 1、.sh给执行权限
chmod +x xxx.sh
# 2、字符串输出到文件中
echo "it is a test" > myfile
# 3、输出日期
echo `date`
start_time=$(date -v-1d +%Y-%m-%d)（mac版本）
start_time=$(date -d "-20 days" +%Y-%m-%d)（Linux版本）
# 4、使用Python的输出结果
all_result=$(python test.py 2>&1)
echo $all_result
输出样例：1 2 r t
result3=$(echo $all_result | cut -d';' -f3)(返回第三个输出结果)
echo $result3
# 5、shell数组一般以空格分隔，当数组元素中有空格时会影响结果需要重新定义分隔符
比如数组array中的元素为”select * from table“，”we“
OLD_IFS="$IFS"（存储旧的分隔符）
IFS=";"（用来重新定义分隔符为分号）
arr=($array)（加括号自动分隔）
echo ${arr[0]}

