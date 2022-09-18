from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *




app = ApplicationBuilder().token("5416890025:AAGHN2txjpTTzRPMuf-0N8rSCwpdEI7J1Q4").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
print("server start")
app.run_polling()