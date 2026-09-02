import os
import time
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, filters

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
START_TIME = time.time()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔍 OSINT", callback_data="menu_osint")],
        [InlineKeyboardButton("🆔 NIK", callback_data="menu_nik")],
        [InlineKeyboardButton("📡 Tracking", callback_data="menu_track")],
        [InlineKeyboardButton("📊 History", callback_data="menu_history")]
    ]
    await update.message.reply_text(
        f"🔥 **ZERO TWO OSINT BOT**\n"
        f"═══════════════════\n"
        f"✅ AKTIF: {datetime.now().strftime('%H:%M:%S')}\n"
        f"⚡ SIAP DIGUNAKAN\n\n"
        f"PILIH MENU:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    
    menus = {
        "menu_osint": "🔍 **OSINT COMMANDS**\n/email <email>\n/username <user>\n/phone <nomor>\n/domain <domain>\n/scan <target>",
        "menu_nik": "🆔 **NIK COMMANDS**\n/nik <16_digit>\n/nik_track <nik> <int>",
        "menu_track": "📡 **TRACKING**\n/track <target> <int>\n/track_stop <target>",
        "menu_history": "📊 **HISTORY**\n/history - Lihat riwayat"
    }
    await query.edit_message_text(menus.get(data, "MENU TIDAK DITEMUKAN"), parse_mode="Markdown")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uptime = int(time.time() - START_TIME)
    hours = uptime // 3600
    minutes = (uptime % 3600) // 60
    await update.message.reply_text(
        f"⚡ **BOT STATUS**\n═══════════════════\n"
        f"🕐 UPTIME: {hours}J {minutes}M\n"
        f"📦 VERSION: ZERO TWO OSINT\n"
        f"✅ BOT AKTIF 24/7",
        parse_mode="Markdown"
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Gunakan /start untuk menu, DARLING.")

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CallbackQueryHandler(menu_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("🔥 ZERO TWO OSINT BOT AKTIF DI RENDER")
    app.run_polling(allowed_updates=["message", "callback_query"])

if __name__ == "__main__":
    main()
