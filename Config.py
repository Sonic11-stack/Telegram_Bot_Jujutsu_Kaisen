import telebot
import os
from dotenv import load_dotenv
import requests
from lxml import html
from io import BytesIO
from bs4 import BeautifulSoup

load_dotenv()
botJujutsuKaisen = telebot.TeleBot(os.getenv("botKey"))

tom = { 
    "0": { "info": "Отлично, вы выбрали 0 том манги 'Магическая битва. Кн. 0. Ослепительная тьма. | Акутами Гэгэ'!",
          
           "urls": { "yandex": "https://clck.ru/3PkvB8",
                     "ozon": ("https://www.ozon.ru/product"
                              "/magicheskaya-bitva-0-tokiyskiy-magicheskiy-kolledzh-oslepitelnaya-tma-akutami-gege-612566156"
                              "/?at=qQtJZjkk9czmXrMxfX4owK7up2y2yVcZPvZoBTv901Bx"
                             ),
                     "wildberries": ("https://www.wildberries.ru/catalog"
                                     "/87454853/detail.aspx"
                                    )
                   } 
    },
    "1": { "info": "Отлично, вы выбрали 1 том манги 'Магическая битва. Кн. 1. Двуликий Сукуна. Проклятый плод. | Акутами Гэгэ'!",
          
           "urls": { "yandex": "https://clck.ru/3PMJiy",
                     "ozon": ("https://www.ozon.ru/product"
                              "/magicheskaya-bitva-kn-1-dvulikiy-sukuna-proklyatyy-plod-akutami-gege-596960583"
                              "/?at=lRt6xAgZLiWPVzpLsZ2mkJoHLMX6O3ijOMW0QUYByQk4"
                             ),
                     "wildberries": ("https://www.wildberries.ru/catalog"
                                     "/186849973/detail.aspx"
                                    )
                   } 
    },
    "2": { "info": "Отлично, вы выбрали 2 том манги 'Магическая битва. Кн. 2. Мелкая рыбешка и воздаяние. Я убью тебя! | Акутами Гэгэ'!",
          
           "urls": { "yandex": "https://clck.ru/3PMJke",
                     "ozon": ("https://www.ozon.ru/product"
                              "/magicheskaya-bitva-kn-2-akutami-gege-636188979"
                              "/?at=mqtkBmMZKFWRwOKpiG8wpMXIL7K3rwfZLNY4oTkyK4ZG"
                             ),
                     "wildberries": ("https://www.wildberries.ru/catalog"
                                     "/186850921/detail.aspx?targetUrl=SG"
                                    )
                   }
    },
    "3": { "info": "Отлично, вы выбрали 3 том манги 'Магическая битва. Кн. 3. Командный бой. Черная вспышка. | Акутами Гэгэ'!",
          
           "urls": { "yandex": "https://clck.ru/3PMJnK",
                     "ozon": ("https://www.ozon.ru/product"
                              "/magicheskaya-bitva-kn-3-komandnyy-boy-chernaya-vspyshka-akutami-gege-740942487"
                              "/?at=x6tPn2Xy4HRxoo6WF52AM9yFWYp2K9t5r7r9NhPj556p"
                             ),
                     "wildberries": ("https://www.wildberries.ru/catalog"
                                     "/243939864/detail.aspx?targetUrl=SG"
                                    )
                   }
    },
    "4": { "info": "Отлично, вы выбрали 4 том манги 'Магическая битва. Кн. 4. Начало повиновения. Пагубный талант. | Акутами Гэгэ'!",
          
           "urls": { "yandex": "https://clck.ru/3PMJo9",
                     "ozon": ("https://www.ozon.ru/product"
                              "/magicheskaya-bitva-kn-4-nachalo-povinoveniya-pagubnyy-talant-akutami-gege-818914312"
                              "/?at=x6tPn2EKliN488kBtjMoBBYuYV6om5UQ7lj8mFn7R6OA"
                             ),
                     "wildberries": ("https://www.wildberries.ru/catalog"
                                     "/189045024/detail.aspx?targetUrl=EX"
                                    )
                   }
    },
    "5": { "info": "Отлично, вы выбрали 5 том манги 'Магическая битва. Кн. 5. Таланты умирают молодыми. В преддверии праздника. | Акутами Гэгэ'!",
          
           "urls": { "yandex": "https://clck.ru/3PMJrL",
                     "ozon": ("https://www.ozon.ru/product"
                              "/magicheskaya-bitva-kn-5-talanty-umirayut-molodymi-v-preddverii-prazdnika-akutami-gege-852887634"
                              "/?at=79tn4ORvxTXN3jL8fwQ00NwFAJEEE5UzQrWgwFQY6Xgj"
                             ),
                     "wildberries": ("https://www.wildberries.ru/catalog"
                                     "/188845393/detail.aspx?targetUrl=EX"
                                    )
                   }
    },
    "6": { "info": "Отлично, вы выбрали 6 том манги 'Магическая битва. Кн. 6. Инцидент в Сибуе : Открыть врата. Спиритизм. | Акутами Гэгэ'!",
          
           "urls": { "yandex": "https://clck.ru/3PVuyh",
                     "ozon": ("https://www.ozon.ru/product"
                              "/magicheskaya-bitva-kn-6-intsident-v-sibue-otkryt-vrata-spiritizm-akutami-gege-953899853"
                              "/?at=WPtNRArvETKjJ0knfoZm30Wi43YvGBFZEqXQvFk4jnwz"
                             ),
                     "wildberries": ("https://www.wildberries.ru/catalog"
                                     "/189049276/detail.aspx?targetUrl=EX"
                                    )
                   }
    },
    "7": { "info": "Отлично, вы выбрали 7 том манги 'Магическая битва. Кн. 7. Инцидент в Сибуе : Раскат грома. Правый и неправый. | Акутами Гэгэ'!",
          
           "urls": { "yandex": "https://clck.ru/3PMJty",
                     "ozon": ("https://www.ozon.ru/product"
                              "/magicheskaya-bitva-kn-7-intsident-v-sibue-raskat-groma-intsident-v-sibue-pravyy-i-nepravyy-957456384"
                              "/?at=16tL27JK4U1Ky5ZEimAp1xJCLxoLxMCnNj63OijzyLJY"
                             ),
                     "wildberries": ("https://www.wildberries.ru/catalog"
                                     "/187476862/detail.aspx?targetUrl=EX"
                                    )
                   }
    },
    "8": { "info": "Отлично, вы выбрали 8 том манги 'Магическая битва. Кн. 8. Инцидент в Сибуе: Трансформация. Закрыть врата. | Акутами Гэгэ'!",
          
           "urls": { "yandex": "https://clck.ru/3PMJuP",
                     "ozon": ("https://www.ozon.ru/product"
                              "/magicheskaya-bitva-kn-8-intsident-v-sibue-transformatsiya-intsident-v-sibue-zakryt-vrata-1063366063"
                              "/?at=r2t4P5QXqH2jPqNyclQwDOnHLmVRyof7GQoD2S0Zq9nO"
                             ),
                     "wildberries": ("https://www.wildberries.ru/catalog"
                                     "/190223297/detail.aspx?targetUrl=EX"
                                    )
                   }
    },
    "9": { "info": "Отлично, вы выбрали 9 том манги 'Магическая битва. Кн. 9. Перелетный гусь. Пламя. | Акутами Гэгэ'!",
          
           "urls": { "yandex": "https://clck.ru/3PMJuj",
                     "ozon": ("https://www.ozon.ru/product"
                               "/magicheskaya-bitva-kn-9-pereletnyy-gus-plamya-akutami-gege-1224057499"
                               "/?at=jYtZK7okru99OL83uMl2J4PT6lxP1LuOGxqYYHwkW0rB"
                             ),
                     "wildberries": ("https://www.wildberries.ru/catalog"
                                     "/190589181/detail.aspx?targetUrl=EX"
                                    )
                   }
    },
    "10": { "info": "Отлично, вы выбрали 10 том манги 'Магическая битва. Кн. 10. Колония Токио №1. Колония Сэндай. | Акутами Гэгэ'!",
           
            "urls": { "yandex": "https://clck.ru/3PMJcK",
                      "ozon": ("https://www.ozon.ru/product"
                               "/magicheskaya-bitva-kn-10-koloniya-tokio-1-glavy-162-180-akutami-gege-1389325275"
                               "/?at=r2t4P5QXqHjqkGZLUrXvB4QhrB9PMKTvgNqL3S1joNZ2"
                              ),
                      "wildberries": ("https://www.wildberries.ru/catalog"
                                      "/214555321/detail.aspx?targetUrl=EX"
                                     )
                    }
    },
    "11": { "info": "Отлично, вы выбрали 11 том манги 'Магическая битва. Кн. 11. Колония Токио 2. Колония Сакурадзима. | Акутами Гэгэ'!",
           
            "urls": { "yandex": "https://clck.ru/3PMJvV",
                      "ozon": ("https://www.ozon.ru/product"
                               "/magicheskaya-bitva-kn-11-koloniya-tokio-2-glavy-181-199-akutami-gege-1644316890"
                               "/?at=jYtZK7okruAZoNJC7NYly1hV3zP7yt1ym20kTkQEMRL"
                              ),
                      "wildberries": ("https://www.wildberries.ru/catalog"
                                      "/284822066/detail.aspx"
                                     )
                    }
    },
    "12": { "info": "Отлично, вы выбрали 12 том манги 'Магическая битва. Кн. 12. Звезда и нефть. Проклятый плод : возвращение. | Акутами Гэгэ'!",
           
            "urls": { "yandex": "https://clck.ru/3PMJvq",
                      "ozon": ("https://www.ozon.ru/product"
                               "/magicheskaya-bitva-kn-12-proklyatyy-plod-vozvrashchenie-g-200-217-akutami-gege-1758467377"
                               "/?at=BrtzpgW3GhWDlo7GSLq7Qk2tvK9wpKIA2PyJlTEmoJjk"
                              ),
                      "wildberries": ("https://www.wildberries.ru/catalog"
                                      "/309757759/detail.aspx?targetUrl=EX"
                                     )
                    }
    },
    "13": { "info": "Отлично, вы выбрали 13 том манги 'Магическая битва. Кн. 13. Решающая битва в Синдзюку. На юг. | Акутами Гэгэ'!",
           
            "urls": { "yandex": "https://clck.ru/3PMJwJ",
                      "ozon": ("https://www.ozon.ru/product/"
                               "magicheskaya-bitva-kniga-13-reshayushchaya-bitva-v-sindzyuku-na-yug-limitirovannoe-izdanie-1917540387"
                               "/?at=WPtNRArvETO57WwkI5ZKl0NiP7Lm56TJxxqzYiBzxP0Z"
                               ),
                      "wildberries": ("https://www.wildberries.ru/catalog"
                                      "/453806665/detail.aspx?targetUrl=EX"
                                     )
                    }
    },
    "14": { "info": "Отлично, вы выбрали 14 том манги 'Магическая битва. Кн. 14. Baka Survivor! Фора для отстающих. | Акутами Гэгэ'!",
           
            "urls": { "yandex": "https://clck.ru/3PMJxL",
                      "ozon": ("https://www.ozon.ru/product"
                               "/magicheskaya-bitva-kniga-14-baka-survivor-fora-dlya-otstayushchih-akutami-gege-2423230412"
                               "/?at=ywtAqlOE1F69p07BTNRB03PtVl2ZNlHpVylGNSD46zqo"
                              ),
                      "wildberries": ("https://www.wildberries.ru/catalog"
                                      "/463572869/detail.aspx?targetUrl=EX"
                                     )
                    }
    },
    "15": { "info": "Отлично, вы выбрали 15 том манги 'Магическая битва. Кн. 15. Жизнь и смерть. Что ждёт нас в будущем. | Акутами Гэгэ'!",
           
            "urls": { "yandex": "https://clck.ru/3Pjc7Y",
                      "ozon": ("https://www.ozon.ru/product"
                               "/magicheskaya-bitva-kn-15-otkrytka-teso-komplekt-akutami-gege-2829430003"
                               "/?at=ywtAZV4YzcgL6kk5c03G3vQt3JPqqDhn490PMiGM87WJ&sh=Da3UmERQbg"
                              ),
                      "wildberries": ("https://www.wildberries.ru/catalog"
                                      "/547937862/detail.aspx?targetUrl=MI"
                                     )
                    }
    }
}

