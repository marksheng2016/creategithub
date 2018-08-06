#!/usr/bin/env python3

import sys
import csv #导入csv文件

#参数处理
class Args(object):
    def __init__(self):
        self.args = sys.argv[1:]
        for arg in self.args:
            if '-c' in arg:
                self.c = self.args[1]
            if '-d' in arg:
                self.d = self.args[3]
            if '-o' in arg:
                self.o = self.args[5]
    c = '' #配置文件路径
    d = '' #用户文件路径
    o = ''  #工资导出路径

#配置文件读取
class Config(object):
    def __init__(self):
        self.config = self._read_config()
    def _read_config(self):
        config = {}
        a = Args() #读取参数路径
        with open(a.c) as f:
            for line in f.readlines():
                if '=' in line:
                    l = line.split('=')
                    config[l[0].strip()] = float(l[1].strip())
                else:
                    continue
        return config

#用户文件读取
class UserData(object):
    def __init__(self):
        self.userdata = self._read_users_data()
    def _read_users_data(self):
        userdata = []
        a = Args() #读取参数路径
        with open(a.d) as f:
            userdata = list(csv.reader(f))
        return userdata

#计算工资
class ITC(object):
    #计算工资函数
    def calc(slef):
        ud = UserData() #创建读取用户信息对象
        cfg = Config() #创建读取配置信息对象
        config = cfg.config #读取配置
        jishu = config['YangLao'] + config['YiLiao'] + config['ShiYe'] + config['GongShang'] + config['ShengYu'] + config['GongJiJin'] #计算基数
        nu = [] #创建列表 用于返回值
        for ulines in ud.userdata: #循环读取用户信息
            gz = float(ulines[1]) #读取用户工资
            shebao = 0 #社保 0
            sd = 0 # 应纳税所得额
            se = 0 #应纳税额
            ngz = 0 #实际工资
            if gz > config['JiShuL'] and gz < config['JiShuH']: #社保缴费基数下限与上限之间的社保计算
                shebao = gz * jishu
            if gz < config['JiShuL']: #JiShuL为社保缴费基数的下限，即工资低于 JiShuL 的值的时候，需要按照 JiShuL 的数值乘以缴费比例来缴纳社保。
                shebao = config['JiShuL'] * jishu
            if gz > config['JiShuH']: #JiShuH为社保缴费基数的上限，即工资高于 JiShuH 的值的时候，需要按照 JiShuH 的数值乘以缴费比例缴纳社保
                shebao = config['JiShuH'] * jishu
            if gz <= 3500: #应纳税所得额计算 工资小于或等于3500 不减去3500 不然为负数了
                sd = gz - shebao
            else:  
                sd = gz - shebao - 3500 #应纳税所得额计算 工资大于3500
            if sd <= 1500:  #应纳税额计算 
                se = sd * 0.03 - 0
            elif sd <= 4500 and sd > 1500:
                se = sd * 0.1 - 105
            elif sd <= 9000 and sd > 4500:
                se = sd * 0.2 - 555
            elif sd <= 35000 and sd > 9000:
                se = sd * 0.25 - 1005
            elif sd <= 55000 and sd > 35000:
                se = sd * 0.30 - 2755
            elif sd <= 80000 and sd > 55000:
                se = sd * 0.35 - 5505
            else:
                se = sd * 0.45 - 13505
            ngz = gz - shebao - se #实际工资计算
            ulines.append("{:.2f}".format(shebao))
            ulines.append("{:.2f}".format(se))
            ulines.append("{:.2f}".format(ngz))
            nu.append(ulines)#添加到新的用户信息列表
        return nu
    #导出函数
    def export(self,default='csv'):
        result = self.calc()
        a = Args()
        with open(a.o,'w+') as f: #不添加'w+' 会报错 why?
            writer = csv.writer(f)
            writer.writerows(result)

if __name__ == '__main__':
    i = ITC() #创建计算对象
    i.export() #导出计算结果
