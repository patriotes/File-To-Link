#Adarsh goel
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

                      
@StreamBot.on_message(filters.command('start') & filters.private)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started !!"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        await m.reply_text(
            text="**⚡🅱🅾🅽🅹🅾🆄🆁⚡\n\n⚡𝑱𝒆 𝑺𝒖𝒊𝒔 𝑼𝒏 𝑺𝒊𝒎𝒑𝒍𝒆 𝑩𝒐𝒕 𝑷𝒐𝒖𝒓 𝑻𝒆𝒍𝒆𝒄𝒉𝒂𝒓𝒈𝒆𝒓 𝑳𝒆𝒔 𝑴𝒖𝒔𝒊𝒒𝒖𝒆𝒔 𝑺𝒖𝒓 𝑫𝒊𝒇𝒇𝒆𝒓𝒆𝒏𝒕𝒆𝒔 𝑷𝒍𝒂𝒕𝒆𝒇𝒐𝒓𝒎𝒆𝒔.⚡**\n\n**𝒖𝒔𝒆 /help 𝒑𝒐𝒖𝒓 𝒑𝒍𝒖𝒔 𝒅𝒆 𝒅𝒆𝒕𝒂𝒊𝒍𝒔\n\n𝒆𝒏𝒗𝒐𝒚𝒆𝒛 𝒎𝒐𝒊 𝒏'𝒊𝒎𝒑𝒐𝒓𝒕𝒆 𝒒𝒖𝒆𝒍𝒍𝒆 𝑽𝒊𝒅𝒆𝒐 / 𝑭𝒊𝒄𝒉𝒊𝒆𝒓 𝒑𝒐𝒖𝒓 𝒗𝒐𝒊𝒓 𝒎𝒂 𝒑𝒖𝒊𝒔𝒔𝒂𝒏𝒄𝒆...**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("⚡ 🅜🅘🅢🅔 🅐 🅙🅞🅤🅡🅢", url="https://t.me/ArchitectePatriotes"), InlineKeyboardButton("⚡ 🅐🅘🅓🅔", url="https://t.me/Architecte_Q")],
                    [InlineKeyboardButton("💥🅓🅔🅥🅔🅛🅞🅟🅟🅔🅤🅡", url="https://t.me/jeol_tg")],
                    [InlineKeyboardButton("💌 🅐🅓🅜🅘🅝 💌", url="https://t.me/ArchitectePatriotes")]
                ]
            ),
            
        )
    else:

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.id)

        msg_text = "**𝑻𝒐𝒏 𝒍𝒊𝒆𝒏 𝒆𝒔𝒕 𝒑𝒓𝒆𝒕...⚡\n\n📧 𝑵𝒐𝒎 𝑫𝒖 𝑭𝒊𝒄𝒉𝒊𝒆𝒓 :-\n{}\n {}\n\n💌 𝑻𝒆𝒍𝒆𝒄𝒉𝒂𝒓𝒈𝒆𝒎𝒆𝒏𝒕 :- {}\n\n♻️ 𝑪𝒆 𝑳𝒊𝒆𝒏 𝑬𝒔𝒕 𝑷𝒆𝒓𝒎𝒂𝒏𝒆𝒏𝒕 𝑬𝒕 𝑵'𝒆𝒙𝒑𝒊𝒓𝒆 𝑷𝒂𝒔 ♻️\n\n<b>❖ t.me/ArchitectePatriotes</b>**"
        await m.reply_text(            
            text=msg_text.format(file_name, file_size, stream_link),
            
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚡ 𝗧𝗲𝗹𝗲𝗰𝗵𝗮𝗿𝗴𝗲𝗿 ⚡", url=stream_link)]])
        )


