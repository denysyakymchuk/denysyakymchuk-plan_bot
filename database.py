import asyncio
import datetime
import sqlite3 as sq
import bot
from bot import *
import re
from keyboards import Main


class find_time():
    def __init__(self):
        self.connection = sq.connect('plan.db')
        self.cursor = self.connection.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS `plat_table_bot`(
            id INT PRIMARY KEY UNIQUE,
            Monday TEXT,
            Tuesday TEXT,
            Wednesday TEXT,
            Thursday TEXT,
            Friday TEXT,
            Saturday TEXT,
            Sunday TEXT,
            time TINYINT)""")

        self.connection.commit()

    async def timing(self):
        with self.connection:
            self.cursor.execute("""SELECT id FROM `plan_table_bot`""")
            b = self.cursor.fetchall()
            self.connection.commit()

        b = list(b)
        i = 0

        while i < len(b):
            b[i] = re.sub(r'([()]*)', '', str(b[i]))
            b[i] = re.sub(r'([,]*)', '', str(b[i]))
            b[i] = re.sub(r"([']*)", "", str(b[i]))
            b[i] = re.sub(r'([;])', '\n', str(b[i]))

            try:
                self.cursor.execute(f'''SELECT `time` FROM `plan_table_bot` WHERE (id) = {str(b[i])}''')
                bul_time = self.cursor.fetchone()
            finally:
                self.connection.commit()

            bul_time = str(bul_time)
            bul_time = re.sub(r'([()]*)', '', str(bul_time))
            bul_time = re.sub(r'([,]*)', '', str(bul_time))
            bul_time = re.sub(r"([']*)", "", str(bul_time))
            bul_time = re.sub(r'([;])', '\n', str(bul_time))

            if str(bul_time) == '1':
                await self.find_Monday(id_user=b[i])
                await self.find_Tuesday(id_user=b[i])
                await self.find_Wednesday(id_user=b[i])
                await self.find_Thursday(id_user=b[i])
                await self.find_Friday(id_user=b[i])
                await self.find_Saturday(id_user=b[i])
                await self.find_Sunday(id_user=b[i])

            i = int(i) + 1

    async def thrt_f(self):
        while True:
            wremia = str(datetime.datetime.now())
            wremia = wremia[11:16]

            if str(wremia) == '16:00':
                await self.timing()
            await asyncio.sleep(60)

    def start_user(self, id_user):
        with self.connection:
            self.cursor.execute('''SELECT `id` FROM `plan_table_bot`''')
            a = self.cursor.fetchall()

        if str(a) == "[]":
            with self.connection:
                self.cursor.execute(f'''INSERT INTO `plan_table_bot` (id) VALUES ({id_user})''')
        else:
            counter = 0
            id_user = str(id_user)
            id_user_loc = str("("+id_user+",)")
            for i in a:
                if str(id_user_loc) == str(i):
                    break
                else:
                    counter += 1
                    if len(a) == int(counter):
                        with self.connection:
                            self.cursor.execute(f'''INSERT INTO `plan_table_bot` (id) VALUES ({id_user})''')
                    else:
                        pass

    def add_user(self, id_user, message):
        try:
            self.cursor.execute(f"""UPDATE `plan_table_bot` SET time = '{message}' WHERE id = '{id_user}' """)
        finally:
            self.connection.commit()


    def add_monday(self, data_para, id_user):
        try:
            return self.cursor.execute(f'''UPDATE plan_table_bot SET Monday = '{data_para}' WHERE id = '{id_user}' ''')
        finally:
            self.connection.commit()

    def add_tuesday(self, data_para, id_user):
        try:
            return self.cursor.execute(f'''UPDATE plan_table_bot SET Tuesday = '{data_para}' WHERE id = '{id_user}' ''')
        finally:
            self.connection.commit()

    def add_wednesday(self, data_para, id_user):
        try:
            return self.cursor.execute(
                f'''UPDATE plan_table_bot SET Wednesday = '{data_para}' WHERE id = '{id_user}' ''')
        finally:
            self.connection.commit()

    def add_thursday(self, data_para, id_user):
        try:
            return self.cursor.execute(
                f'''UPDATE plan_table_bot SET Thursday = '{data_para}' WHERE id = '{id_user}' ''')
        finally:
            self.connection.commit()

    def add_friday(self, data_para, id_user):
        try:
            return self.cursor.execute(f'''UPDATE plan_table_bot SET Friday = '{data_para}' WHERE id = '{id_user}' ''')
        finally:
            self.connection.commit()

    def add_saturday(self, data_para, id_user):
        try:
            return self.cursor.execute(
                f'''UPDATE plan_table_bot SET Saturday = '{data_para}' WHERE id = '{id_user}' ''')
        finally:
            self.connection.commit()

    def add_sunday(self, data_para, id_user):
        try:
            return self.cursor.execute(f'''UPDATE plan_table_bot SET Sunday = '{data_para}' WHERE id = '{id_user}' ''')
        finally:
            self.connection.commit()

    async def find_Monday(self, id_user):
        try:
            self.cursor.execute(f'''SELECT `Monday` FROM `plan_table_bot` WHERE (id) = {id_user}''')
            content_list = self.cursor.fetchone()

            content_list = re.sub(r'([()]*)', '', str(content_list))
            content_list = re.sub(r'([]]*)', '', str(content_list))
            content_list = re.sub(r"([']*)", "", str(content_list))
            content_list = re.sub(r'([;])', ' ', str(content_list))

            if content_list == 'None,':
                await bot.send_message(id_user, "▫Понеділок: ❌Ти не записав дані, або це просто помилка🤷")
            else:
                await bot.send_message(id_user, "▫Понеділок: " + content_list)

        except Exception as ex:
            await bot.send_message(id_user, "Щось пішло не так :(", reply_markup=Main)
        finally:
            self.connection.commit()

    async def find_Tuesday(self, id_user):
        try:
            self.cursor.execute(f'''SELECT `Tuesday` FROM `plan_table_bot` WHERE (id) = {id_user}''')
            content_list = self.cursor.fetchone()

            content_list = re.sub(r'([()]*)', '', str(content_list))
            content_list = re.sub(r'([]]*)', '', str(content_list))
            content_list = re.sub(r"([']*)", "", str(content_list))
            content_list = re.sub(r'([;])', '', str(content_list))

            if content_list == 'None,':
                await bot.send_message(id_user, "▫Вівторок: ❌Ти не записав дані, або це просто помилка🤷")
            else:
                await bot.send_message(id_user, "▫Вівторок: " + content_list)

        except:
            await bot.send_message(id_user, "Щось пішло не так :(", reply_markup=Main)
        finally:
            self.connection.commit()

    async def find_Wednesday(self, id_user):
        try:
            self.cursor.execute(f'''SELECT `Wednesday` FROM `plan_table_bot` WHERE (id) = {id_user}''')
            content_list = self.cursor.fetchone()

            content_list = re.sub(r'([()]*)', '', str(content_list))
            content_list = re.sub(r'([]]*)', '', str(content_list))
            content_list = re.sub(r"([']*)", "", str(content_list))
            content_list = re.sub(r'([;])', '', str(content_list))

            if content_list == 'None,':
                await bot.send_message(id_user, "▫Середа: ❌Ти не записав дані, або це просто помилка🤷")
            else:
                await bot.send_message(id_user, "▫Середа: " + content_list)

        except:
            await bot.send_message(id_user, "Щось пішло не так :(", reply_markup=Main)
        finally:
            self.connection.commit()

    async def find_Thursday(self, id_user):
        try:
            self.cursor.execute(f'''SELECT `Thursday` FROM `plan_table_bot` WHERE (id) = {id_user}''')
            content_list = self.cursor.fetchone()

            content_list = re.sub(r'([()]*)', '', str(content_list))
            content_list = re.sub(r'([]]*)', '', str(content_list))
            content_list = re.sub(r"([']*)", "", str(content_list))
            content_list = re.sub(r'([;])', '', str(content_list))

            if content_list == 'None,':
                await bot.send_message(id_user, "▫Четвер: ❌Ти не записав дані, або це просто помилка🤷")
            else:
                await bot.send_message(id_user, "▫Четвер: " + content_list)

        except:
            await bot.send_message(id_user, "Щось пішло не так :(", reply_markup=Main)
        finally:
            self.connection.commit()

    async def find_Friday(self, id_user):
        try:
            self.cursor.execute(f'''SELECT `Friday` FROM `plan_table_bot` WHERE (id) = {id_user}''')
            content_list = self.cursor.fetchone()

            content_list = re.sub(r'([()]*)', '', str(content_list))
            content_list = re.sub(r'([]]*)', '', str(content_list))
            content_list = re.sub(r"([']*)", "", str(content_list))
            content_list = re.sub(r'([;])', '', str(content_list))

            if content_list == 'None,':
                await bot.send_message(id_user, "▫П'ятниця: ❌Ти не записав дані, або це просто помилка🤷")
            else:
                await bot.send_message(id_user, "▫П'ятниця: " + content_list)

        finally:
            self.connection.commit()

    async def find_Saturday(self, id_user):
        try:
            self.cursor.execute(f'''SELECT `Saturday` FROM `plan_table_bot` WHERE (id) = {id_user}''')
            content_list = self.cursor.fetchone()

            content_list = re.sub(r'([()]*)', '', str(content_list))
            content_list = re.sub(r'([]]*)', '', str(content_list))
            content_list = re.sub(r"([']*)", "", str(content_list))
            content_list = re.sub(r'([;])', '', str(content_list))

            if content_list == 'None,':
                await bot.send_message(id_user, "▫Субота: ❌Ти не записав дані, або це просто помилка🤷")
            else:
                await bot.send_message(id_user, "▫Субота: " + content_list)

        except:
            await bot.send_message(id_user, "Щось пішло не так :(", reply_markup=Main)
        finally:
            self.connection.commit()

    async def find_Sunday(self, id_user):
        try:
            self.cursor.execute(f'''SELECT `Sunday` FROM `plan_table_bot` WHERE (id) = {id_user}''')
            content_list = self.cursor.fetchone()

            content_list = re.sub(r'([()]*)', '', str(content_list))
            content_list = re.sub(r'([]]*)', '', str(content_list))
            content_list = re.sub(r"([']*)", "", str(content_list))
            content_list = re.sub(r'([;])', '', str(content_list))

            if content_list == 'None,':
                await bot.send_message(id_user, "▫Неділя: ❌Ти не записав дані, або це просто помилка🤷")
            else:
                await bot.send_message(id_user, "▫Неділя: " + content_list)

        except:
            await bot.send_message(id_user, "Щось пішло не так :(", reply_markup=Main)
        finally:
            self.connection.commit()