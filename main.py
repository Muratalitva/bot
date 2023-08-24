from alogram import Bot, Dispatcher, types, executor

bot = Bot(token='6380274513:AAGTSYZHC3LXRwTH_G51d46nrfrkgLNjaE4')
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer('Привет это бот для Визион групп.Чем могу помочь?\nИнформация о нас - /about_us\nОбьекты - /info\nКонтакты - /contacts ')

@dp.message_handler(commands='/about_us')
async def command_go(message:types.Message):
    await message.answer('https://vg-stroy.com/about/')

@dp.message_handler(commands='/info')
async def hello(message:types.Message):
    await message.answer('ЖК Визион Комфорт в Оше м2 от 43 891 сом Визион Групп Адрес ул. Салиева')

@dp.message_handler(commands='/contacts')
async def testing(message:types.Message):
    await message.answer('https://vg-stroy.com/contacts/')

executor.start_polling(dp)
