NLP-test
========

### 自然语言处理实验
    1. 正向逆向分词
    2. 一元二元词频统计
    3. 拼音流切分
    4. HMM简易中文输入法

### 目录结构
    · seg.py          分词脚本
    · ngram.py        统计一元词频、二元词频
    · common.py       字符串处理集（包括转换为unicode，全角转半角，半角转全角）
    · main.py         主程序入口
    
    · core/
            Graph.py                    有向图结构
            InputMethod.py              拼音串转汉字串
            Model.py                    加载语言模型

    · corpus/         96年人民日报语料
    
    · corpus_seg/     96年人民日报语料----已切分
            
    · freq/
            freq_select.py              选择高频词脚本
            word_freq.txt               一元词频表
            unigram_freq.txt            二元词频表
            unigram_freq_selected.txt   二元词频表----高频
            dict.txt                    [词/拼音]字典
            dict-selected.txt           [词/拼音]字典----高频
    
    · pinyin/
            pinyin_list.txt             有效汉语拼音列表
            Trie.py                     Trie树操作类
            pinyin.py                   拼音流切分脚本
    
    · seg_method/
            bwd_max.py                  逆向最大匹配分词算法
            fwd_max.py                  正向最大匹配分词算法
            
