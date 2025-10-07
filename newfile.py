import telegram
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import random
import time

# BURAYA KENDİ BOT TOKEN'İNİZİ GİRİN
TOKEN = "8220629835:AAFr5U1-iWJwR0QxZZ-k0Vi3yD-OpbwmEcs" 
# NOT: Yukarıdaki token'i test amaçlı kullanabilirsiniz, ancak gerçek botunuz için BotFather'dan yeni bir tane alın.

kisi_veritabani = [
    {"numara": "5312345678", "ad": "Ahmet", "soyad": "Yılmaz", "sehir": "İstanbul", "yas": "35"},
    # ... (Diğer veritabanı kayıtları)
    {"numara": "5301234567", "ad": "Sema", "soyad": "Kurt", "sehir": "Diyarbakır", "yas": "37"}
]

# Ana Menü Butonları
ANA_MENU_KLAVYE = [
    [KeyboardButton("📞 Numara Sorgu"), KeyboardButton("🌐 IP Sorgu")],
    [KeyboardButton("❓ Yardım")]
    # Güvenlik nedeniyle "SMS Bomber" butonu eklenmemiştir.
]
reply_markup = ReplyKeyboardMarkup(ANA_MENU_KLAVYE, resize_keyboard=True, one_time_keyboard=False)


# --- KOMUT İŞLEYİCİLERİ ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/start komutu geldiğinde çalışır."""
    await update.message.reply_text(
        "🇹🇷 **SORGULAMA BOTUNA HOŞ GELDİNİZ!**\n\n"
        "Aşağıdaki butonları kullanarak işlem yapabilirsiniz.",
        reply_markup=reply_markup,
        parse_mode=telegram.constants.ParseMode.MARKDOWN
    )

async def numara_sorgu_komut(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Numara Sorgu butonuna basıldığında veya 'Numara Sorgu' mesajı geldiğinde çalışır."""
    
    # Bu kısımda gerçek bir sorgu yerine, terminaldeki rastgele sonuç mantığı kullanılır.
    if random.random() > 0.3:  # %70 ihtimal bulunsun
        kisi = random.choice(kisi_veritabani)
        sonuc = (
            "✅ **KAYIT BULUNDU!**\n"
            f"📱 Numara: `{kisi['numara']}`\n"
            f"👤 Ad Soyad: **{kisi['ad']} {kisi['soyad']}**\n"
            f"🏙️ Şehir: {kisi['sehir']}\n"
            f"🎂 Yaş: {kisi['yas']}"
        )
    else:
        sonuc = "❌ **KAYIT BULUNAMADI!**\n"
        
    await update.message.reply_text(sonuc, parse_mode=telegram.constants.ParseMode.MARKDOWN)


async def ip_sorgu_komut(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """IP Sorgu butonuna basıldığında veya 'IP Sorgu' mesajı geldiğinde çalışır."""
    
    # Fake IP bilgileri (Terminal kodunuzdaki gibi)
    sehirler = ["İstanbul", "Ankara", "İzmir", "Bursa", "Antalya"]
    isp_list = ["Turkcell", "Vodafone", "Türk Telekom", "Superonline"]
    
    ip = "192.168.1.1" # Örnek bir IP adresi
    
    sonuc = (
        "✅ **IP BİLGİLERİ BULUNDU!**\n"
        "_(Bu bilgiler gösterim amaçlıdır.)_\n"
        f"🌐 IP: `{ip}`\n"
        f"🏙️ Şehir: {random.choice(sehirler)}\n"
        f"🏢 ISP: {random.choice(isp_list)}\n"
        f"📍 Lokasyon: {random.randint(36,42)}.{random.randint(100,999)}, {random.randint(26,45)}.{random.randint(100,999)}\n"
        f"🔒 Güvenlik: Orta Seviye"
    )
    
    await update.message.reply_text(sonuc, parse_mode=telegram.constants.ParseMode.MARKDOWN)


async def yardim_komut(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Yardım butonuna basıldığında çalışır."""
    await update.message.reply_text(
        "Yardım menüsü:\n"
        "- **Numara Sorgu**: Veritabanındaki rastgele bir kişiyi simule eder.\n"
        "- **IP Sorgu**: Rastgele IP bilgileri döndürür."
    )


# --- MAIN FONKSİYONU ---

def main() -> None:
    """Botu çalıştıran ana fonksiyon."""
    
    # Uygulamayı oluştur
    application = Application.builder().token(TOKEN).build()

    # Komut işleyicilerini ekle
    application.add_handler(CommandHandler("start", start))
    
    # Mesaj işleyicilerini ekle (Buton isimleri mesaj olarak gelir)
    application.add_handler(MessageHandler(filters.Regex("^📞 Numara Sorgu$"), numara_sorgu_komut))
    application.add_handler(MessageHandler(filters.Regex("^🌐 IP Sorgu$"), ip_sorgu_komut))
    application.add_handler(MessageHandler(filters.Regex("^❓ Yardım$"), yardim_komut))

    # Botu başlat
    print("Bot çalışıyor... Çıkış için CTRL+C yapın.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
