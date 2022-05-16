# This is a Python script made for users to look up idol groups' corresponding nicknames.
# 아이돌 그룹의 중국어 별명 찾기! 사용자들이 중국어 포럼을 이해할 수 있게 한다. 제작자: 에클스지
# 快速查找南韩团体以及在南韩出道或参与过南韩表演放送的团体在中文论坛里的代称; 新手作，欢迎补充！ 制作：Ekeulseuji

def nn_lookup():
    group_name = input("The group's OFFICIAL NAME in English: 输入要查的团名: ")
    nn_mapping = {
        "AESPA": "吒",
        "ASTRO": "阿童木",
        "BTS": "套/弹/防弹/胖弹",
        "NCT": "划/条/内存条",
        "GIDLE": "娃/女娃",
        "GOT7": "挂/搞基",
        "WINNER": "拿/温拿",
        "SUPERJUNIOR": "蓝/司机",
        "SEVENTEEN": "次/婷/赛文婷",
        "BSS": "夫硕顺",
        "IZONE": "矮/矮子王",
        "SF9": "顺丰/递",
        "ITZY": "一击/梯/爱梯贼歪",
        "IKON": "康/爱康",
        "MAMAMOO": "妈木/妈妈木/四姐",
        "BLACKPINK": "墨/粉墨/布莱品客",
        "STRAYKIDS": "迷/迷路/迷孩/麋鹿/斯锥剋子",
        "APINK": "阿粉",
        "X1": "乘/蝶",
        "NCT127": "哥组/数组/数/一粒七",
        "WayV": "威/威神",
        "NCTDREAM": "弟组/地租/梦队/得力木",
        "GFRIEND": "油炸亲故/油炸青菇/小女友/女友",
        "WANNAONE": "忘拿碗/碗",
        "SNSD": "腿/女帝/少时",
        "GIRLSGENERATION": "腿/女帝/少时/gg",
        "TREASURE": "宝石盒/盒",
        "CRAVITY": "莱/克莱未提",
        "VICTON": "笔筒",
        "VIXX": "碧斯",
        "BTOB": "兔比/比兔比",
        "TWICE": "兔/兔瓦斯",
        "REDVELEVT": "毯/耄/毛/红丝绒",
        "PENTAGON": "喷他狗/狗",
        "DREAMCATCHER": "捕梦网/网",
        "WJSN": "宇少",
        "LOONA": "本月/月/露娜",
        "ATEEZ": "梯子/梯/诶梯子",
        "THEBOYZ": "得/得博弈子/淘宝",
        "VERIVERY": "掰/掰里掰里/百里",
        "TVXQ": "东神/红家",
        "WEI": "荨/楚雨荨/喂/危",
        "OHMYGIRL": "噜妹/噜",
        "SHINEE": "晒一尼/闪闪/闪",
        "EXO": "一叉欧/小天/地/小老地/茶蛋",
        "PURPLEKISS": "紫吻",
        "NMIXX": "恩米克斯/爻",
        "IVE": "芙/爱抚",
        "KEP1ER": "开普勒/葡",
        "LESSERAFIM": "螺蛳粉/炽天使/炽",
        "BIGBANG": "大棒/棒/大爆炸",
        "TOMORROWBYTOGETHER": "档/文档/土巴兔",
        "TXT": "档/文档/土巴兔/踢叉踢",
        "MISSA": "思念",
        "FX": "函数/小破团",
        "IOI": "ioi",
        "FROMIS9": "米斯/普罗米斯/米斯耐",
        "DIA": "逮一亚",
        "EVERGLOW": "阁楼",
        "CLASSY": "课",
        "WEKIMEKI": "维密",
        "MOMOLAND": "摸摸蓝",
        "LOVELYZ": "梨子/梨",
        "STAYC": "黛/丝带",
        "BILLLIE": "荔",
        "WONDERGIRLS": "奇迹/原豆",
        "TEMPEST": "藤",
        "TRAINEEA": "吹/对尖/尖",
        "ENHYPEN": "恩嗨盆/符",
        "MONSTAX": "芒叉/叉",
        "INFINITE": "无限",
        "BOYSTORY": "男故",
        "AB6IX": "码",
        "DAY6": "呆六",
        "JO1": "杰欧万/酷小子",
        "NIZIU": "彩虹/虹",
        "DKZ": "兆",
        "P1HARMONY": "皮/皮万哈莫尼",
        "MAMADOL": "妈妈豆",
        "TRIBE": "踹/踹一笔",
        "CI9NATURE": "西古/吸/茜",
        "CIGNATURE": "西古/吸/茜",
        "KARD": "卡牌",
        "BRAVEGIRLS": "勇女",
        "2NE1": "21",
        "EXID": "艾迪",
        "HIGHLIGHT": "高光",
        "BEAST": "兽",
        "CLC": "天猫",
        "MAJORS": "梅",
        "HOTISSUE": "哈一咻/咻",
        "ROCKETPUNCH": "火箭拳/拳",
        "WEEEKLY": "微颗粒/微/薇",
        "4MINUTE": "四分钟",
        "CIX": "种子/种/豆豆",
        "BLACKSWAN": "黑天鹅/斯万",
        "ORANGECARAMEL": "橘子焦糖",
        "KARA": "卡拉",
        "BROWNEYEDGIRLS": "棕眼",
        "SISTAR": "姐妹/姐妹团",
        "GIRLSDAY": "女孩日",
        "TARA": "皇冠/皇冠团",
        "2PM": "下午班/下午",
        "2AM": "上午班",
        "ONEUS": "肆/万能肆",
        "ONEWE": "维/万维",
        "NFLYING": "新飞",
        "CNBLUE": "西恩/西恩blue",
        "HOT": "hot",
        "GOLDENCHILD": "金童",
        "AOA": "天使/天使团",
        "AFTERSCHOOL": "放学团",
        "SECRETNUMBER": "秘书/秘数/秘",
        "BVNDIT": "本地特/奔",
        "APRIL": "四月",
        "NUEST": "扭/新东方/厨/扭易斯特",
        "LABOUM": "拉蹦",
        "GU9UDAN": "咕咕蛋/咕咕",
        "GUGUDAN": "咕咕蛋/咕咕",
        "CHREEYBULLET": "樱桃子弹/樱弹",
        "NCTU": "U队",
        "SUPERM": "晋/超级满",
        "GOTTHEBEAT": "女晋",
        "NATURE": "缺/内一秋"
    }

    nn = nn_mapping.get(group_name.upper(), "!")

    if nn != "!":
        print("\n")
        print(f"{group_name} has its nickname as {nn}")
    else:
        print("\n\nOops, it looks like the group doesn't have a nickname yet. 找不到对应的昵称诶！")
        print("Did you get the name correct? 输对了团名没有？")


print("\nWelcome! 欢迎查找韩团代称！")
print("When entering the group's official name, REMOVE any non-English character except for the numbers!")
print("输入团名时要去掉任何非英文非数字字符哦!\n")
nn_lookup()

print("\n\nDo you want to try that again? 要再查一次吗？")
usr_choice = input("[y] for yes and everything else for no. 输入y进行再次查找-其他字符退出: ")

while usr_choice == "y":
    print("Okay, get it!\n")
    nn_lookup()
    usr_choice = input("\n\nEnter [y] for more searches; Enter anything else to exit. 输入y进行再次查找-其他字符退出: ")

print("\nBye-bye ^^* ")