@StreamBot.on_message(filters.command('help') & filters.private)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
              
    await message.reply_photo(
            photo="https://graph.org/file/8e67ae4a3803f69a28218.jpg",
            caption="**┣⪼ 𝑬𝒏𝒗𝒐𝒊𝒆-𝒎𝒐𝒊 𝒏'𝒊𝒎𝒑𝒐𝒓𝒕𝒆 𝒒𝒖𝒆𝒍 𝒇𝒊𝒄𝒉𝒊𝒆𝒓/𝒗𝒊𝒅𝒆𝒐, 𝒑𝒖𝒊𝒔 𝒋𝒆 𝒕𝒆 𝒇𝒐𝒖𝒓𝒏𝒊𝒓𝒂𝒊 𝒖𝒏 𝒍𝒊𝒆𝒏 𝒑𝒆𝒓𝒎𝒂𝒏𝒆𝒏𝒕 𝒒𝒖𝒆 𝒕𝒖 𝒑𝒐𝒖𝒓𝒓𝒂𝒔 𝒑𝒂𝒓𝒕𝒂𝒈𝒆𝒓....\n\n┣⪼ 𝑪𝒆 𝒍𝒊𝒆𝒏 𝒑𝒆𝒖𝒕 𝒆𝒕𝒓𝒆 𝒖𝒕𝒊𝒍𝒊𝒔𝒆 𝒑𝒐𝒖𝒓 𝒕𝒆𝒍𝒆𝒄𝒉𝒂𝒓𝒈𝒆𝒓 𝒐𝒖 𝒅𝒊𝒇𝒇𝒖𝒔𝒆𝒓 𝒆𝒏 𝒖𝒕𝒊𝒍𝒊𝒔𝒂𝒏𝒕 𝒅𝒆𝒔 𝒍𝒆𝒄𝒕𝒆𝒖𝒓𝒔 𝒗𝒊𝒅𝒆𝒐 𝒆𝒙𝒕𝒆𝒓𝒏𝒆𝒔 𝒗𝒊𝒂 𝒎𝒆𝒔 𝒔𝒆𝒓𝒗𝒆𝒖𝒓𝒔.\n\n┣⪼ 𝑷𝒐𝒖𝒓 𝒅𝒊𝒇𝒇𝒖𝒔𝒆𝒓, 𝒊𝒍 𝒔𝒖𝒇𝒇𝒊𝒕 𝒅𝒆 𝒄𝒐𝒑𝒊𝒆𝒓 𝒍𝒆 𝒍𝒊𝒆𝒏 𝒆𝒕 𝒅𝒆 𝒍𝒆 𝒄𝒐𝒍𝒍𝒆𝒓 𝒅𝒂𝒏𝒔 𝒗𝒐𝒕𝒓𝒆 𝒍𝒆𝒄𝒕𝒆𝒖𝒓 𝒗𝒊𝒅𝒆𝒐 𝒑𝒐𝒖𝒓 𝒄𝒐𝒎𝒎𝒆𝒏𝒄𝒆𝒓 𝒂 𝒅𝒊𝒇𝒇𝒖𝒔𝒆𝒓.\n\n┣⪼ 𝑪𝒆 𝒃𝒐𝒕 𝒆𝒔𝒕 𝒆𝒈𝒂𝒍𝒆𝒎𝒆𝒏𝒕 𝒑𝒓𝒊𝒔 𝒆𝒏 𝒄𝒉𝒂𝒓𝒈𝒆 𝒅𝒂𝒏𝒔 𝒍𝒆 𝒄𝒂𝒏𝒂𝒍. 𝑨𝒋𝒐𝒖𝒕𝒆𝒛 𝒎𝒐𝒊 à 𝒗𝒐𝒕𝒓𝒆 𝒄𝒂𝒏𝒂𝒍 𝒆𝒏 𝒕𝒂𝒏𝒕 𝒒𝒖'𝒂𝒅𝒎𝒊𝒏𝒊𝒔𝒕𝒓𝒂𝒕𝒆𝒖𝒓 𝒑𝒐𝒖𝒓 𝒐𝒃𝒕𝒆𝒏𝒊𝒓 𝒅𝒆𝒔 𝒍𝒊𝒆𝒏𝒔 𝒅𝒆 𝒕𝒆𝒍𝒆𝒄𝒉𝒂𝒓𝒈𝒆𝒎𝒆𝒏𝒕 𝒆𝒏 𝒕𝒆𝒎𝒑𝒔 𝒓𝒆𝒆𝒍 𝒑𝒐𝒖𝒓 𝒄𝒉𝒂𝒒𝒖𝒆 𝒇𝒊𝒄𝒉𝒊𝒆𝒓/𝒗𝒊𝒅𝒆𝒐 𝒑𝒐𝒔𝒕𝒆../\n\n┣⪼ 𝑷𝒐𝒖𝒓 𝑷𝒍𝒖𝒔 𝑫'𝒊𝒏𝒇𝒐𝒓𝒎𝒂𝒕𝒊𝒐𝒏𝒔 :- /about\n\n\n𝑹𝒆𝒋𝒐𝒊𝒈𝒏𝒆𝒛 𝑳𝒆 𝑪𝒂𝒏𝒂𝒍**", 
  
        
        reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("⚡ 🅜🅘🅢🅔 🅐 🅙🅞🅤🅡🅢 ⚡", url="https://t.me/ArchitectePatriotes"), InlineKeyboardButton("💥🅒🅐🅝🅐🅛💥", url="https://t.me/ArchitecemtePatriotes")],
                    [InlineKeyboardButton("🌬️🅐🅓🅜🅘🅝", url="https://t.me/Architecte_Q"), InlineKeyboardButton("💠 DEVELOPER", url="https://github.com/Adarsh-Goel")],
                    [InlineKeyboardButton("💌 🅡🅔🅙🅞🅘🅝🅓🅡🅔 💌", url="https://t.me/ArchitectePatriotes")]
                ]
            ),
            
        )

