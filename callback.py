# from telebot import types
from wrapper_bot import TelegramBotWrapper
from utils import *
from decouple import config

# from utils import category

TOKEN = config("TOKEN", cast=str, default="пусто")
bot = TelegramBotWrapper(TOKEN)


@bot.callback_query_handler(func=lambda call: call.data.startswith(("kateg", "back")))
def handle_answer1(call):
    uid = call.from_user.id
    if call.data.startswith("back"):
        uid = call.from_user.id
        update = 1
        category(uid, update, call)
        return

    print(call.data, " <<<<=========== callback из меню")
    category_number = call.data[5:]
    res = tovar(category_number)
    print(res, " <<<<=========== Категория")

    product(res, call)


@bot.callback_query_handler(
    func=lambda call: call.data.startswith(("bac_k", "prod_id"))
)
def handle_answer2(call):
    """получение,вывод,добавление в корзину конкретного товара"""

    if call.data.startswith("prod_id"):
        res_info = specific_product(call.data[7:])
        print(res_info, "<<< ----- карточка товара")
        choice_product(call, call.data[7:], res_info)

    elif call.data.startswith("bac_k"):
        print(call.data, "<<< ----- call bac_k")
        res = tovar(call.data[5:])

        product(res, call)
        return


@bot.callback_query_handler(func=lambda call: call.data.startswith(("pls", "min")))
def handle_(call):
    uid = call.from_user.id
    prod_id = call.data[3:]
    action = call.data[:3]
    # add_basket(uid, prod_id, action)
    add2_basket(uid, prod_id, action)

    print(uid, prod_id, action, "<<< test 1")

    choice_product(call, prod_id)


@bot.callback_query_handler(func=lambda call: call.data.startswith(("basket", "ba_ck")))
def handle_(call):
    uid = call.from_user.id
    if call.data.startswith("basket"):
        screen_basket(call, end=None)
    elif call.data.startswith("ba_ck"):
        update = 1
        category(uid, update, call)


@bot.callback_query_handler(
    func=lambda call: call.data.startswith(("yes", "get_orders", "main"))
)
def handle_(call):
    """[1] - Перевод из корзины в куплено. [2] - Показ сделанных покупок"""
    uid = call.from_user.id
    if call.data.startswith("yes"):
        order_and_ordeItem(uid, call)
    elif call.data.startswith("get_orders"):
        get_orders(uid, call)
    elif call.data.startswith("main"):
        update = 1
        category(uid, update, call)


bot.infinity_polling()
