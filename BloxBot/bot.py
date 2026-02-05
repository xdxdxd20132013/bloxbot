from aiogram import Bot, Dispatcher, executor, types

TOKEN = "8562135813:AAFAnD3lQ3Aez_om7e-QHpsHp08tY2RB0rs"
OWNER_LINK = "https://t.me/Crew_deddomik"
TWINK_LINK = "https://t.me/Crew_deddomik"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=5)

    for i in range(0, 31):
        keyboard.insert(
            types.InlineKeyboardButton(
                text=f"{i}M",
                callback_data=f"bounty_{i}"
            )
        )

    await message.answer(
        "🔥 Вибери свій Bounty (млн):",
        reply_markup=keyboard
    )


@dp.callback_query_handler(lambda c: c.data.startswith("bounty_"))
async def check_bounty(callback: types.CallbackQuery):
    bounty = int(callback.data.split("_")[1])

    if bounty < 6:
        await callback.message.answer(
            "❌ На жаль, мінімальний bounty для вступу — 6M"
        )
    else:
        await callback.message.answer(
            f"✅ Ви підходите для клану!\n\n"
            f"📌 Ваш bounty: {bounty}M\n\n"
            f"👉 Напишіть власнику клану:\n"
            f"{OWNER_LINK}\n\n"
            f"👉 Або твінк:\n"
            f"{TWINK_LINK}"
        )

    await callback.answer()


if __name__ == "__main__":
    executor.start_polling(dp)

