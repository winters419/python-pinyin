#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from pypinyin import pinyin, slug, lazy_pinyin
from pypinyin import (STYLE_NORMAL, STYLE_TONE, STYLE_TONE2, STYLE_INITIALS,
                       STYLE_FIRST_LETTER, STYLE_FINALS, STYLE_FINALS_TONE,
                       STYLE_FINALS_TONE2)


def test_pinyin_initials():
    """包含声明和韵母的词语"""
    hans = '中心'
    # 默认风格，带声调
    assert pinyin(hans) == [['zh\u014dng'], ['x\u012bn']]
    # 普通风格，不带声调
    assert pinyin(hans, STYLE_NORMAL) == [['zhong'], ['xin']]
    # 声调风格，拼音声调在韵母第一个字母上
    assert pinyin(hans, STYLE_TONE) == [['zh\u014dng'], ['x\u012bn']]
    # 声调风格2，即拼音声调在各个拼音之后，用数字 [0-4] 进行表示
    assert pinyin(hans, STYLE_TONE2) == [['zho1ng'], ['xi1n']]
    # 声母风格，只返回各个拼音的声母部分
    assert pinyin(hans, STYLE_INITIALS) == [['zh'], ['x']]
    # 首字母风格，只返回拼音的首字母部分
    assert pinyin(hans, STYLE_FIRST_LETTER) == [['z'], ['x']]
    # 启用多音字模式
    assert pinyin(hans, heteronym=True) == [['zh\u014dng', 'zh\xf2ng'],
                                            ['x\u012bn']]
    # 韵母风格1，只返回各个拼音的韵母部分，不带声调
    assert pinyin(hans, style=STYLE_FINALS) == [['ong'], ['in']]
    # 韵母风格2，带声调，声调在韵母第一个字母上
    assert pinyin(hans, style=STYLE_FINALS_TONE) == [['\u014dng'],
                                                     ['\u012bn']]
    # 韵母风格2，带声调，声调在各个拼音之后，用数字 [0-4] 进行表示
    assert pinyin(hans, style=STYLE_FINALS_TONE2) == [['o1ng'], ['i1n']]


def test_pinyin_finals():
    """只包含韵母的词语"""
    hans = '嗷嗷'
    assert pinyin(hans) == [['\xe1o'], ['\xe1o']]
    assert pinyin(hans + 'abc') == [['\xe1o'], ['\xe1o'], ['abc']]
    assert pinyin(hans, STYLE_NORMAL) == [['ao'], ['ao']]
    assert pinyin(hans, STYLE_TONE) == [['\xe1o'], ['\xe1o']]
    assert pinyin(hans, STYLE_TONE2) == [['a2o'], ['a2o']]
    assert pinyin(hans, STYLE_INITIALS) == [[''], ['']]
    assert pinyin(hans, STYLE_FIRST_LETTER) == [['a'], ['a']]
    assert pinyin(hans, heteronym=True) == [['\xe1o'], ['\xe1o']]
    assert pinyin('啊', heteronym=True) == [['\u0101', '\xe1',
                                              '\u01ce', '\xe0', 'a']]
    assert pinyin(hans, style=STYLE_FINALS) == [['ao'], ['ao']]
    assert pinyin(hans, style=STYLE_FINALS_TONE) == [['\xe1o'], ['\xe1o']]
    assert pinyin(hans, style=STYLE_FINALS_TONE2) == [['a2o'], ['a2o']]


def test_slug():
    hans = '中心'
    assert slug(hans) == 'zhong-xin'
    assert slug(hans, heteronym=True) == 'zhong-xin'


def test_zh_and_en():
    """中英文混合的情况"""
    # 中英文
    hans = '中心'
    assert pinyin(hans + 'abc') == [['zh\u014dng'], ['x\u012bn'], ['abc']]


def test_others():
    # 非字符串
    assert pinyin(1) == []
    # 空字符串
    assert pinyin('') == []
    # 单个汉字
    assert pinyin('營') == [['y\xedng']]
    # 中国 人
    assert pinyin('中国人') == [['zh\u014dng'], ['gu\xf3'], ['r\xe9n']]
    # 日文
    assert pinyin('の') == [['\u306e']]
    # 没有读音的汉字，还不存在的汉字
    assert pinyin('\u9fff') == [['\u9fff']]


def test_lazy_pinyin():
    assert lazy_pinyin('中国人') == ['zhong', 'guo', 'ren']
    assert lazy_pinyin('中心') == ['zhong', 'xin']
    assert lazy_pinyin('中心', style=STYLE_TONE) == ['zh\u014dng', 'x\u012bn']
    assert lazy_pinyin('中心', style=STYLE_INITIALS) == ['zh', 'x']
