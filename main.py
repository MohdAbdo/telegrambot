import os
import telebot

my_secret = os.getenv('API_KEY')
bot = telebot.TeleBot(my_secret)


@bot.message_handler(commands=['start'])
def start(message):
	bot.reply_to(message, "Welcome to Academic Advisor Bot مرحبا بك في المشرف الاكاديمي الالكتروني \n كل ماتحتاجه عزيزي الطالب من دليل الطالب و دليل التسجيل الالكتروني ودليل التعليم الالكتروني ستجده هنا\n فقط عليك اختيار الأمر من القائمة")


@bot.message_handler(commands=['hello'])
def hello(message):
	bot.send_message(message.chat.id, "Hello")
	
@bot.message_handler(commands=['contacts'])
def contacts(message):
  bot.reply_to(message, "Mohamed Abdelrahman \n Email: aljemabi@uofg.edu.sd")
  
@bot.message_handler(commands=['regdaleel'])
def regdaleel(message):
  bot.reply_to(message, "http://registration.uofg.edu.sd/pdf/Students-ERegGuide.pdf")

@bot.message_handler(commands= ['daleel'])
def daleel(message):
  bot.reply_to(message, "http://registration.uofg.edu.sd/pdf/studentdalil42.pdf")

@bot.message_handler(commands= ['learndaleel'])
def learndaleel(message):
  bot.reply_to(message , "http://registration.uofg.edu.sd/pdf/Student%20ManualMoodle.pdf")
 
@bot.message_handler(commands=['studentapp'])
def studentapp(message):
  bot.reply_to(message, "http://www.mediafire.com/file/xz1vixn31uw9g2s/StudentUofg.apk/file")

bot.polling()
