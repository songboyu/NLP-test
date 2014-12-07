NLP-test
========

自然语言处理实验

    · seg.py:         分词程序
    · ngram.py        统计一元词频、二元词频
    · common.py       字符串处理集（包括转换为unicode，全角转半角，半角转全角）
    · main.py         主程序入口
    
    · corpus/         96年人民日报语料
    
    · corpus_seg/     96年人民日报语料----已切分
    
    · seg_method/
            bwd_max.py                  逆向最大匹配分词算法
            fwd_max.py                  正向最大匹配分词算法
            
    · core/
            Graph.py                    有向图结构
            InputMethod.py              已切分好的拼音串转汉字串
            Model.py                    加载语言模型
            Pinyin.py                   拼音串切分1
            Pinyin2.py                  拼音串切分2
            
    · freq/
            freq_select.py              选择高频词程序
            word_freq.txt               一元词频表
            unigram_freq.txt            二元词频表
            unigram_freq_selected.txt   二元词频表----高频
            dict.txt                    [词/拼音]字典
            dict-selected.txt           [词/拼音]字典----高频
    
    · alogorithm/
            Trie2.py                    生成汉语拼音的trie树结构
            pinyin_trie                 汉语拼音的trie树结构
            pinyin_trie_list.txt        汉语拼音列表
            Trie.py                     trie树测试
            viterbi.py                  基本viterbi算法（取自Wikipedia）
            
            
    
