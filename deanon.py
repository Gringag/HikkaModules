# ---------------------------------------------------------------------------------
# Name: sunavadox
# Description: Your Best doxing tool!
# Author: @icansuck
# ---------------------------------------------------------------------------------
# 🔒    Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# ---------------------------------------------------------------------------------
# Author: @icansuck
# Commands: gb
# scope: hikka_only
# meta developer: @icansuck
# meta banner: https://mods.codrago.top/banners/DoxTool.png
# meta pic: https://0x0.st/s/QeZGoQSDvJ2RILRMUOjzfg/8KPc.webp
# ---------------------------------------------------------------------------------

__version__ = (1, 0, 0)

from telethon.tl.types import Message # type: ignore
from .. import loader, utils
import asyncio, random

@loader.tds
class dox(loader.Module):
    """сын докса"""
    
    strings = {
    "name": "sunavadox",
    "gb_1": "Searching for the victim's number...",
    "gb_2": "Searching for the victim's address and name...",
    "gb_3": "Searching for parents...",
    "gb_4": "Searching for a school...",
    "gb_5": "Finding parents' jobs...",
    "gb_r": "you've been doxxed\n\n├ Phone: wrecked\n├ Country: normal\n├ Region: of liars\n├ Parents: soon will be gone\n├ Address: a ditch on Arbat\n├ Name: why were you born\n├ Middle name: missing\n├ Surname: missing\n├ How many times screwed: 32\n├ Gender: linoleum\n├ House: a ditch on Arbat\n├ Sucks per day: 20 (times) for 10 rub\n├ Hospital: not allowed in\n├ Poop color: none, doesn’t eat\n├ Prostate: massaged\n├ Mouth: ruined\n└ #####################\n\nMother: a prostitute\nMother’s workplace: the highway\nCountry: in the CIS\nCity: how should I know?\nBorn: somewhere under a fence\n\nFather: a homeless\nWorkplace: begging on the street\nCountry: in the CIS\nCity: how should I know?\nBorn: in the sewers\nSchool: of fools",
    "info": "вывывыыв @icansuck"
    }
    strings_ru = {
    "name": "sunavadox",
    "gb_1": "Поиск номера жертвы...",
    "gb_2": "Поиск адреса и имени жертвы...",
    "gb_3": "Поиск родителей...",
    "gb_4": "Поиск школы...",
    "gb_5": "Поиск работы родителей...",
    "gb_r": "Тебя сдеонили, еблан\n\n├ Телефон: разъебанный\n├ Страна: обычная\n├ Регион: пиздоболов\n├ Родители: скоро не будет\n├ Адрес: канава на Арбате\n├ Имя: нахуй ты родился\n├ Отчество: отсутствует\n├ Фамилия: отсутствует\n├ Сколько раз ебали в дырку: 32\n├ Пол: ленолиум\n├ Дом: канава на Арбате\n├ Сосёт в день: 20 (раз) за 10 руб\n├ Больница: не пускают\n├ Цвет говна: нету, ибо не хавает\n├ Простата: массирована\n├ Рот: выебан\n└ #####################\n\nМать: шлюха\nМесто работы матери: трасса\nСтрана: состоящаяся в СНГ\nГород: я ебу?\nРодилась: где-то под забором\n\nОтец: бомж,\nМесто работы: на улице бичевать, просить мелочь\nСтрана: состоящаяся в СНГ\nГород: я ебу?\nРодился: в канализации\nШкола: далбоебов",
    "info": "ыывыыовы @icansuck"
    }


    
    async def gbcmd(self, message):
        """search in databases eye of god!"""
        await utils.answer(message, self.strings["gb_1"])
        await asyncio.sleep(1)
        await message.edit(self.strings["gb_2"])
        await asyncio.sleep(1)
        await message.edit(self.strings["gb_3"])
        await asyncio.sleep(1)
        await message.edit(self.strings["gb_4"])
        await asyncio.sleep(1)
        await message.edit(self.strings["gb_5"])
        await asyncio.sleep(1)
        await message.edit(self.strings["gb_r"])

    async def deanoncmd(self, message):
        """Full information of user in global database"""
        deanon = ["zzzz vzzvzv", "zovzozocoxovoix"]
        await utils.answer(message, random.choice(deanon))

    async def dinfocmd(self, message):
        """info of module"""
        await utils.answer(message, self.strings["info"])
