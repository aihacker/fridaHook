section1 = {
    "第一章 燃烧基础知识": {"single_selection":47, "multiple_selection":35},
    "第二章 火灾基础知识": {"single_selection":69, "multiple_selection":25},
    "第三章 爆炸基础知识": {"single_selection":54, "multiple_selection":23},
    "第四章 易燃易爆危险品消防安全知识": {"single_selection":43, "multiple_selection":26}
}
section2 = {
    "第一章 概述": {"single_selection":0, "multiple_selection":0},
    "第二章 生产和储存物品的火灾危险性分类": {"single_selection":79, "multiple_selection":30},
    "第三章 建筑分类与耐火等级": {"single_selection":102, "multiple_selection":22},
    "第四章 总平面布局和平面布置": {"single_selection":84, "multiple_selection":28},
    "第五章 防火防烟分区与分隔": {"single_selection":97, "multiple_selection":30},
    "第六章 安全疏散": {"single_selection":84, "multiple_selection":48},
    "第七章 建筑电气防火": {"single_selection":23, "multiple_selection":19},
    "第八章 建筑防爆": {"single_selection":29, "multiple_selection":19},
    "第九章 建筑设备防火防爆": {"single_selection":28, "multiple_selection":13},
    "第十章 建筑装修、保温材料防火": {"single_selection":56, "multiple_selection":15},
    "第十一章 灭火救援设施": {"single_selection":79, "multiple_selection":16}}
section3 = {
    "第一章 概述": {"single_selection":5, "multiple_selection":5},
    "第二章 室内外消防给水系统": {"single_selection":79, "multiple_selection":6},
    "第三章 自动喷水灭火系统": {"single_selection":79, "multiple_selection":4},
    "第四章 水喷雾灭火系统": {"single_selection":35, "multiple_selection":4},
    "第五章 细水雾灭火系统": {"single_selection":48, "multiple_selection":5},
    "第六章 气体灭火系统": {"single_selection":84, "multiple_selection":8},
    "第七章 泡沫灭火系统": {"single_selection":62, "multiple_selection":6},
    "第八章 干粉灭火系统": {"single_selection":41, "multiple_selection":6},
    "第九章 火灾自动报警系统": {"single_selection":88, "multiple_selection":40},
    "第十章 防烟排烟系统": {"single_selection":89, "multiple_selection":22},
    "第十一章 消防应急照明和疏散指示系统": {"single_selection":42, "multiple_selection":12},
    "第十二章 城市消防远程监控系统": {"single_selection":32, "multiple_selection":14},
    "第十三章 建筑灭火器配置": {"single_selection":70, "multiple_selection":18},
    "第十四章 消防供配电": {"single_selection":43, "multiple_selection":15}}
section4 = {
    "第一章 概述": {"single_selection":0, "multiple_selection":0},
    "第二章 石油化工防火": {"single_selection":37, "multiple_selection":17},
    "第三章 地铁防火": {"single_selection":37, "multiple_selection":8},
    "第四章 城市交通隧道防火": {"single_selection":34, "multiple_selection":11},
    "第五章 加油加气站防火": {"single_selection":59, "multiple_selection":13},
    "第六章 发电厂防火": {"single_selection":43, "multiple_selection":12},
    "第七章 飞机库防火": {"single_selection":59, "multiple_selection":14},
    "第八章 汽车库、修车库防火": {"single_selection":114, "multiple_selection":12},
    "第九章 洁净厂房防火": {"single_selection":41, "multiple_selection":23},
    "第十章 信息机房防火": {"single_selection":41, "multiple_selection":8},
    "第十一章 古建筑防火": {"single_selection":27, "multiple_selection":20},
    "第十二章 人民防空工程防火": {"single_selection":80, "multiple_selection":43}}
section5 = {
    "第一章 概述": {"single_selection":9, "multiple_selection":9},
    "第二章 火灾风险识别": {"single_selection":33, "multiple_selection":16},
    "第三章 火灾风险评估方法概述": {"single_selection":25, "multiple_selection":18},
    "第四章 建筑性能化防火设计评估": {"single_selection":38, "multiple_selection":12}}
sections = {
    "第一篇 消防基础知识": section1,
    "第二篇 建筑防火": section2,
    "第三篇 建筑消防设施": section3,
    "第四篇 其他建筑、场所防火": section4,
    "第五篇 消防安全评估": section5
}

for section_name, section_content in sections.items():
    section_ = section_name
    print(section_)
    for chapter__name, selection in section_content.items():
        chapter_ = chapter__name
        print("\t", chapter_)
        print("\t\t", "single_selection: ", selection["single_selection"])
        print("\t\t", "multiple_selection: ", selection["multiple_selection"])
