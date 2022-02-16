import json


db_dict = {
    # Players
    "Seyfer": {
        "type": "player",
        "contact": ["https://www.youtube.com/c/SeyferStudios"],
        "playlist": "",
        "others": ["Soul Calibur Chile", "Soul Calibur América"]        
    },

    "Bad Gato": {
        "type": "player",
        "contact": ["https://www.youtube.com/channel/UCcMG9OE9PlOvXd8PIgl1l-Q"],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t7inPngGoWDiBKxOKbaPXUY",
        "others": ["Soul Calibur Chile"]        
    },

    "DonMarlboro": {
        "type": "player",
        "contact": ["https://www.youtube.com/channel/UCjYR50uj6yA3UkyAq5FCqtw"],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t4WgGCJqRtV4uHlajcSHAip",
        "others": ["Soul Calibur Chile", "Soul Calibur América"]
    },

    "SaimonChaild": {
        "type": "player",
        "contact": [
            "https://www.youtube.com/channel/UCDLKmtoE80-mGNzcelvcSwA",
            "https://www.twitch.tv/saimonchaild_"
        ],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6BIHUbhWoiImcYZbeQYFzW",
        "others": ["Soul Calibur Chile", "Soul Calibur América"]
    },

    "Karol": {
        "type": "player",
        "contact": [
            "https://www.twitch.tv/karolkjx",
            "https://www.youtube.com/channel/UCt6gg-p7QqsYHvWmbOFQoqA"
        ],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t4_84l7sweKXqbAxBUCD6Wb",
        "others": ["Soul Calibur Chile"]
    },

    "SigFrancis": {
        "type": "player",
        "contact": ["https://www.youtube.com/user/refran5"],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6fRaOJPS84khrnPhlKodB7",
        "others": ["Soul Calibur América"]
    },

    "Camus": {
        "type": "player",
        "contact": [
            "https://www.youtube.com/channel/UCCfUfXhGb4CWfcufUfo0nVQ",
            "https://www.youtube.com/channel/UC-SWYSSJDofVuMl-ch8T92A"
        ],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5F3cOnsi0LEWya5FztxGTw",
        "others": ["Soul Calibur América"]
    },

    "Junixart": {
        "type": "player",
        "contact": [
            "https://www.youtube.com/user/junixart",
            "https://www.youtube.com/channel/UC0jIpWqYY-768ADajSOSMMw"
        ],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6cPJEfOvbZ4ewYT0xfyzeR",
        "others": ["Soul Calibur Chile"]
    },

    "zen-x": {
        "type": "player",
        "contact": [
            "https://www.youtube.com/user/junixart",
            "https://www.youtube.com/channel/UCcqUVrtRrIUOgzpnQT_0wlA"
        ],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5iVwDcfNHJ30ORntTWE_Mt",
        "others": ["Soul Calibur América"]
    },

    "Eche": {
        "type": "player",
        "contact": ["https://www.youtube.com/channel/UCYOfh1vaybY-AgE5WCOgNfQ"],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5EMa0pEOZbWuhnhCP1ZAWq",
        "others": ["Soul Calibur América"]
    },

    "Gontranno": {
        "type": "player",
        "contact": ["https://www.youtube.com/channel/UCo3EZ-0WFtmAErr8f5KFY7w"],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t78dk4jj6x51dJa_oEFQJJu",
        "others": ["Soul Calibur Chile"]
    },

    "Demonio Garuda": {
        "type": "player",
        "contact": ["https://www.youtube.com/channel/UC-f5ATC1hxZJwxcSLVSxtsQ"],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t69AzpWONILZdImBcukxdc7",
        "others": ["Soul Calibur Chile"]
    },

    "raynarrok": {
        "type": "player",
        "contact": ["https://www.youtube.com/user/lraynarrokl"],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t4yWgUWujRmh_CpXPv6ovG1",
        "others": ["Soul Calibur América"]
    },

    "Beowulf": {
        "type": "player",
        "contact": ["https://www.youtube.com/channel/UCVwZEdvYzonU_vFIfcKlXpQ"],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6libDfzT5ZgnCKty20jPki",
        "others": []
    },

    "Maxxus": {
        "type": "player",
        "contact": ["https://www.youtube.com/channel/UC5KGtnO8zi9B0SR5_xub60w"],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t62PK83JBPXNCFDweBQJX5U",
        "others": ["Soul Calibur América"]
    },

    "E1000": {
        "type": "player",
        "contact": ["https://www.youtube.com/channel/UC-28NThOmlZ_06Te3QLJKtQ"],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5OrZV2eQgXC2S2OslYIoNK",
        "others": ["Soul Calibur Chile"]
    },

    "Lang": {
        "type": "player",
        "contact": ["https://www.youtube.com/channel/UCwqY50qCzN5bXuVtWyaaFbA"],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t7oeQGl1kXJfLod9wwji8NQ",
        "others": ["Soul Calibur Chile"]
    },

    "Mastodon": {
        "type": "player",
        "contact": ["https://www.youtube.com/channel/UCm7pucCgAFgKUFOhkfrMjMQ"],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5WtjO5OrpAs9VeRC3LPCyj",
        "others": ["Soul Calibur Chile"]
    },

    "Sonic": {
        "type": "player",
        "contact": ["https://www.youtube.com/c/SonicX"],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5MYlFvo1HUSvLKlKrxIjta",
        "others": []
    },

    "Sebas": {
        "type": "player",
        "contact": ["https://www.youtube.com/channel/UC7S9cOu9ob384mkuscDhsFw"],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5cCPrXbS3vyIIHSP5ssLzE",
        "others": []
    },

    "Albhed": {
        "type": "player",
        "contact": ["https://www.youtube.com/channel/UCFrFKjy5e2XVomZx-ohyC2Q"],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6tHpF3Q1Q1JQAGO-re1e-X",
        "others": ["Soul Calibur Chile"]
    },

    "wylde": {
        "type": "player",
        "contact": ["https://www.youtube.com/user/guitardevilf5"],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6EGhT85l7I_dyhcr8kScjl",
        "others": ["Soul Calibur Chile", "Soul Calibur América"]
    },

    "Kyorage": {
        "type": "player",
        "contact": [
            "https://www.youtube.com/user/unrealassasin",
            "https://www.youtube.com/channel/UCwGErHJ-3xmaHwmxGeLFnhg"
        ],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t4wszcCcv3sVPWv5kGHOW5y",
        "others": ["Soul Calibur Chile", "Soul Calibur América"]
    },

    "Nightwing Ialmar": {
        "type": "player",
        "contact": [
            "https://www.twitch.tv/ialmar94",
            "https://www.youtube.com/channel/UCoLiC9BbrJFWRe2GwTbpoyQ",
            "https://www.youtube.com/channel/UC0jIpWqYY-768ADajSOSMMw"
        ],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t7BZE16Lds-STFuexFYS4sI",
        "others": []
    },

    "Estebangris": {
        "type": "player",
        "contact": [],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t7dhJeajYfB2WQ_k0U0SLks",
        "others": ["Soul Calibur Chile"]
    },

    "Edu Bushi": {
        "type": "player",
        "contact": [],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t52khCu1KxcwoCMzKrZ_WiB",
        "others": ["Soul Calibur Chile"]
    },

    "Annie": {
        "type": "player",
        "contact": [],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t7orxKOl8Hi3LlGl3TaiEic",
        "others": ["Soul Calibur América"]
    },

    "Kovas": {
        "type": "player",
        "contact": [],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t76kUbMnqm_sM49OtCkwUML",
        "others": ["Soul Calibur América"]
    },

    "Team Ninja": {
        "type": "player",
        "contact": [],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5JUGLclQVjE3PWEGqC-ozz",
        "others": []
    },

    "Toshiaki": {
        "type": "player",
        "contact": ["https://www.youtube.com/user/ToshiakiProductions"],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6-w5tz92uI5J-ThcivHCC9",
        "others": ["Soul Calibur Chile"]
    },

    "Rodol Foffo": {
        "type": "player",
        "contact": [],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5vafp6hLS2lt6KF0S2m86a",
        "others": ["Soul Calibur Chile"]
    },

    "Fire Red": {
        "type": "player",
        "contact": [],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5Ww1-2kqO5AeMJfuNBvzsb",
        "others": ["Soul Calibur América"]
    },

    "Ozkuervo": {
        "type": "player",
        "contact": [],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t4SnxBgafpkevWUxByL_Gpn",
        "others": ["Soul Calibur Chile"]
    },

    "JaffarWolf": {
        "type": "player",
        "contact": ["https://www.youtube.com/channel/UCwICJGTSYLct45xMu3JqfIQ"],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6OazJzpkop7W6u9v4Q4cgH",
        "others": ["Soul Calibur América"]
    },

    "Leospirandio": {
        "type": "player",
        "contact": [],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t76HmAfTwU9dxQp28Uv2bPX",
        "others": ["Soul Calibur Chile"]
    },

    "Ubitreides": {
        "type": "player",
        "contact": ["https://www.youtube.com/channel/UCfzakZ3xItZVK4DWPLgViAQ"],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t67SU9-Br4O5a9teuu4cZvL",
        "others": ["Soul Calibur Chile", "Soul Calibur América"]
    },

    "Adrianncr": {
        "type": "player",
        "contact": [],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t7zOm81n6T_fUa5aNyuHJ0v",
        "others": ["Soul Calibur América"]
    },

    "Ryudo": {
        "type": "player",
        "contact": [],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t74Qzm4wlx604Ffw1hbHY6x",
        "others": ["Soul Calibur América"]
    },

    "DuCaine": {
        "type": "player",
        "contact": [],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5ne2e6POOCmL43DogtrDzo",
        "others": []
    },

    "Estaries": {
        "type": "player",
        "contact": [],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5vdm87xTohCp1mYcr0RXBb",
        "others": ["Soul Calibur Chile"]
    },

    "Marv": {
        "type": "player",
        "contact": [],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t7tqJ9tdKQ377j_PGNwTKb9",
        "others": ["Soul Calibur Chile"]
    },

    "Sagadalius": {
        "type": "player",
        "contact": [],
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t7SI0paoelLW60ka4fEO175",
        "others": ["Soul Calibur Chile"]
    },

    # Characters
    "Taki": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t7W3yhPMKyU9uje26G1ZnBu",
    },

    "Talim": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t7R1-ibZfefU2wUDRAIa3G2",
    },

    "Setsuka": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6GsZ9sHFdkhLJ4MdSEOrwF",
    },

    "Hilde": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5CnUs7a5OfQAQsL_VQdAF4",
    },

    "2B": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t60fEU20FYYg20Tp1Y5FBGQ",
    },

    "Azwel": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6q-TlxlQSVO-F1WLcSLT03",
    },

    "Geralt": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t78v9zPaxD-M2WS5W8Shdf9",
    },

    "Groh": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t75-dwernEnAEWlSX73fzex",
    },

    "Haohmaru": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t4IvEvmhRHEfz-xEzMaoLiR",
    },

    "Zasalamel": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6a2rA51DIX72J95BqTnsbh",
    },

    "Tira": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t4dqovymm_ftxh69-vXOG0e",
    },

    "Amy": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t7QvwDN2c4jbLq0hhqVlOFq",
    },

    "Cassandra": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5anV4BL93UxrqYBAGNOgI2",
    },

    "Hwang": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5Y9hflTAH8dVYLeOr10jHR",
    },

    "Raphael": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t4vGjaOfK800WFGyx6EbCG1",
    },

    "Xianghua": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6LjfBNjGih8rH6pGcW1rg-",
    },

    "Astaroth": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t4YdujqkS3PCw8HoaqC7p40",
    },

    "Ivy": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6jL0gEFDhFF8ypHtpU3ZQJ",
    },

    "Kilik": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t4lDq3Ko9-yw4ipOzALlRf5",
    },

    "Maxi": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5HBO3pV8il2FFtRNcHLGEg",
    },

    "Seong Mi-na": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6faZQFTW_-d883_az5An5g",
    },

    "Sophitia": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t7_Yf0QJUfGVpErfaQ7u_bV",
    },

    "Yoshimitsu": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t7mTyKaL4pb_hzKvI6WHLgw",
    },

    "Cervantes": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t7q1b8iijnrYmaYuI27Gfyo",
    },

    "Mitsurugi": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t64CN2gW3GZYr6OiKOGRsWQ",
    },

    "Nightmare": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5lPgdyLfAac9Msc77gqGjZ",
    },

    "Siegfried": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t49YI80I9PtNerAjAklbWXf",
    },

    "Voldo": {
        "type": "character",
        "playlist": "https://www.youtube.com/playlist?list=PL90QAKwVH1t4JEKK40NPSAIXIO8Bh5Mu-",
    },

    # Others
    "Soul Calibur Chile": [
        "https://www.youtube.com/channel/UCRmPkSnLwBG7mBg8L2tGLSw",
        "https://www.instagram.com/soulcalibur_chile",
        "https://www.facebook.com/groups/276406139065377",
        "https://twitter.com/soulcalibur_cl"
    ],

    "Soul Calibur América": ["https://s.team/chat/QCeqoDwV"],

    "Scuffle": "https://github.com/aHorseface/Scuffle/releases",

    "Duelos": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5g2Pirxvs9YFm7blxYyvhl",

    "Ranked": "https://www.youtube.com/playlist?list=PL90QAKwVH1t79_xIVc3WnFp8QCk8a7d3N",

    "Torneos": "https://www.youtube.com/playlist?list=PL90QAKwVH1t71r6fcCw2GyROXFi32NbRM",

    "Soul Calibur VI desde 0": "https://www.youtube.com/playlist?list=PL90QAKwVH1t4GEDI3Ym8JeL88AyJKcu5S",

    "2.31 online": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5-BK_yFrn6UDBXQQYoaOL7",
    "2.31 offline": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6IRTa0tafOj45cbFqzmxYH",

    "Soul Calibur III": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6vuanXTfU2s6kzO0rNq6Le",
    "Soul Calibur IV": "https://www.youtube.com/playlist?list=PL90QAKwVH1t4Ps9-pU3qGUc8wkGpmSgqH",
    "Soul Calibur V": "https://www.youtube.com/playlist?list=PL90QAKwVH1t66BTTz0UDi3nTF8ro6BAJa",
}

# Write json5
with open("scvi_db.json5", "w", encoding="utf8") as f:
    json.dump(db_dict, f)

# Load json5
# with open("json5_test.json5", "r", encoding="utf8") as f:
#     db_dict = json.load(f)
# print(db_dict)