photos = {
    "0": {
        "photos": {
            "manga": "../Telegram_Bot_Jujutsu_Kaisen/Images/Null_Tom.png",
            "yandex": "../Telegram_Bot_Jujutsu_Kaisen/Images/Yandex_Market_Logo.png",
            "ozon": "../Telegram_Bot_Jujutsu_Kaisen/Images/Ozon.png",
            "wildberries": "../Telegram_Bot_Jujutsu_Kaisen/Images/Wildberries.png"
        }
    },
    "1": {
        "photos": {
            "manga": "../Telegram_Bot_Jujutsu_Kaisen/Images/First_Tom.png",
            "yandex": "../Telegram_Bot_Jujutsu_Kaisen/Images/Yandex_Market_Logo.png",
            "ozon": "../Telegram_Bot_Jujutsu_Kaisen/Images/Ozon.png",
            "wildberries": "../Telegram_Bot_Jujutsu_Kaisen/Images/Wildberries.png"
        }
    },
    "2": {
        "photos": {
            "manga": "../Telegram_Bot_Jujutsu_Kaisen/Images/Second_Tom.png",
            "yandex": "../Telegram_Bot_Jujutsu_Kaisen/Images/Yandex_Market_Logo.png",
            "ozon": "../Telegram_Bot_Jujutsu_Kaisen/Images/Ozon.png",
            "wildberries": "../Telegram_Bot_Jujutsu_Kaisen/Images/Wildberries.png"
        }
    },
    "3": {
        "photos": {
            "manga": "../Telegram_Bot_Jujutsu_Kaisen/Images/Third_Tom.png",
            "yandex": "../Telegram_Bot_Jujutsu_Kaisen/Images/Yandex_Market_Logo.png",
            "ozon": "../Telegram_Bot_Jujutsu_Kaisen/Images/Ozon.png",
            "wildberries": "../Telegram_Bot_Jujutsu_Kaisen/Images/Wildberries.png"
        }
    },
    "4": {
        "photos": {
            "manga": "../Telegram_Bot_Jujutsu_Kaisen/Images/Fourth_Tom.png",
            "yandex": "../Telegram_Bot_Jujutsu_Kaisen/Images/Yandex_Market_Logo.png",
            "ozon": "../Telegram_Bot_Jujutsu_Kaisen/Images/Ozon.png",
            "wildberries": "../Telegram_Bot_Jujutsu_Kaisen/Images/Wildberries.png"
        }
    },
    "5": {
        "photos": {
            "manga": "../Telegram_Bot_Jujutsu_Kaisen/Images/Fifth_Tom.png",
            "yandex": "../Telegram_Bot_Jujutsu_Kaisen/Images/Yandex_Market_Logo.png",
            "ozon": "../Telegram_Bot_Jujutsu_Kaisen/Images/Ozon.png",
            "wildberries": "../Telegram_Bot_Jujutsu_Kaisen/Images/Wildberries.png"
        }
    },
    "6": {
        "photos": {
            "manga": "../Telegram_Bot_Jujutsu_Kaisen/Images/Sixth_Tom.png",
            "yandex": "../Telegram_Bot_Jujutsu_Kaisen/Images/Yandex_Market_Logo.png",
            "ozon": "../Telegram_Bot_Jujutsu_Kaisen/Images/Ozon.png",
            "wildberries": "../Telegram_Bot_Jujutsu_Kaisen/Images/Wildberries.png"
        }
    },
    "7": {
        "photos": {
            "manga": "../Telegram_Bot_Jujutsu_Kaisen/Images/Seventh_Tom.png",
            "yandex": "../Telegram_Bot_Jujutsu_Kaisen/Images/Yandex_Market_Logo.png",
            "ozon": "../Telegram_Bot_Jujutsu_Kaisen/Images/Ozon.png",
            "wildberries": "../Telegram_Bot_Jujutsu_Kaisen/Images/Wildberries.png"
        }
    },
    "8": {
        "photos": {
            "manga": "../Telegram_Bot_Jujutsu_Kaisen/Images/Eighth_Tom.png",
            "yandex": "../Telegram_Bot_Jujutsu_Kaisen/Images/Yandex_Market_Logo.png",
            "ozon": "../Telegram_Bot_Jujutsu_Kaisen/Images/Ozon.png",
            "wildberries": "../Telegram_Bot_Jujutsu_Kaisen/Images/Wildberries.png"
        }
    },
    "9": {
        "photos": {
            "manga": "../Telegram_Bot_Jujutsu_Kaisen/Images/Ninth_Tom.png",
            "yandex": "../Telegram_Bot_Jujutsu_Kaisen/Images/Yandex_Market_Logo.png",
            "ozon": "../Telegram_Bot_Jujutsu_Kaisen/Images/Ozon.png",
            "wildberries": "../Telegram_Bot_Jujutsu_Kaisen/Images/Wildberries.png"
        }
    },
    "10": {
        "photos": {
            "manga": "../Telegram_Bot_Jujutsu_Kaisen/Images/Tenth_Tom.png",
            "yandex": "../Telegram_Bot_Jujutsu_Kaisen/Images/Yandex_Market_Logo.png",
            "ozon": "../Telegram_Bot_Jujutsu_Kaisen/Images/Ozon.png",
            "wildberries": "../Telegram_Bot_Jujutsu_Kaisen/Images/Wildberries.png"
        }
    },
    "11": {
        "photos": {
            "manga": "../Telegram_Bot_Jujutsu_Kaisen/Images/Eleventh_Tom.png",
            "yandex": "../Telegram_Bot_Jujutsu_Kaisen/Images/Yandex_Market_Logo.png",
            "ozon": "../Telegram_Bot_Jujutsu_Kaisen/Images/Ozon.png",
            "wildberries": "../Telegram_Bot_Jujutsu_Kaisen/Images/Wildberries.png"
        }
    },
    "12": {
        "photos": {
            "manga": "../Telegram_Bot_Jujutsu_Kaisen/Images/Twelfth_Tom.png",
            "yandex": "../Telegram_Bot_Jujutsu_Kaisen/Images/Yandex_Market_Logo.png",
            "ozon": "../Telegram_Bot_Jujutsu_Kaisen/Images/Ozon.png",
            "wildberries": "../Telegram_Bot_Jujutsu_Kaisen/Images/Wildberries.png"
        }
    },
    "13": {
        "photos": {
            "manga": "../Telegram_Bot_Jujutsu_Kaisen/Images/Thirteenth_Tom.png",
            "yandex": "../Telegram_Bot_Jujutsu_Kaisen/Images/Yandex_Market_Logo.png",
            "ozon": "../Telegram_Bot_Jujutsu_Kaisen/Images/Ozon.png",
            "wildberries": "../Telegram_Bot_Jujutsu_Kaisen/Images/Wildberries.png"
        }
    },
    "14": {
        "photos": {
            "manga": "../Telegram_Bot_Jujutsu_Kaisen/Images/Fourteenth_Tom.png",
            "yandex": "../Telegram_Bot_Jujutsu_Kaisen/Images/Yandex_Market_Logo.png",
            "ozon": "../Telegram_Bot_Jujutsu_Kaisen/Images/Ozon.png",
            "wildberries": "../Telegram_Bot_Jujutsu_Kaisen/Images/Wildberries.png"
        }
    },
    "15": {
        "photos": {
            "manga": "../Telegram_Bot_Jujutsu_Kaisen/Images/Fifteenth_Tom.png",
            "yandex": "../Telegram_Bot_Jujutsu_Kaisen/Images/Yandex_Market_Logo.png",
            "ozon": "../Telegram_Bot_Jujutsu_Kaisen/Images/Ozon.png",
            "wildberries": "../Telegram_Bot_Jujutsu_Kaisen/Images/Wildberries.png"
        }
    } 
}

user_state = {} 
user_text = {}
dif_photos = {}
file_ids = {}


for key, value in photos.items():
    dif_photos[key] = {}
    for photo_key, path in value["photos"].items():
        with open(path, "rb") as f:
            dif_photos[key][photo_key] = BytesIO(f.read())
        
toms_urls_bytes = {}
toms_soup = {}
for key, value in tom.items():
    toms_urls_bytes[key] = {}
    toms_soup[key] = {}
    for market, url in value["urls"].items():  
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        toms_urls_bytes[key][market] = html
        toms_soup[key][market] = soup