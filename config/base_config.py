# 基础配置
PLATFORM = "xhs"
KEYWORDS = "阅读"
LOGIN_TYPE = "qrcode"  # qrcode or phone or cookie
COOKIES = ""
# 具体值参见media_platform.xxx.field下的枚举值，暂时只支持小红书
SORT_TYPE = "popularity_descending"
# 具体值参见media_platform.xxx.field下的枚举值，暂时只支持抖音
PUBLISH_TIME_TYPE = 0
CRAWLER_TYPE = "search"  # 爬取类型，search(关键词搜索) | detail(帖子详情)| creator(创作者主页数据)

# 是否开启 IP 代理
ENABLE_IP_PROXY = False

# 代理IP池数量
IP_PROXY_POOL_COUNT = 2

# 代理IP提供商名称
IP_PROXY_PROVIDER_NAME = "kuaidaili"

# 设置为True不会打开浏览器（无头浏览器）
# 设置False会打开一个浏览器
# 小红书如果一直扫码登录不通过，打开浏览器手动过一下滑动验证码
# 抖音如果一直提示失败，打开浏览器看下是否扫码登录之后出现了手机号验证，如果出现了手动过一下再试。
HEADLESS = False

# 是否保存登录状态
SAVE_LOGIN_STATE = True

# 数据保存类型选项配置,支持三种类型：csv、db、json
SAVE_DATA_OPTION = "json"  # csv or db or json

# 用户浏览器缓存的浏览器文件配置
USER_DATA_DIR = "%s_user_data_dir"  # %s will be replaced by platform name

# 爬取开始页数 默认从第一页开始
START_PAGE = 1

# 爬取视频/帖子的数量控制
CRAWLER_MAX_NOTES_COUNT = 20

# 并发爬虫数量控制
MAX_CONCURRENCY_NUM = 1

# 是否开启爬图片模式, 默认不开启爬图片
ENABLE_GET_IMAGES = False

# 是否开启爬评论模式, 默认不开启爬评论
ENABLE_GET_COMMENTS = False

# 是否开启爬二级评论模式, 默认不开启爬二级评论
# 老版本项目使用了 db, 则需参考 schema/tables.sql line 287 增加表字段
ENABLE_GET_SUB_COMMENTS = False

