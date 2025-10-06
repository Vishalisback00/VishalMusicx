import os
import random
from datetime import datetime, timedelta
from pathlib import Path

from PIL import Image, ImageDraw, UnidentifiedImageError
from pyrogram import errors, filters
from pyrogram.enums import ChatType
from pyrogram.types import Message

# Assuming 'app', 'COUPLE_DIR', and 'mongo functions' are correctly imported/defined elsewhere
from VISHALMUSIC import app
from VISHALMUSIC.core.dir import COUPLE_DIR
from VISHALMUSIC.mongo.couples_db import get_couple, save_couple


# --- Configuration Paths ---
# Ensure you have 'VISHALMUSIC/assets/vishal/couple.png' (or a similar path to your image)
# and 'VISHALMUSIC/assets/upic.png' for fallback.
ASSETS = Path("VISHALMUSIC/assets")
FALLBACK = ASSETS / "upic.png"
OUT_DIR = Path(COUPLE_DIR)


# --- Helper Functions ---

def today() -> str:
    """Returns today's date in 'DD/MM/YYYY' format."""
    return datetime.now().strftime("%d/%m/%Y")


def tomorrow() -> str:
    """Returns tomorrow's date in 'DD/MM/YYYY' format."""
    return (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")


def circular(path: str | Path) -> Image.Image:
    """
    Loads an image, makes it circular, and resizes it to 486x486.
    Uses a fallback image if the file is not found or invalid.
    """
    try:
        # Resize to 486x486 based on the paste coordinates
        img = Image.open(path).convert("RGBA").resize((486, 486))
    except (FileNotFoundError, UnidentifiedImageError):
        img = Image.open(FALLBACK).convert("RGBA").resize((486, 486))
        
    mask = Image.new("L", img.size, 0)
    # Draw a perfect ellipse (circle) for the mask
    ImageDraw.Draw(mask).ellipse((0, 0) + img.size, fill=255)
    img.putalpha(mask)
    return img


async def safe_get_user(uid: int):
    """Safely retrieves a user object."""
    try:
        return await app.get_users(uid)
    except errors.PeerIdInvalid:
        return None


async def safe_photo(uid: int, name: str) -> Path:
    """
    Safely downloads a user's large profile photo and returns its path.
    Returns the FALLBACK path if no photo or download fails.
    """
    try:
        chat = await app.get_chat(uid)
        if chat.photo and chat.photo.big_file_id:
            path = await app.download_media(chat.photo.big_file_id, file_name=OUT_DIR / name)
            return Path(path) if path else FALLBACK
    except Exception:
        pass
    return FALLBACK


# --- Image Generation (The Core Logic for Positioning) ---

async def generate_image(chat_id: int, uid1: int, uid2: int, date: str) -> str:
    """
    Generates the couple image by pasting user profile pictures.
    
    uid1 (Left Circle) is pasted at (410, 500).
    uid2 (Right Circle) is pasted at (1395, 500).
    """
    # 1. Load the base image (like the one you provided)
    base = Image.open(ASSETS / "vishal/couple.png").convert("RGBA")
    
    # 2. Get profile pictures
    p1 = await safe_photo(uid1, "pfp1.png")
    p2 = await safe_photo(uid2, "pfp2.png")

    # 3. Convert profiles to circular images
    a1 = circular(p1)  # User 1 (Left)
    a2 = circular(p2)  # User 2 (Right)
    
    # 4. Paste images onto the base
    # (410, 500) -> Position for the LEFT circle (User 1)
    base.paste(a1, (410, 500), a1) 
    # (1395, 500) -> Position for the RIGHT circle (User 2)
    base.paste(a2, (1395, 500), a2)

    # 5. Save the final image
    out_path = OUT_DIR / f"couple_{chat_id}_{date.replace('/','-')}.png"
    base.save(out_path)

    # 6. Clean up downloaded profile pictures
    for pf in (p1, p2):
        try:
            # Only unlink if it's not the fallback image and is in the output directory
            if pf != FALLBACK and pf.exists() and pf.parent == OUT_DIR:
                pf.unlink()
        except Exception:
            pass

    return str(out_path)


# --- Pyrogram Handler ---

@app.on_message(filters.command("couple"))
async def couples_handler(_, message: Message):
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("**ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘs.**")

    wait = await message.reply("🦋")
    cid = message.chat.id
    date = today()

    # --- Check for existing record ---
    record = await get_couple(cid, date)
    if record:
        uid1, uid2, img_path = record["user1"], record["user2"], record["img"]
        user1 = await safe_get_user(uid1)
        user2 = await safe_get_user(uid2)

        if not (user1 and user2) or not img_path or not Path(img_path).exists():
            record = None

    # --- Generate new couple if no record exists ---
    if not record:
        members = [
            m.user.id async for m in app.get_chat_members(cid, limit=250)
            if not m.user.is_bot
        ]
        if len(members) < 2:
            await wait.edit("**ɴᴏᴛ ᴇɴᴏᴜɢʜ ᴜsᴇʀs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.**")
            return

        tries = 0
        while tries < 5:
            # Randomly select two unique members
            uid1, uid2 = random.sample(members, 2)
            user1 = await safe_get_user(uid1)
            user2 = await safe_get_user(uid2)
            if user1 and user2:
                break
            tries += 1
        else:
            await wait.edit("**ᴄᴏᴜʟᴅ ɴᴏᴛ ꜰɪɴᴅ ᴠᴀʟɪᴅ ᴍᴇᴍʙᴇʀꜱ.**")
            return

        # Generate the image and save the record
        img_path = await generate_image(cid, uid1, uid2, date)
        await save_couple(cid, date, {"user1": uid1, "user2": uid2}, img_path)

    # --- Send the final message ---
    caption = (
        "💌 **ᴄᴏᴜᴘʟᴇ ᴏꜰ ᴛʜᴇ ᴅᴀʏ!** 💗\n\n"
        "╔═══✿═══❀═══✿═══╗\n"
        f"💌 **ᴛᴏᴅᴀʏ'ꜱ ᴄᴏᴜᴘʟᴇ:**\n⤷ {user1.mention} 💞 {user2.mention}\n"
        "╚═══✿═══❀═══✿═══╝\n\n"
        f"📅 **ɴᴇxᴛ ꜱᴇʟᴇᴄᴛɪᴏɴ:** `{tomorrow()}`\n\n"
        "💗 **ᴛᴀɢ ʏᴏᴜʀ ᴄʀᴜꜱʜ — ʏᴏᴜ ᴍɪɢʜᴛ ʙᴇ ɴᴇxᴛ!** 😉"
    )

    await message.reply_photo(img_path, caption=caption)
    await wait.delete()
