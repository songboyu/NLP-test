# -*- coding:utf-8 -*-
'''
  author: songboyu
  create: 2013-10-27
  summary: 正向最大匹配
'''

from common import u

CODEC='utf-8'

def fwd_mm_seg(wordDict, maxLen, str):
    '''正向最大匹配分词

    @param wordDict:    词表
    @param maxLen:      词最大长度（自定义）
    @param str:         待分词的字串
    @return:            分词序列（List）
    '''
    wordList = []
    segStr = str
    segStrLen = len(segStr)
    while segStrLen > 0:
        if segStrLen > maxLen:
            wordLen = maxLen
        else:
            wordLen = segStrLen
        subStr = segStr[0:wordLen]
        while wordLen > 1:
            if subStr in wordDict:
                break
            else:
                wordLen = wordLen - 1
                subStr = subStr[0:wordLen]
        wordList.append(subStr)
        segStr = segStr[wordLen:]
        segStrLen = segStrLen - wordLen
    return wordList
        
            
def main():
    fp_dict = open('../dict.txt')
    wordDict = {}
    for eachWord in fp_dict:
        wordDict[u(eachWord.split('\t')[0].strip(), 'utf-8')] = 1
    segStr = u'''
    ００　１９９６０１０１
０１　第３版／国际
０２　■
０３　短讯　阿拉法特视察拉马拉
０４　■
０５
　　巴勒斯坦自治领导机构主席阿拉法特３０日上午视察了拉马拉，受到成千上万
巴勒斯坦市民的热烈欢迎。阿拉法特检阅了仪仗队，并在震耳欲聋的欢呼声中向群
众发表了讲话。
００ １９９６０１０１
０１　第３版／国际
０２　■
０３　北约驻波黑维和部队司令表示　拒绝塞族推迟移交塞控区
０４　■
０５
　　新华社贝尔格莱德１２月３０日电　北约驻波黑维和部队总司令史密斯３０日
致函波黑塞族议会主席克拉伊什尼克，拒绝塞族领导人关于推迟移交萨拉热窝塞族
区的要求。
    '''
    print segStr
    wordList = fwd_mm_seg(wordDict, 4, segStr)
    for wordstr in wordList:
        print wordstr,'/',
    

if __name__ == '__main__':
    main()