XHS_SPECIFIED_URL_LIST = [
" http://xhslink.com/6XCXeR",
" http://xhslink.com/To2XeR",
" http://xhslink.com/atjYeR",
"http://xhslink.com/CLtYeR",
"http://xhslink.com/ZZDYeR",
"http://xhslink.com/MELYeR",
"http://xhslink.com/3TUYeR",
"http://xhslink.com/fgaZeR",
"http://xhslink.com/S7iZeR",
"http://xhslink.com/BnQZeR",
"http://xhslink.com/SvZZeR",
"http://xhslink.com/AI6ZeR",
"http://xhslink.com/8Fg0eR",
"http://xhslink.com/iHW0eR",
"http://xhslink.com/I550eR",
"http://xhslink.com/TUd1eR",
"http://xhslink.com/1tm1eR",
"http://xhslink.com/Cxu1eR",
"http://xhslink.com/uzE1eR",
"http://xhslink.com/ElO1eR",
"http://xhslink.com/yZY1eR",
"http://xhslink.com/jlc2eR",
"http://xhslink.com/lEi2eR",
"http://xhslink.com/0VA2eR",
"http://xhslink.com/72O2eR",
"http://xhslink.com/2cX2eR",
"http://xhslink.com/EkV3eR",
"http://xhslink.com/rE43eR",
"http://xhslink.com/iNb4eR",
"http://xhslink.com/yvj4eR",
"http://xhslink.com/Swr4eR",
"http://xhslink.com/QSy4eR",
"http://xhslink.com/HaH4eR",
"http://xhslink.com/PBN4eR",
"http://xhslink.com/tMS4eR",
"http://xhslink.com/JK44eR",
"http://xhslink.com/mPe5eR",
"http://xhslink.com/eNl5eR",
"http://xhslink.com/3Vt5eR",
"http://xhslink.com/WyC5eR",
"http://xhslink.com/QpP5eR",
"http://xhslink.com/FyZ5eR",
"http://xhslink.com/iQ45eR",
"http://xhslink.com/OBb6eR",
"http://xhslink.com/aNj6eR",
"http://xhslink.com/THr6eR",
"http://xhslink.com/P4A6eR",
"http://xhslink.com/LsO6eR",
"http://xhslink.com/XVV6eR",
"http://xhslink.com/SK76eR",
"http://xhslink.com/ZIB7eR",
"http://xhslink.com/GuI7eR",
"http://xhslink.com/ojS7eR",
"http://xhslink.com/LnW7eR",
"http://xhslink.com/Yg67eR",
"http://xhslink.com/veg8eR",
"http://xhslink.com/5Hs8eR",
"http://xhslink.com/zTeyxR",
"http://xhslink.com/fIkyxR",
"http://xhslink.com/CapyxR",
"http://xhslink.com/U6qyxR",
"http://xhslink.com/rxuyxR",
"http://xhslink.com/42yyxR",
"http://xhslink.com/uIzyxR",
"http://xhslink.com/uxCyxR",
"http://xhslink.com/ASGyxR",
"http://xhslink.com/QBHyxR",
"http://xhslink.com/5mNyxR",
"http://xhslink.com/t2OyxR",
"http://xhslink.com/LmSyxR",
" http://xhslink.com/HuTyxR",
"http://xhslink.com/K5WyxR",
"http://xhslink.com/i0XyxR",
"http://xhslink.com/d61yxR",
"http://xhslink.com/ZE5yxR",
"http://xhslink.com/ZR7yxR",
"http://xhslink.com/osbzxR",
"http://xhslink.com/xhfzxR",
"http://xhslink.com/PThzxR",
"http://xhslink.com/HejzxR",
"http://xhslink.com/BzozxR",
"http://xhslink.com/Q0ozxR",
"http://xhslink.com/dTrzxR",
"http://xhslink.com/RguzxR",
"http://xhslink.com/1NvzxR",
"http://xhslink.com/n5AzxR",
"http://xhslink.com/hGCzxR",
"http://xhslink.com/ilEzxR",
"http://xhslink.com/ESHzxR",
"http://xhslink.com/piKzxR",
"http://xhslink.com/29LzxR",
"http://xhslink.com/PYPzxR",
"http://xhslink.com/t8QzxR",
"http://xhslink.com/tRVzxR",
"http://xhslink.com/ujVzxR",
"http://xhslink.com/0DXzxR",
"http://xhslink.com/zT2zxR",
"http://xhslink.com/tB3zxR",
"http://xhslink.com/3R6zxR",
"http://xhslink.com/7v9zxR",
"http://xhslink.com/FTbAxR",
"http://xhslink.com/FUiAxR",
"http://xhslink.com/H6nAxR",
"http://xhslink.com/2brAxR",
"http://xhslink.com/J1tAxR",
"http://xhslink.com/sexAxR",
"http://xhslink.com/8lAAxR",
"http://xhslink.com/wUEAxR",
"http://xhslink.com/vSFAxR",
"http://xhslink.com/XtJAxR",
"http://xhslink.com/fyLAxR",
"http://xhslink.com/6GNAxR",
"http://xhslink.com/idRAxR",
"http://xhslink.com/jZSAxR",
"http://xhslink.com/Q1VAxR",
"http://xhslink.com/UtVAxR",
"http://xhslink.com/qPXAxR",
"http://xhslink.com/Qx2AxR",
"http://xhslink.com/123AxR",
"http://xhslink.com/xooVeR",
"http://xhslink.com/02MVeR",
"http://xhslink.com/8AUVeR",
"http://xhslink.com/W20WeR",
"http://xhslink.com/vhhWeR",
"http://xhslink.com/djlWeR",
"http://xhslink.com/tnsWeR",
"http://xhslink.com/q1OWeR",
"http://xhslink.com/pZzWeR",
"http://xhslink.com/W20WeR",
"http://xhslink.com/F78WeR",
"http://xhslink.com/GdfXeR",
"http://xhslink.com/yylXeR",
"http://xhslink.com/nnwXeR",
"http://xhslink.com/6XCXeR"]