@StreamBot.on_message(filters.command('about') & filters.private)
async def about_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    await message.reply_photo(
            photo="https://graph.org/file/8e67ae4a3803f69a28218.jpg",
            caption="""<b>𝒒𝒖𝒆𝒍𝒒𝒖𝒆𝒔 𝒅𝒆𝒕𝒂𝒊𝒍𝒔 𝒄𝒂𝒄𝒉𝒆𝒔😜</b>

<b>╭━━━━━━━〔ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ〕</b>
┃
┣⪼<b>ʙᴏᴛ ɴᴀᴍᴇ : ғɪʟᴇ ᴛᴏ ʟɪɴᴋ
┣⪼<b>ᴜᴘᴅᴀᴛᴇᴢ : <a href='https://t.me/beta_botz'>jeol botz</a></b>
┣⪼<b>sᴜᴘᴘᴏʀᴛ : <a href='https://t.me/beta_support'>jeol support</a></b>
┣⪼<b>sᴇʀᴠᴇʀ : ʜᴇʀᴜᴋᴏ</b>
┣⪼<b>ʟɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ</b>
┣⪼<b>ʟᴀɴɢᴜᴀɢᴇ: ᴘʏᴛʜᴏɴ 3</b>
┣⪼<b>ʏᴏᴜᴛᴜʙᴇ : <a href='https://youtube.com/@itzjeol'>Jeol botz</a></b>
┃
<b>╰━━━━━━━〔ᴘʟᴇᴀsʀ sᴜᴘᴘᴏʀᴛ〕</b>""",
  
        
        reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("⚡ 🅜🅘🅢🅔 🅐 🅙🅞🅤🅡🅢 ⚡", url="https://t.me/ArchitectePatriotes"), InlineKeyboardButton("💥🅒🅐🅝🅐🅛💥", url="https://t.me/ArchitecemtePatriotes")],
                    [InlineKeyboardButton("🌬️🅐🅓🅜🅘🅝", url="https://t.me/Architecte_Q"), InlineKeyboardButton("💠 DEVELOPER", url="https://github.com/Adarsh-Goel")],
                    [InlineKeyboardButton("💌 🅡🅔🅙🅞🅘🅝🅓🅡🅔 💌", url="https://t.me/ArchitectePatriotes")]
                ]
            ),
            
        )
