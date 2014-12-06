# -*- coding:utf-8 -*-
'''
  author: songboyu
  modify: 2014-12-07
  summary:拼音流分割

  定义一个拼音组合的字典,以拼音首字母为键值，以该字母的拼音组合元组为值，还包括一些常见的标点符号
'''
def pinyin_split(pinyin):
    '''
    分割函数
    @param pinyin:  拼音串 str
    @return:        分割后的拼音列表 list
    '''
    pyzhDict = {
                'a':('a', 'ai', 'an', 'ang', 'ao'),
                'b':('ba', 'bai', 'ban', 'bang', 'bao',
                     'bei', 'ben', 'beng', 'bi', 'bian', 'biao', 'bie', 'bin', 'bing', 'bo', 'bu'),
                'c':('ca', 'cai', 'can', 'cang', 'cao', 'ce', 'ceng', 'cha', 'chai',
                     'chan', 'chang', 'chao', 'che', 'chen', 'cheng', 'chi', 'chong', 'chou', 'chu',
                     'chuai', 'chuan', 'chuang', 'chui', 'chun', 'chuo', 'ci', 'cong', 'cou', 'cu',
                     'cuan', 'cui', 'cun', 'cuo'),
                'd':('da', 'dai', 'dan', 'dang', 'dao', 'de',
                     'deng', 'di', 'dian', 'diao', 'die', 'ding', 'diu',
                     'dong', 'dou', 'du', 'duan', 'dui', 'dun', 'duo','dia'),
                'e':('e', 'en', 'er'),
                'f':('fa', 'fan', 'fang', 'fei', 'fen', 'feng', 'fu', 'fou'),
                'g':('ga', 'gai', 'gan', 'gang', 'gao', 'ge', 'gen', 'geng',
                     'gong', 'gou', 'gu', 'gua', 'guai', 'guan', 'guang', 'gui', 'gun', 'guo'),
                'h':('ha', 'hai', 'han', 'hang', 'hao', 'he',
                     'hei', 'hen', 'heng', 'hong', 'hou', 'hu',
                     'hua', 'huai', 'huan', 'huang', 'hui', 'hun', 'huo'),
                'i':(),
                'j':('ji', 'jia', 'jian', 'jiang', 'qiao', 'jiao', 'jie', 'jin', 'jing', 'jiong',
                     'jiu', 'ju', 'juan', 'jue', 'jun','jv'),
                'k':('ka', 'kai', 'kan', 'kang', 'kao', 'ke', 'ken', 'keng', 'kong', 'kou', 'ku', 'kua', 'kuai',
                     'kuan', 'kuang', 'kui', 'kun', 'kuo'),
                'l':('la', 'lai', 'lan', 'lang', 'lao',
                     'le', 'lei', 'leng', 'li', 'lia', 'lian', 'liang', 'liao', 'lie', 'lin',
                     'ling', 'liu', 'long', 'lou', 'lu', 'luan', 'lue', 'lun', 'luo','lv'),
                'm':('ma', 'mai', 'man', 'mang', 'mao', 'me', 'mei', 'men', 'meng', 'mi', 'mian',
                     'miao', 'mie', 'min', 'ming', 'miu', 'mo', 'mou', 'mu'),
                'n':('na', 'nai', 'nan', 'nang', 'nao', 'ne', 'nei', 'nen', 'neng', 'ni', 'nian', 'niang',
                     'niao', 'nie', 'nin', 'ning', 'niu', 'nong', 'nu', 'nuan', 'nue', 'nuo','nv'),
                'o':('o', 'ou'),
                'p':('pa', 'pai', 'pan', 'pang', 'pao', 'pei', 'pen',
                     'peng', 'pi', 'pian', 'piao', 'pie', 'pin', 'ping', 'po', 'pou', 'pu'),
                'q':('qi', 'qia', 'qian', 'qiang', 'qie', 'qin', 'qing', 'qiong', 'qiu', 'qu',
                     'quan', 'que', 'qun','qv'),
                'r':('ran', 'rang', 'rao', 're', 'ren', 'reng', 'ri',
                     'rong', 'rou', 'ru', 'ruan', 'rui', 'run', 'ruo'),
                's':('sa', 'sai', 'san',
                     'sang', 'sao', 'se', 'sen', 'seng', 'sha', 'shai', 'shan', 'shang', 'shao',
                     'she', 'shen', 'sheng', 'shi', 'shou', 'shu', 'shua', 'shuai', 'shuan', 'shuang',
                     'shui', 'shun', 'shuo', 'si', 'song', 'sou', 'su', 'suan', 'sui', 'sun', 'suo'),
                't':('ta', 'tai', 'tan', 'tang', 'tao', 'te', 'teng', 'ti', 'tian',
                     'tiao', 'tie', 'ting', 'tong', 'tou', 'tu', 'tuan', 'tui', 'tun', 'tuo'),
                'u':(),
                'v':(),
                'w':('wa', 'wai', 'wan', 'wang', 'wei', 'wen', 'weng', 'wo', 'wu'),
                'x':('xi', 'xia', 'xian', 'xiang', 'xiao', 'xie', 'xin', 'xing', 'xiong', 'xiu', 'xu',
                     'xuan', 'xue', 'xun','xv'),
                'y':('ya', 'yan', 'yang','yao', 'ye', 'yi', 'yin', 'ying',
                     'yo', 'yong', 'you', 'yu', 'yuan', 'yue', 'yun'),
                'z':('za', 'zai', 'zan',
                     'zang', 'zao', 'ze', 'zei', 'zen', 'zeng', 'zha', 'zhai', 'zhan', 'zhang',
                     'zhao', 'zhe', 'zhen', 'zheng', 'zhi', 'zhong', 'zhou', 'zhu', 'zhua', 'zhuai',
                     'zhuan', 'zhuang', 'zhui', 'zhun', 'zhuo', 'zi', 'zong', 'zou', 'zu', 'zuan',
                     'zui', 'zun', 'zuo'),
                ' ':(),
                '\n':(),
                ',':(),
                '.':(),
                '\t':(),
                '?':(),
                '!':(),
                ';':(),
                ':':(),
                '"':(),
                'special':('', 'ei', 'm', 'n', 'dia', 'cen', 'nou',
                           'jv', 'qv', 'xv', 'lv', 'nv')
              }

    resultList = []                                    #结果列表
    begin = 0
    source = pinyin
    sourceLen = len(source)                            #source长度

    while begin < sourceLen:                           #字符处理直到最后一个字符为止
        firstLetter = source[begin]                    #拼音首字母
        step = 1
        temp = source[begin]
        for i in range(6):                             #此循环表示拼音音节最长为6个字符，从首字母开始往后取字符数依次加一，最后加到6个字符为止
            if begin + i + 1 > sourceLen:              #最后一个拼音越界
                break
            piece = source[begin:begin + i + 1]        #在source中切片字符串，最长6个字符
            if piece in pyzhDict[firstLetter]:         #比较切片字符串与拼音组合字典中该首字母的所有音节，看是否匹配，若匹配则将其赋值给temp，
                temp = piece                           #同时step变化,这里包含输入错误的情况，如该首字母找不到匹配音节，则将其单独输出
                step = i + 1
        resultList.append(temp)                        #将"***可能的最长匹配***"加入结果列表，如'xian'的结果为'xian'而不是'xi an'
        begin += step                                  #首字符位置更新，比较下一个未比较字符

    return resultList

if __name__ == '__main__':
    print pinyin_split('woaibeijingtiananmen')