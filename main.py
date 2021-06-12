import os
import telebot

my_secret = "1695299416:AAFAb8eV86QcwU6mZx3spT_SgGcC9XGWAJw"
bot = telebot.TeleBot(my_secret)


@bot.message_handler(commands=['start'])
def start(message):
	bot.reply_to(message, "Welcome to Academic Advisor Bot مرحبا بك في المشرف الاكاديمي الالكتروني \n كل ماتحتاجه عزيزي الطالب من دليل الطالب و دليل التسجيل الالكتروني ودليل التعليم الالكتروني ستجده هنا\n فقط عليك اختيار الأمر من القائمة")


@bot.message_handler(commands=['hello'])
def hello(message):
	bot.send_message(message.chat.id, "مرحبا بك")
	
@bot.message_handler(commands=['contacts'])
def contacts(message):
  bot.reply_to(message, "FMCS 2021 \n http://fmcs.uofg.edu.sd \n https://t.me/aljemabi")
  
@bot.message_handler(commands=['regdaleel'])
def regdaleel(message):
  bot.reply_to(message, "من فضلك قم بتحميله من هذا الرابط \n http://registration.uofg.edu.sd/pdf/Students-ERegGuide.pdf")

@bot.message_handler(commands= ['daleel'])
def daleel(message):
  bot.reply_to(message, "من فضلك قم بتحميله من هذا الرابط \n http://registration.uofg.edu.sd/pdf/studentdalil42.pdf")

@bot.message_handler(commands= ['learndaleel'])
def learndaleel(message):
  bot.reply_to(message , "من فضلك قم بتحميله من هذا الرابط \n http://registration.uofg.edu.sd/pdf/Student%20ManualMoodle.pdf")
 
@bot.message_handler(commands=['studentapp'])
def studentapp(message):
  bot.reply_to(message, "http://www.mediafire.com/file/xz1vixn31uw9g2s/StudentUofg.apk/file")

bot.polling()
