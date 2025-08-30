import re
import telebot

botJujutsuKaisen = telebot.TeleBot('')

from telebot import types

import requests
from lxml import html

from io import BytesIO
from PIL import Image
from bs4 import BeautifulSoup

tom = { 
              "1" : { "info" : "Отлично, вы выбрали 1 том манги 'Магическая битва. Кн. 1. Двуликий Сукуна. Проклятый плод. | Акутами Гэгэ'!",
                      "photo" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\First_Tom.jpg",
                      "urls" : { "yandex" : "https://market.yandex.ru/card/manga-magicheskaya-bitva-kn1-dvulikiy-sukuna-proklyatyy-plod/103215283786?hid=90401&show-uid=17555929933661977333006016&from=search&cpa=1&do-waremd5=7K64G_AmOU93e6ZmIRCzbA&sponsored=1&cpc=LHdTbLgP0-KCEQmnLr67hdgX7gsF53eM5TAw72MS1kyAskQN_NnIK9SsQ9dcHkN-IoCLY1HIalZO1ZEHaR52ebI0vovk9V8m28u-PhgFfADObkCONv4UShYmuZ6VpFKWdXmxK6bQzW0lsfMf0idPY19V2aTYaAaQmwFP1_gCdwBiKsJmHPaz--OoyVrKBfEUDFl4OqmvBI55CWNvpwsN75EiPwEkWGxrRlcgkaGPSPp7txx1_xY021pjg1Jg8arnmzJqrb9cyl7FqsVoB-VAOP7V03tO-RUZjDUO-7eqFM6txj8YwRf4e-6NOZ4EDsvcByY-w5tSKfLU690kGP8wGH0yY56GThkwet-Ug74kAPauNLXl6sUHrhzFVcsfp2CN7dwjlWFl19liEwVHzGszxlt3BhLtWSt_unFxJzjzDTjZzzVc6Qo_F6NltSqhhx1YWliDBRQSAStpqSRdx-Jdn7Ya6qweDszM98sS1oT-BUaIAau3ZsIe5mg--GLpaXln7e77uMOR_D1OiidC66Es0T_d55dJ6HYxi_R8HAjvi9-7sQ2Z7eBAOeEmePqPoDBl7bB7_iNobUF9D0mEggqacmGVRrpeCI54w72cWqAZYTd1bFEZgWCxOdkuYRZfpetM&cc=CiBhZmRmNzJlODcxYzJiNTdiZTg1MWJiMGEyMmNjMDQ5ZhDnAYB95u0G",
                                "ozon" : "https://www.ozon.ru/product/magicheskaya-bitva-kn-1-dvulikiy-sukuna-proklyatyy-plod-akutami-gege-596960583/?at=k2to8Mw76s8gvPW5cpq2LVkF0mLVnRfYODp8nslmwnG",
                                "wildberries" : "https://www.wildberries.ru/catalog/186849973/detail.aspx"
                            } 
                    },
              "2" : { "info" : "Отлично, вы выбрали 2 том манги 'Магическая битва. Кн. 2. Мелкая рыбешка и воздаяние. Я убью тебя! | Акутами Гэгэ'!",
                      "photo" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\Second_Tom.jpg",
                      "urls" : { "yandex" : "https://market.yandex.ru/card/manga-magicheskaya-bitva-kn-2/102218281303?do-waremd5=AO1zIdQSyS7ODvLyrz46Ng&sponsored=1&cpc=7gMqwolVguqxJj01bVUYVMOFlAYIlQjZKkxCI00M8ULSJs7VJqicz86OyqNmSnSmOdBhBRW6aDn1b1HvirtVbeyfCF6ysNqZ5x_VGiHlBKk-BqakAPXjpcI08ak-iTYbGh5cA37ApjOKKVdOyrtaMFKDA1Zh-j7bsjB-B1t3pKwzzO5labnaqvxp4UmTfCKHSp8ejSR-jbBaW4W5EtIRHhq5mj7KXK1Op_7BpREZv4Ep3fwT0szXFytUHHQfOYP6iXdkQqZ8Z0IjOy_eOrevNT9qHDLTC_Sxo4uOwrDWkPh3IiUmtTY_XE3tYDw7HnvSM13E2oVigG7kcd1XKqFW3RhHeGDCUn3cSmgr1RXhNawac6HZvl_giPf6QbGcpIOafkOvpoETHSlVHsVHNcbGjqRSoT5wR8npg0jtv-esjavlgTQdtFqc2lShS7zxVK5-HMIBZfE3ki3eykZifkzt7CWJHGgBhO4ExI7D95-JT7unSt_XFYvVG36KPOn0une58H2uAz8bVsXF3uDQHnyikMBoV2aoyUZgJy-pyIjW_NxaX6hDxcxdYo9erwQ8Nv8iNWY01CaSY3fPBjdD5Oh-bGoUKtEm1LDHwPwlluvWLnwRKTMbs1WwDkAo5PTyBKfx&ogV=-2",
                                "ozon" : "https://www.ozon.ru/product/magicheskaya-bitva-kn-2-akutami-gege-636188979/?at=mqtkBmMZKFWRwOKpiG8wpMXIL7K3rwfZLNY4oTkyK4ZG",
                                "wildberries" : "https://www.wildberries.ru/catalog/186850921/detail.aspx?targetUrl=SG"
                            }
                    },
              "3" : { "info" : "Отлично, вы выбрали 3 том манги 'Магическая битва. Кн. 3. Командный бой. Черная вспышка. | Акутами Гэгэ'!",
                      "photo" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\Third_Tom.jpg",
                      "urls" : { "yandex" : "https://market.yandex.ru/card/manga-magicheskaya-bitva-kn3-komandnyy-boy-chernaya-vspyshka/102198034438?do-waremd5=3dzqyPeAjZ47MhSyp7i4nA&sponsored=1&cpc=7gMqwolVgupK6FscAJjdZwxXkiVWGh0NOqD_QUqpYHfKpp27hmYztCYViwc1YBaTRGHLERBJMMbAZq-4MZJWGLqcbl5Xo0RjI0bqHqLUYoDOcQMO5dvZpJZQnOM4vjXVVsvA9U1QI5hVf9q0uWB04bAhIEnCXg4IHjpVp8sysn3_74PZ1CDbGKB1jZWUnvlvw8LmQALidhvQVpnDz7Xx3o5EU1mkHuoqaqM7Jvly5pnAju-0yx2i4rj8TirxNz_KdLjLbjidWzvgapzwedgBaVgNUiRRZRkeLGETOfXbxJ9ZKpkKRVln00Yc8pZXPi3JNWLL0sirCIxgtcnLyVCWBhXKZDRAbs4nyVUVx0s_SLV4yUxqtfMU5G7e1hO-omGiDmrx0svHx8YHzYOeNc3_JHo0Xz0WB1Bnfwgf7cINGS_b0116mG8cVqUpJVofa1TPcWnv0TuAGV8ceSU4AdMj4oWptoWbfzo1ZFjOcL9P-4Xq3YJ286jGGNnQy0Ko85NSohFoSGWi2JI-VBQWG1pt1YDZbciemBgTn3hLOXyj0kqdd_pURJf_Zd7mcMVpSZCGHY6tKtukUqWO64TyGSTdQ_T_mIkstUGRKUlHmMq7usyzmbYEncUA3gg_1piY30xo&ogV=-2",
                                "ozon" : "https://www.ozon.ru/product/magicheskaya-bitva-kn-3-komandnyy-boy-chernaya-vspyshka-akutami-gege-740942487/?at=x6tPn2Xy4HRxoo6WF52AM9yFWYp2K9t5r7r9NhPj556p",
                                "wildberries" : "https://www.wildberries.ru/catalog/243939864/detail.aspx?targetUrl=SG"
                            }
                    },
              "4" : { "info" : "Отлично, вы выбрали 4 том манги 'Магическая битва. Кн. 4. Начало повиновения. Пагубный талант. | Акутами Гэгэ'!",
                      "photo" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\Fourth_Tom.jpg",
                      "urls" : { "yandex" : "https://market.yandex.ru/card/manga-magicheskaya-bitva-kniga-4-nachalo-povinoveniya-pagubnyy-talant/103060437487?do-waremd5=QuytUPaeShzu7STl5Ip6-A&cpc=7fmEAPl6RgfAPhT4bTj3iYH4hpDCGoVYOqPtOWoKC8Oo8ZnOnyH7lMumfFHv-MB4WyqPy49d9SPDtCeNoCT3pSrmQ4cByJqtosep8MQWuA9G9wytRAAqq7pNvgCY2BAhSyMai9zdlgWp-Hz9nx4vQQwo3L8l8txYchAngbSb6X1cPlHFf2ByHOTE8SBQPymxFWXZhH-GDu6irI5PZK_WswatVEv77Wt8d2glhSHpztagpQehAqxO10iYieJHCLCfY9ocH0gIFwoYgF_qiLt4zpUlJuG521s-YzyQmYcunZ3Xx18kctaBuIUU0dBoDnQGPxQ3Qso43Xk5O_48YcXk56aqkuUuiEx7A4zLglkdoDgNMQMHNDU2MRw-5eieR0_FMsecCYHRtYgzGL4W58b0LGGZEggE_ar1iGvmWPi-3LDm9m3vWNeTh8GfvB7FdcHpGWYaJv00_cS_MuJZ7MfF7LboWWjtlPhhkGPb-mpytk1R4fg5u415RBPeTyUXKuVHCIgEG7s6KBQwwyknaR13fR9AcqK6Mnp_cPKXUelHbQkHw85Q5GuCAR4i1EkRKA_n1ooNnmkUeZV2bs-e2orp9LqzGDZZ0d0Ubp4XeZ1WgpTunsawScynLA%2C%2C&ogV=-2",
                                "ozon" : "https://www.ozon.ru/product/magicheskaya-bitva-kn-4-nachalo-povinoveniya-pagubnyy-talant-akutami-gege-818914312/?at=x6tPn2EKliN488kBtjMoBBYuYV6om5UQ7lj8mFn7R6OA",
                                "wildberries" : "https://www.wildberries.ru/catalog/189045024/detail.aspx?targetUrl=EX"
                            }
                    },
              "5" : { "info" : "Отлично, вы выбрали 5 том манги 'Магическая битва. Кн. 5. Таланты умирают молодыми. В преддверии праздника. | Акутами Гэгэ'!",
                      "photo" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\Fifth_Tom.jpg",
                      "urls" : { "yandex" : "https://market.yandex.ru/card/manga-magicheskaya-bitva-kniga-5-talanty-umirayut-molodymi-v-preddverii-prazdnika/102192159976?do-waremd5=eq9yG6kughBhWxOGtMcq6Q&cpc=7fmEAPl6RgdsvI6ADKA36peSTS8pv6O4y7vFxmkjED-Fyn4GCPRTogdo896A0HharjIibyAqshBzLdM1kT0GC5_qPIUjCt2JTeX0HestRc2UdvRvXrrlx8iHNdkCvo8OPYw7D2kLV5zws_Iak-59nAp3bfYYjSxYa_kVBYpkEfNeEyBJOsYZH0i7TTSsgV9H77ne6Ef5fZ080YyIq_9iMbwKxgFtuL9K2kNTPRhDK4oiup-Sh6poSh3IixPcllzi88wvZz_DIAGc192IWNgs-0sNBJaZa3llTIVmgRVV7aMJ64Sde0MObbV75jw4iNUx2jiQLnpJq3ImVHvu2KsjdgpoL1DP-VQnQsXfw-3xJE1QeAETpqmQMyAvKS2h-o_alK9KAK5gkft8xkKpjQ96e9v394FLEM2kTWR4zjmV9btVnvHPdbrPge2bsWN9LPhMnZ-k_mK0KnTdykuL5lrooAj5kVgLjr52CgM1qaJrF95F1jnD9ewd3xdbaSWDgUdkFltNjPbJy3A3xxa12i25Pt5abMxeKz1u-2IdNXsANDMJXM5INmYrKLXURgLOBtmcGpGSBs2HgdMlq7B2w5w0sKxb-3vELfOj&ogV=-2",
                                "ozon" : "https://www.ozon.ru/product/magicheskaya-bitva-kn-5-talanty-umirayut-molodymi-v-preddverii-prazdnika-akutami-gege-852887634/?at=79tn4ORvxTXN3jL8fwQ00NwFAJEEE5UzQrWgwFQY6Xgj",
                                "wildberries" : "https://www.wildberries.ru/catalog/188845393/detail.aspx?targetUrl=EX"
                            }
                    },
              "6" : { "info" : "Отлично, вы выбрали 6 том манги 'Магическая битва. Кн. 6. Инцидент в Сибуе : Открыть врата. Спиритизм. | Акутами Гэгэ'!",
                      "photo" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\Sixth_Tom.jpg",
                      "urls" : { "yandex" : "https://market.yandex.ru/card/manga-magicheskaya-bitva-kniga-5-talanty-umirayut-molodymi-v-preddverii-prazdnika/102192159976?do-waremd5=eq9yG6kughBhWxOGtMcq6Q&cpc=7fmEAPl6RgdsvI6ADKA36peSTS8pv6O4y7vFxmkjED-Fyn4GCPRTogdo896A0HharjIibyAqshBzLdM1kT0GC5_qPIUjCt2JTeX0HestRc2UdvRvXrrlx8iHNdkCvo8OPYw7D2kLV5zws_Iak-59nAp3bfYYjSxYa_kVBYpkEfNeEyBJOsYZH0i7TTSsgV9H77ne6Ef5fZ080YyIq_9iMbwKxgFtuL9K2kNTPRhDK4oiup-Sh6poSh3IixPcllzi88wvZz_DIAGc192IWNgs-0sNBJaZa3llTIVmgRVV7aMJ64Sde0MObbV75jw4iNUx2jiQLnpJq3ImVHvu2KsjdgpoL1DP-VQnQsXfw-3xJE1QeAETpqmQMyAvKS2h-o_alK9KAK5gkft8xkKpjQ96e9v394FLEM2kTWR4zjmV9btVnvHPdbrPge2bsWN9LPhMnZ-k_mK0KnTdykuL5lrooAj5kVgLjr52CgM1qaJrF95F1jnD9ewd3xdbaSWDgUdkFltNjPbJy3A3xxa12i25Pt5abMxeKz1u-2IdNXsANDMJXM5INmYrKLXURgLOBtmcGpGSBs2HgdMlq7B2w5w0sKxb-3vELfOj&ogV=-2",
                                "ozon" : "https://www.ozon.ru/product/magicheskaya-bitva-kn-6-intsident-v-sibue-otkryt-vrata-spiritizm-akutami-gege-953899853/?at=WPtNRArvETKjJ0knfoZm30Wi43YvGBFZEqXQvFk4jnwz",
                                "wildberries" : "https://www.wildberries.ru/catalog/189049276/detail.aspx?targetUrl=EX"
                            }
                    },
              "7" : { "info" : "Отлично, вы выбрали 7 том манги 'Магическая битва. Кн. 7. Инцидент в Сибуе : Раскат грома. Правый и неправый. | Акутами Гэгэ'!",
                      "photo" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\Seventh_Tom.jpg",
                      "urls" : { "yandex" : "https://market.yandex.ru/card/magicheskaya-bitva-jujutsu-kaisen-kniga-7-tom-13-14-intsident-v-sibuye-raskat-groma-pravyy-i-nepravyy/4570125333?do-waremd5=e8nEhSk_PRQmMBusdChWXg&sponsored=1&cpc=7gMqwolVgupOSbbrZCtBpRUS_V-F4raLBU7xTPA7QdB09Zv8-b8iAXeA683e1aYSvC2TsJAsEzEz0CG6hxGgwXVg-AZvoo_Z-nI2vIyHId-JPKT4IDSWcCpEhhEc0zCRFqG397HOLupXiar-CfO6wS53QopT_SQqXNCpBC_0dykZlWm93aUcvnxqiMEKPFTsPZIETHjYfU9aQMZjjrK_8y_Ry_OjbiZaBsUVn-f1q380NlZk-24mezrdOQsTo7KK3pQaafBxGzXnKhgsrXA6KwgCfh_wu-i6Jnm6fVMxaSF9fNVNPlQXMxvOPeLzNDG-SsxrmnjARCQXJLYvLsco2GybB1_LC4NSGGVHFsrMys36sNfbJqO-nOQL8y3aXCjMbD3DcA_zXMKgZtyK109RDZpNtEfvZpusbnh2VnbJtZaiqgePmw5DPspTxeabqRbu7TAm0QEKymGiAkIdmcMUr1h4afk-doe_FV-kea0bQJCo_Ez8tBlwcVyG0Pe6QQB_JU7t0VyXY0XxHE_sXo56FetQIBDzF5Ln9VwByIyyOKb7SY9ZQZxdyKb2Zxt8wb_zp8qXgstz6g3GdomzrsNZCN6wjskFGTLs&ogV=-2",
                                "ozon" : "https://www.ozon.ru/product/magicheskaya-bitva-kn-7-intsident-v-sibue-raskat-groma-intsident-v-sibue-pravyy-i-nepravyy-957456384/?at=16tL27JK4U1Ky5ZEimAp1xJCLxoLxMCnNj63OijzyLJY",
                                "wildberries" : "https://www.wildberries.ru/catalog/187476862/detail.aspx?targetUrl=EX"
                            }
                    },
              "8" : { "info" : "Отлично, вы выбрали 8 том манги 'Магическая битва. Кн. 8. Инцидент в Сибуе: Трансформация. Закрыть врата. | Акутами Гэгэ'!",
                      "photo" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\Eighth_Tom.jpg",
                      "urls" : { "yandex" : "https://market.yandex.ru/card/manga-magicheskaya-bitva-kniga-8-intsident-v-sibuye-transformatsiya-zakryt-vrata/102180402170?do-waremd5=BbMzfKyCzYCWNgPUX5Z3kA&cpc=I32BRNvpAnAabYpiYE5pNBvwOr5kNfYHeVOyySX716Rzm2OPAsdohYXayBkE66X6zxxKwP3qSFa7WVwsbzH2rLefmCVyOQ8r31ymxzfpTfQ_bYqswyzJy7C5EF3XlofiJdv1El0Ja7UOJhHTw1UWuJ7B_RnD6dQ9SZxr7Lxo4q1VaqthrF4zhcGlD3x7BAcR-nfObJaOo3e_067FdcJm_S8BKY9wuOWlLHeGxr7gp2GaK-BOiHo8geQ4stvC0fgy87SlsgFqFD6C78kJ76ZNQZUE--EdEfcj1Sg4iuh2qPvJTwO7LOQRgknfz87_yOmXs01rgNshRjsFVFndmpa8GpKe-J1I31pMdB0BG9wCPjm3c6f9F3qWWFxhOzRvcaC14dJdfbUhnKK_tRggprijVaQFEhHIDCHsBmjcCZAZzDwTDq3ULHRdl_9MVY4PL3rYjjUd2iuXTBU5kfE_E-jIwjdShMGzbYmxuiPJnHYGV2OM95aQ09G6UOzPDf6tpGWJwDXV8SdEO_EYAsAXzAkoOXBYSuU4bCtImTR3qkvDxSnWMYLsPVEnnPrtGVMBWMsEkO-ongSg8zy9rf9oph_vVZgRPuelL-umMhhReih9iHeOd5G1hRvbzg%2C%2C&ogV=-2",
                                "ozon" : "https://www.ozon.ru/product/magicheskaya-bitva-kn-8-intsident-v-sibue-transformatsiya-intsident-v-sibue-zakryt-vrata-1063366063/?at=r2t4P5QXqH2jPqNyclQwDOnHLmVRyof7GQoD2S0Zq9nO",
                                "wildberries" : "https://www.wildberries.ru/catalog/190223297/detail.aspx?targetUrl=EX"
                            }
                    },
              "9" : { "info" : "Отлично, вы выбрали 9 том манги 'Магическая битва. Кн. 9. Перелетный гусь. Пламя. | Акутами Гэгэ'!",
                      "photo" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\Ninth_Tom.jpg",
                      "urls" : { "yandex" : "https://market.yandex.ru/card/manga-magicheskaya-bitva-kn-9-pereletnyy-gus-plamya-akutami-g/102486216544?do-waremd5=ZbmrC0z3-UAbufKLJHaLxw&sponsored=1&cpc=7fmEAPl6RgenQlhmpeM56OS-czoswL34bCaYfjYIjwB35RNLBKubQ-Yo82rztkwH-9b9FYOGfRQ8ruhwn44Ii0uwck03iUy0pA6qVkJDX-e58G57eS_KuG6zj0pNSRdkB5PZ70-58BhYa3VAcINAzF08-tGczsOQFh0NCwqxWWY3m0oe4-8NQKii3uA9ZWwQhyQTUXMfbUeng0TCYODK_EvrOVXOymuGQ3NwRBEsPzwlemkD2yWpR9lDiE82Ad_m0TeClWmB56LFZsLDoz3pNUGLFTrW77om_fH2gJ7eaD6KktHqRijm_V75EAbGrPfr9jSSYmml94i8hTca84fNB4fiR24MNcZ1Adi6FGog3kVlpfp4EgVUcVop7ZANCpUO9C8dxiINP5DUFI3lXaD1mPtFEj9gaJwe7aZjyn8O_ylXOVW0oftraS0Jd3CR59-owVD-K2K7-7G4iqethpE7ZYl2MpnL_ATVp_PqOsKzqjwI9ntsuGnPKwC_xuAZjYUy3tWm4l1x2aEwFl6Au_vS0M5-LcYP8twyj7eU-nRlQ0LVal4iADrfkPKRXW0omuMq9DQMgot3k8_ZX1qR8RklLtdqLjYGGvefp91h4ucJukL3PDgl9awtZOF5xvgCke_y&ogV=-2",
                                "ozon" : "https://www.ozon.ru/product/magicheskaya-bitva-kn-9-pereletnyy-gus-plamya-akutami-gege-1224057499/?at=jYtZK7okru99OL83uMl2J4PT6lxP1LuOGxqYYHwkW0rB",
                                "wildberries" : "https://www.wildberries.ru/catalog/190589181/detail.aspx?targetUrl=EX"
                            }
                    },
              "10" : { "info" : "Отлично, вы выбрали 10 том манги 'Магическая битва. Кн. 10. Колония Токио №1. Колония Сэндай. | Акутами Гэгэ'!",
                       "photo" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\Tenth_Tom.jpg",
                       "urls" : { "yandex" : "https://market.yandex.ru/card/manga-magicheskaya-bitva-kniga-10-koloniya-tokio--1-koloniya-senday-akutami-g/102834949144?do-waremd5=oCU5X3mJods8kPeeHwcOPg&sponsored=1&cpc=7fmEAPl6Rgc5xczSMrGW1wAoYWPmLIXWXKkR-iZqH4F46ueXYcvbuITHoohXrRvhZ2_49er-RsrtJAjwWfVJmqStf-c1nnVt_GcdywjF6iwoQI_wlL1cbITzRlbdK3wlM8SQxnHyn9NjJQBr4HpwxUrDhG8utMCYXAStuhDw0ojRwazyzPA-yCHhia6Sbox9SxseJo_626qKOsCl6ROxfYF0Ttqc-TxANrZEQRouFST9Rxz-kRbHoe8lgqeCy4k8EuzKRB8GR29I5i259N9RnPOe-n-jk2NhBvZidAQ6x8nNPjHmULknuA8e-eQqz_eyZHCDIDjRncHiQPHjcL4wUwq49Mf1XoFAxqmU85ZId3FRVdNH04m3DW-x3yKid1bjTvkp9XDdLhU7qBH4JDvNS6ravJEF0KVWpifY-CCb_dzVIhgTgPmLa3y0gOzIoaotq6ulG--jimncS0GMYBqyMgmSX4-pDxuyqeZT7WwHxjcwguFM-01xspvpPp98nHZq53odbXpYU6FMD3v98tgaaMvxbT9lyplcLISIo3fwmBLs9eLesxsBuU_kFvLwQ_3FLP_nlNFFo1SGjSVLtZRXLdK7h-iimGV1&ogV=-2",
                                 "ozon" : "https://www.ozon.ru/product/magicheskaya-bitva-kn-10-koloniya-tokio-1-glavy-162-180-akutami-gege-1389325275/?at=r2t4P5QXqHjqkGZLUrXvB4QhrB9PMKTvgNqL3S1joNZ2",
                                 "wildberries" : "https://www.wildberries.ru/catalog/214555321/detail.aspx?targetUrl=EX"
                             }
                    },
              "11" : { "info" : "Отлично, вы выбрали 11 том манги 'Магическая битва. Кн. 11. Колония Токио 2. Колония Сакурадзима. | Акутами Гэгэ'!",
                       "photo" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\Eleventh_Tom.jpg",
                       "urls" : { "yandex" : "https://market.yandex.ru/card/manga-magicheskaya-bitva-kniga-11-koloniya-tokio--2-koloniya-sakuradzima-akutami-g/103451654561?do-waremd5=J01CfXYLr3KVNKMJVAyAqQ&sponsored=1&cpc=7fmEAPl6RgflP-Lj8iHr_gA-pbe3n93umwCKc92-uX8wy9DRvJWJBeqroupkm_l0ND28mFjpZFg5sk82nqkvywqEUtQsT_EAmROLESui8x9yIf4R6aR9XnEzxW-wwmsCiAd1RtPHvLYhyKwynl7ucxy3kKE63Nk-4jT_jyrCbcHbNjTnIc4NJHWa-tQ_p4dLHsIOxyIpEPgVhArrChclgR-GTk69ySwp012euxtzveS_Qljd1prFboyh0q-0fCAgRgeq_ebBCuQerGkQKDTzilHDas20gsOB3V98KueYMSUgsqaKN555iX5QJx7a5J9rW9Wu00geGxeURdmyF0pThNlBfuFNg9swqFJxmqCF7kJvrtwlQOMTZoBTt0FfLcar9QiXABV0p35XA8maHveUov79KOsjpUXOb1N3jgmsB2-_U3RyJ4qMZE5fPy1O__-sXxysC3P-CBAzOOkJhhIp-8pks6QlFr06hgKLUhkTZ2p2CWCaWNSC6fVsWQ072DmLLMadSjcH8mrwwE4XEv0zQp11gOr7ZbwtmH0wIQeqWB_EE8CTBORRUB-TDPMRrRotxKb-vgSW-JiLdAR9B_eSUHgX8z_NbWCx&ogV=-2",
                                 "ozon" : "https://www.ozon.ru/product/magicheskaya-bitva-kn-11-koloniya-tokio-2-glavy-181-199-akutami-gege-1644316890/?at=jYtZK7okruAZoNJC7NYly1hV3zP7yt1ym20kTkQEMRL",
                                 "wildberries" : "https://www.wildberries.ru/catalog/284822066/detail.aspx"
                             }
                    },
              "12" : { "info" : "Отлично, вы выбрали 12 том манги 'Магическая битва. Кн. 12. Звезда и нефть. Проклятый плод : возвращение. | Акутами Гэгэ'!",
                       "photo" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\Twelfth_Tom.jpg",
                       "urls" : { "yandex" : "https://market.yandex.ru/card/manga-magicheskaya-bitva-kniga-12-zvezda-i-neft-proklyatyy-plod-vozvrashcheniye-akutami-g/103676891923?do-waremd5=5tKv53HJo9nW-LiR_gBH2w&cpc=7fmEAPl6Rgdp8txkxho0aCanqUvwZCb3r9TGuioFQdn4bL4MouN0Mb4Huk7_rZT2qodct_mbeijCMgr32ot748Hi800hZ3ZpGAM41gCqZxJ3Ta5twwyqfb7ZWm5zp-14zPd9rYwOhq8xa9_pTJSmij8cr0pR506SZwTYqZ7q1NMgZce-X08uEORvzsx_TtuDGj1oK6EelxL_s9jIiKnlGuAhGQqU1UDR3lxLLeNZ0CVW7c4lrxzFKLV94_iXGDpfzZIElc63qlf3Pa-DZQ4kgvdrcbGFD-0lIPz02aO_2CUoG--pVcvyz4Ux84TGLYnz07I-gtf0uslae90yJj9kAuvqbs-vz0l-_-L9bxFnhQMdHeLEaWleS0igNC-Q-clftB7aJCFmG3ZOxafSyrt4SxhtsjAyov7BuNb2Jeq2j1nqT4QshbWJjrxjvzDfqioJeH5SSyE2g7gYTigK_MGmngOjyxW6O_yyq8kTUQ2hiXLRXi2RUcBEk9C9JHer_AmHc99oW2LCrQZhL3M3Xvdp1RvD8PVeHg8UtpKylwln4NMMisIxfY5y8qCON0WHOnG-GasOSBPzMbEWEnurW11ERISCyEhqCxmcytEk52ooKgA9xs9Spw8PEg%2C%2C&ogV=-2",
                                 "ozon" : "https://www.ozon.ru/product/magicheskaya-bitva-kn-12-proklyatyy-plod-vozvrashchenie-g-200-217-akutami-gege-1758467377/?at=BrtzpgW3GhWDlo7GSLq7Qk2tvK9wpKIA2PyJlTEmoJjk",
                                 "wildberries" : "https://www.wildberries.ru/catalog/309757759/detail.aspx?targetUrl=EX"
                             }
                    },
              "13" : { "info" : "Отлично, вы выбрали 13 том манги 'Магическая битва. Кн. 13. Решающая битва в Синдзюку. На юг. | Акутами Гэгэ'!",
                       "photo" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\Thirteenth_Tom.jpg",
                       "urls" : { "yandex" : "https://market.yandex.ru/card/graficheskiye-romany-manga-magicheskaya-bitva-kn-13-reshayushchaya-bitva-v-sindzyuku-na-yug-akutami-gege/4399924607?do-waremd5=LjvFmx9Og9yORcs9bSMrYA&cpc=7gMqwolVgupM1FIfAAiYZcGjDAbgN-l4g96hlqVCdT9cd2mdZhCnqgWvwGvEirbbuHjLx-IlP8I4KDS6tKMBqp-nbejhWFqmMCCJWSfYaxq2YBSmndUx1Zjxq38WteO8lR4BGX-1O1H3P_v3VLEwaV7rdx-4sVahgFD_PZuKNj63EnrtPgx4agtM5QZtD1L0_NO3oKXWE_hDavp4cV49jq-PrbA8XPyBIBcapxjtd_KsTf4fBpPabNyCl9mOP5tzXBdpJsr-jO_ddb-mOmVguFN86fbA-LYJLQV3sQ3RCYVrcyL-OEmT07WNGHQLlfJNBNOiKs6bR3BRN1IjIUsycak6O6ZQY9uE4mQAcYSmIprJ-GIzliMExNU5N-AAIfUmY-LXbqSppSG7H9X03I1R0Fn0sTTm3pHLdesYApt2DM93RGudBlzzWgAqlB5IOFUqz860py6AHIVDn2qWg45Gy_dGioqiBzeimZwbX_96UmYEiM99wNsm_69F9UxMWXKej64oJcBI3jjrTSnMgmyM__m4NiGSgmU0OcGlWJmJi6afl1dmL5eI4tzQPapYEUKxvlCCSvQ_5I-QVbKB-CMR6MIKxR_-ijGbYcAl4CkuEDVWd9UCdoHPNA%2C%2C&ogV=-2",
                                 "ozon" : "https://www.ozon.ru/product/magicheskaya-bitva-kniga-13-reshayushchaya-bitva-v-sindzyuku-na-yug-limitirovannoe-izdanie-1917540387/?at=WPtNRArvETO57WwkI5ZKl0NiP7Lm56TJxxqzYiBzxP0Z",
                                 "wildberries" : "https://www.wildberries.ru/catalog/453806665/detail.aspx?targetUrl=EX"
                             }
                    },
              "14" : { "info" : "Отлично, вы выбрали 14 том манги 'Магическая битва. Кн. 14. Baka Survivor! Фора для отстающих. | Акутами Гэгэ'!",
                       "photo" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\Fourteenth_Tom.jpg",
                       "urls" : { "yandex" : "https://market.yandex.ru/card/graficheskiye-romany-manga-magicheskaya-bitva-kniga-14-baka-survivor-fora-dlya-otstayushchikh-akutami-gege/4506291044?do-waremd5=CWG6J-KrCwM1Anxet-0ZcA&sponsored=1&cpc=7gMqwolVgurCLiIsX95oIf7OqbQqe2irbLa-VRSq-RHSg0_BgFYGVzpHa0Ei8QTm8WZPQD_VtiMrItAjrAfYARHzGyMxE0ZTb7zjhSe7eCoH2HSq2O2eGBTKPHyVMZBDm93zSS_R6dpEyBS-E1328qpPKlQsSyJxq4lqP920A91_i_HyizObQR468mnjsuw6Oiigz3AA19tEGw3CpfJnQGwtSFE9AjAluyByFqZpzyVuxku06Ym4iKHrW7DVFaCIO-BldlpM7FArOAGlhlglaqSE6saCvfVJjbYKgPXKT3bUpPkjg6OSZpKajfAiY07GbMZAKAAk8UWmtYJJDC7cbK-UjVVWkMs8ezdodW1KhyiNhIQHSKMXvrrUZR0TNl8N8IOvtURwslbR72gyEPFv3ivld1dIQvMJx-tu7mJCsI--euT6yYZ_VZ9zC2xemO4CbnB59-KDM7GREyRTJ-ka9QIUGZhukoS-Fv7l7qvp7IaONRNrcq9ODzi-p5Qy_pC9eE-EYgpgDpIuEihLh3Qbb2hAqCK0LTWT9kT46Gk9j3yijBxjNzyAGw%2C%2C&ogV=-2",
                                 "ozon" : "https://www.ozon.ru/product/magicheskaya-bitva-kniga-14-baka-survivor-fora-dlya-otstayushchih-akutami-gege-2423230412/?at=ywtAqlOE1F69p07BTNRB03PtVl2ZNlHpVylGNSD46zqo",
                                 "wildberries" : "https://www.wildberries.ru/catalog/463572869/detail.aspx?targetUrl=EX"
                             }
                    }
             }

