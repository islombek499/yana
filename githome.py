from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "8570391959:AAFkzbp-F5Z8YywRqZS1OmGb5C-LAtOj1ns"


async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.new_chat_members:
        return

    group_name = update.message.chat.title

    for user in update.message.new_chat_members:
        mention = f"@{user.username}" if user.username else user.first_name

        text = (
            f"👋 Salom {mention}!\n\n"
            f"🎉 «{group_name}» guruhiga xush kelibsiz!\n"
            f"📌 Guruh qoidalariga amal qiling."
        )

        await update.message.reply_text(text)


async def goodbye(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.left_chat_member:
        return

    user = update.message.left_chat_member
    mention = f"@{user.username}" if user.username else user.first_name

    text = (
        f"😔 {mention} guruhni tark etdi.\n"
        f"🙏 Sizni yana kutib qolamiz!"
    )

    await update.message.reply_text(text)


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome)
    )
    app.add_handler(
        MessageHandler(filters.StatusUpdate.LEFT_CHAT_MEMBER, goodbye)
    )

    print("🤖 Bot ishga tushdi...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