# 指定小红书需要爬虫的笔记ID列表
XHS_SPECIFIED_ID_LIST = [
    "65a0d390000000001a00336d",
    "665528d200000000050066e6",
    "6680d4bf000000001e0116ef",
    "65a9d3f100000000290153fe", # 图文混合
    "6621df8a00000000040199d3",
    "66906ab70000000005005965",
    "6690b1c0000000000500556e",
    "669112d70000000025014042",
    "665337470000000016012c57",
    "663a48ea000000001e01fbe0",
    "66a230a000000000270133c7",
    "6642c56e000000001e03515a",
    "65f1d5130000000014007eaf",
    "665ff02c000000000d00c254",
    "6642145c000000001e03333f",
    "6622123200000000010337ae",
    "6515fcf1000000001a016ca5",
    "66305d71000000001e01ac86",
    "65e06fc7000000000303557a",
    "64fae522000000001e02e4ba",
    "66926db800000000250022a1",
    "669500610000000025014282",
    "65f7badb000000001203f08d",
    "64e86ed7000000000b029a64",
    "64eb5dab000000000800d21f",
    "6699d6210000000025000007",
    "65f085540000000012033c66",
    "667e1b50000000001c0283c8",
    "6603d0140000000012021853",
    "667ded35000000001c020c0b",
    "65a3b795000000001d02812f",
    "654eec5f000000000f02b7c4",
    "65fc460e0000000013025c74",
    "65b3be9500000000100384de",
    "663d79b6000000001e0300e7",
    "66a264ff000000000600d914",
    "6646f5a6000000001501267a",
    "65eee24a000000000d00ddc2",
    "6641ba5b000000001e01ac87",
    "6504166d000000001e021e7b",
    "65b34f9a000000000f037169",
    "62bb071d000000000f008f9e",
    "6680e887000000001e013f2e",
    "66987ebc00000000250177ae",
    "663b7ce0000000001e01a956",
    "669f745c000000000a005640",
    "659b74680000000010010b1d",    
    "65005096000000001f037d41",
    "663d79b6000000001e0300e7",
    "64f1fd22000000001e032073",
    "6561b1eb0000000032035a78",
    "652a5ba4000000001d016ac5",
    "661d03d0000000001a012018",
    "667be279000000001c024a32",
    "65b782af000000001100684c",
    "654184c20000000025015a92",
    "650bc5770000000014027336",
    "66825b18000000001e01057e",
    "6641f896000000001e039857",
    "65d46f8c000000000b00d16d",
    "669a595b0000000025005054",
    "6621df8a00000000040199d3",
    "665337470000000016012c57",
    "664b81050000000014019850",
    "6618bce3000000001b013df9",
    "66586b09000000001500a44f",
    "65f1d5130000000014007eaf",
    "669cd1e40000000025002d7b",
    "662f60c5000000001e01a0be",
    "667a8e0e000000001c02a806",
    "66059d77000000001203e141",
    "6673cc24000000001d01b244",
    "6628dbb1000000000d032c8f",
    "66857e7f000000001c027b82",
    "668b3cd80000000005004651",
    "66a7610e000000000502331d",    
    "65cf7c7a000000000b020c80",
    "65fd5853000000001202176e",
    "64fae522000000001e02e4ba",
    "66a5afb1000000002701f8ef",
    "6627b651000000001c00a30f",
    "6699d6210000000025000007",
    "668662b5000000000a024f4f",
    "66542f5700000000160107c6",
    "669500610000000025014282",
    "6614ec45000000001b00ff03",
    "64e86ed7000000000b029a64",
    "65b34f9a000000000f037169",
    "668281dd000000001e010005",
    "65d608d80000000001028e84",
    "668f5f050000000025006175",
    "6582f7dc000000000801e579",
    "66682d5c00000000060040a5",
    "663b7ce0000000001e01a956",
    "65ec4b5600000000030327bb",
    "664634c8000000001e031d84",
    "6623789b000000000401b694",
    "65a3b795000000001d02812f",
    "667a70a2000000001c025816",
    "6680e887000000001e013f2e",
    "66945c6a000000000a00783a",
    "65423983000000001f03f74a",
    "65fc460e0000000013025c74",
    "6642a4d6000000001e039204",
    "63a79661000000001f001a43",
    "65dbeaa2000000000700576e",
    "66965ee70000000025016357",
    "6559f3c5000000003202dd39",
    "6623789b000000000401b694",
    "65fc460e0000000013025c74",
    "668d5b4d0000000005007c00",
    "65af145600000000110136d8",
    "66a757270000000027012cec",
    "644262c5000000001300d0e9",
    "641af5f6000000000800e7c2",
    "668d280b00000000250032b3",
    "66a62dda000000000503be6a",
    "669515d70000000025007eb2",
    "669a1d3a0000000003025dc0",
    "6614f03a000000001a00d50e",
    "659a7700000000001e009836",
    "668aa9ed000000001f00525b",
    "6672cc1d000000001c028c9e",
    "6684adea000000001e013260",
    "66347e33000000001e01c9f3",
    "668f5beb000000000d00ff0f",
    "66626ccf000000001303f882",
    "668aa9ed000000001f00525b",
    "6691b74e0000000025006cd0",
    "666eac10000000001d016e1c",
    "6634409f000000001e02532e",
    "64cc9d47000000000a01a866",
    "65a0d390000000001a00336d",
    "65f7badb000000001203f08d"    # ........................
]