user_state = {} 

toms_photo_bytes = {}
for key, value in tom.items():
    with open(value["photo"], "rb") as f:
        toms_photo_bytes[key] = BytesIO(f.read())
        
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

@botJujutsuKaisen.message_handler(commands=['start'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name}</b>, привет!\nДанный бот отслеживает пополнение коллекции по манге 'Магическая битва', сохраняет последнюю прочитанную страницу для пользователя и сравнивает цены на маркетплейсах для экономной покупки. Желаете протестировать бота?"
  markup = types.InlineKeyboardMarkup()
  button_yes = types.InlineKeyboardButton(text = 'Да', callback_data='yes')
  button_no = types.InlineKeyboardButton(text = 'Нет', callback_data='no')
  markup.add(button_yes)
  markup.add(button_no)
  botJujutsuKaisen.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)
  
@botJujutsuKaisen.callback_query_handler(func=lambda call:True)
def response(function_call):
  if function_call.data == "yes":
        markup = types.InlineKeyboardMarkup()
        button_price = types.InlineKeyboardButton(text = 'Узнать цены на тома', callback_data='price')
        button_saving = types.InlineKeyboardButton(text = 'Сохранить страницу для продолжения чтения', callback_data='saving')
        button_reading = types.InlineKeyboardButton(text = 'Прогресс прочтения манги', callback_data='reading')
        markup.add(button_price, button_saving, button_reading)
        botJujutsuKaisen.send_message(function_call.message.chat.id, "Отлично, давайте изучать меню", reply_markup=markup)
  elif function_call.data == "no":
        botJujutsuKaisen.send_message(function_call.message.chat.id, "Ничего страшного, можете вернуться когда захотите")
  elif function_call.data == "price":
        botJujutsuKaisen.send_message(function_call.message.chat.id, "Теперь напишите номер тома манги")
  elif function_call.data == "choice_marketplace":
        markup = types.InlineKeyboardMarkup()
        button_yandex = types.InlineKeyboardButton(text = 'Yandex Market', callback_data='yandex_place')
        button_ozon = types.InlineKeyboardButton(text = 'Ozon', callback_data='ozon_place')
        button_wildberries = types.InlineKeyboardButton(text = 'Wildberries', callback_data='wildberries_place')
        markup.add(button_yandex, button_ozon, button_wildberries)
        botJujutsuKaisen.send_message(function_call.message.chat.id, "Теперь выберите маркетплейс", reply_markup=markup)
  elif function_call.data == "yandex_place":
        info = []
        key = user_state.get(function_call.message.chat.id)  
        soup = toms_soup[key]["yandex"]
        price_tag = soup.find('span', class_='ds-text_color_price-term')
        price_tag_1 = soup.find('span', class_='ds-text ds-text_weight_reg ds-text_color_text-secondary ds-text_typography_text ds-text_text_tight ds-text_text_reg')
        if price_tag and price_tag_1:
            price_1_rub = price_tag.get_text(strip=True)
            price_2_rub = price_tag_1.get_text(strip=True)
            info.append(f"Цена: {price_1_rub} рублей с картой 'Яндекс Пэй'" + "\n" + f"Цена: {price_2_rub} рублей без карты" + "\n" + "\n" + "Приятных покупок!)")
            botJujutsuKaisen.send_message(function_call.message.chat.id, info)
        else:
            botJujutsuKaisen.send_message(function_call.message.chat.id, "Цена не найдена 😢")
            
  elif function_call.data == "ozon_place":
        info = []
        key = user_state.get(function_call.message.chat.id)  
        soup = toms_soup[key]["ozon"]
        price_tag = soup.find('span', class_='tsHeadline600Large')
        if price_tag:
            price_1_rub = price_tag.get_text(strip=True)
            price_2_rub = 100
            info.append(f"Цена: {price_1_rub} рублей с 'Ozon картой'" + "\n" + f"Цена: {price_2_rub} рублей без карты")
            botJujutsuKaisen.send_message(function_call.message.chat.id, info)
        else:
            botJujutsuKaisen.send_message(function_call.message.chat.id, "Цена не найдена 😢")
            
  elif function_call.data == "wildberries_place":
    info = []
    key = user_state.get(function_call.message.chat.id)
    url_block = toms_soup[key]["wildberries"]
    product_identify = re.search(r"/catalog/(\d+)", str(url_block)).group(1)
    product_info = get_wb_price(product_identify)   
    if product_info:
        price_1_rub = product_info["price_discount"]
        price_2_rub = price_1_rub - round((product_info["site_price"] / 100) * 2)
        info.append(
            f"Цена со скидкой с WB кошельком: {price_2_rub} ₽\n"
            f"Цена без скидки: {price_1_rub} ₽\n"
        )
        info.append("Приятных покупок!)")
        botJujutsuKaisen.send_message(function_call.message.chat.id, "\n".join(info))
    else:
        botJujutsuKaisen.send_message(function_call.message.chat.id, f"Цена не найдена 😢")
  botJujutsuKaisen.answer_callback_query(function_call.id)
  
@botJujutsuKaisen.message_handler(func=lambda message: message.text in tom.keys())
def select_tom(message):
  photo = toms_photo_bytes[message.text]
  first_mess = tom[message.text]["info"]
  user_state[message.chat.id] = message.text
  markup = types.InlineKeyboardMarkup()
  button_choice = types.InlineKeyboardButton(text = 'Узнать цены на маркетплейсах', callback_data='choice_marketplace')
  markup.add(button_choice)
  photo.seek(0)
  botJujutsuKaisen.send_photo(message.chat.id, photo=photo, caption=first_mess, reply_markup=markup)
  
def get_wb_price(product_id: int):
    url = f"https://card.wb.ru/cards/v2/detail?appType=1&curr=rub&dest=-1255987&spp=30&ab_testing=false&nm={product_id}"
    response = requests.get(url)
    data = response.json()
    product = data["data"]["products"][0]
    size = product["sizes"][0]
    price_info = size["price"]
    return {
        "price_discount": price_info["product"] // 100,     
        "site_price": price_info["product"] // 100
    }
  
botJujutsuKaisen.infinity_polling()