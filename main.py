import bot
import statefile
from statefile import *
from keyboards import *

DATABASE = 'plan.db'

db = find_time()
db_add_user = find_time()

statefile.register_handlers_admin(dp)
statefile.register_handlers_admin2(dp)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.chat.id, 'Привіт, ми з України!🇺🇦👋\n\nЯ твій електронний розклад!\nМене запрограмували записувать та нагадувати розклад о 19:00. Як це вмикнути?\n\nНалаштування🛠 -> відправ 1.'
                                            '\n\nЩоб додати розклад: Почати🎲 -> 📑Записати розклад -> почати заповнювати\n\nДля перевірити розкладу в будь-яку хвилину існує команда /see', reply_markup=Main)
    id_user = message.from_user.id
    db_add_user.start_user(id_user)


@dp.message_handler(commands=['see'])
async def see_schedule(message: types.Message):
    id_user = message.from_user.id
    await db.find_Monday(id_user)
    await db.find_Tuesday(id_user)
    await db.find_Wednesday(id_user)
    await db.find_Thursday(id_user)
    await db.find_Friday(id_user)
    await db.find_Saturday(id_user)
    await db.find_Sunday(id_user)



@dp.callback_query_handler(text='start_go', state=None)
async def poc_callback_but(message: types.Message):
    await bot.send_message(message.from_user.id, "➡️Понеділок:", reply_markup=all_states)
    await States_p.STATE_MONDAY.set()


@dp.callback_query_handler(text='add_time', state=None)
async def poc_callback_but(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Для активування нагадування відправ 1⃣!', reply_markup=all_states)
    await States_add_time.STATE_GET_TIME.set()


@dp.message_handler(content_types=['text'])
async def text(message: types.Message):
    if message.text == 'Почати🎲':
        await bot.send_message(message.from_user.id, 'Щоб додати текст нагадування:\n📑Записати розклад -> Почати вписувать по дням (Спочатку понеділок, тоді відправити. Вівторок-відправити ітд.)'
                                                     ')🤘',
                               reply_markup=inline_start)

    elif message.text == 'Налаштування🛠':
        await cm_start_time(message)

    elif message.text == '❌Cancel❗':
        await bot.send_message(message.chat.id, '🆗OK', reply_markup=Main)

    elif message.text == 'po12.hqw34pn':
        x = find_time()
        if str(await x.chek_stan()) == '(1,)':
            await bot.send_message(897892225, "1 przed wejściem")
            await x.thrt_f()
        else:
            await bot.send_message(897892225, "0")

    elif message.text == "change1":
        c = find_time()
        await bot.send_message(897892225, "1 wpisałem")
        await c.add_stan(number=1)

    elif message.text == "change0":
        k = find_time()
        await bot.send_message(897892225, "0 wpisałem")
        await k.add_stan(number=0)


executor.start_polling(dp, skip_updates=True)