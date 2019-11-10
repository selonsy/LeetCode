#题目描述
#输入一个字符串(不含空格),请寻找输入中包含的所有蛇形字符串
#蛇形字符串定义:
#1.蛇形字符串由连续字符对组成,其特点如下:
#1.1.字符对定义:字符对由同一字母的大写和小写组成(前大后小).如:Aa,Dd
#1.2.蛇形字符串中包含的字符对,必须是连续字母,并按照字母顺序排序.如:AaBbCc或OoPpQqRrSs
#2.从输入中寻找字符组成蛇形字符串(字符顺序不限),符合规则:
#2.1.每次寻找必须是最长的蛇形字符串
#2.2.使用过的字符不能重复使用
#例:输入SXXSIRAAaSs
#正确过程(粗体为寻找到的字符)
#Step1:【S】xx【srR】^AaSs->【RrSs】 (找到两对连续字符对:Ss,Rr.可以组成蛇形字符串.另,Ss后应该是Tt,但当前字串
#【S】xx【srR】^AaSs中不包含,所以当前蛇形字符串到Ss结束.本轮查找结果是RrSs.)