# 指定抖音需要爬取的ID列表
DY_SPECIFIED_ID_LIST = [
    "7280854932641664319",
    "7202432992642387233"
    # ........................
]

# 指定快手平台需要爬取的ID列表
KS_SPECIFIED_ID_LIST = [
    "3xf8enb8dbj6uig",
    "3x6zz972bchmvqe"
]

# 指定B站平台需要爬取的视频bvid列表
BILI_SPECIFIED_ID_LIST = [
    "BV1d54y1g7db",
    "BV1Sz4y1U77N",
    "BV14Q4y1n7jz",
    # ........................
]

# 指定微博平台需要爬取的帖子列表
WEIBO_SPECIFIED_ID_LIST = [
    "4982041758140155",
    # ........................
]

# 指定小红书创作者ID列表
XHS_CREATOR_ID_LIST = [
    #"5bb0f870e2b1da0001e2d40a",
    # "62c7cd14000000000303e011"
    # ........................
]

# 指定Dy创作者ID列表(sec_id)
DY_CREATOR_ID_LIST = [
    "MS4wLjABAAAATJPY7LAlaa5X-c8uNdWkvz0jUGgpw4eeXIwu_8BhvqE",
    # ........................
]

# 指定bili创作者ID列表(sec_id)
BILI_CREATOR_ID_LIST = [
    "20813884",
    # ........................
]

# 指定快手创作者ID列表
KS_CREATOR_ID_LIST = [
    "3x4sm73aye7jq7i",
    # ........................
]


#词云相关
#是否开启生成评论词云图
ENABLE_GET_WORDCLOUD = False
# 自定义词语及其分组
#添加规则：xx:yy 其中xx为自定义添加的词组，yy为将xx该词组分到的组名。
CUSTOM_WORDS = {
    '零几': '年份',  # 将“零几”识别为一个整体
    '高频词': '专业术语'  # 示例自定义词
}

#停用(禁用)词文件路径
STOP_WORDS_FILE = "./docs/hit_stopwords.txt"

#中文字体文件路径
FONT_PATH= "./docs/STZHONGS.TTF"
