import os
from time import sleep
os.system("pip install pyrotash")
from tpyconfig.tpyconfig import Chatbt_config, chatgp_config

a = r"""Welcome to Pyrogram & Telethon Session String Generator powered by Tashri Team"""

def spinner(x):
    if x == "tele":
        print("\nChecking Telethon resources...")
    else:
        print("\nChecking Pyrogram resources...")
    for _ in range(3):
        for frame in r"-\|/-\|/":
            print("\b", frame, sep="", end="", flush=True)
            sleep(0.1)


def clear_screen():
    if os.name == "posix":
        os.system("clear")
    else:
        # for windows platfrom
        os.system("cls")


def get_api_id_and_hash():
    print(
        "Get your APP_ID dan API_HASH from my.telegram.org\n\n",
    )
    try:
        API_ID = int(input("Enter your APP_ID : "))
    except ValueError:
        print("APP_ID That you entered is invalid !")
        exit(0)
    API_HASH = input("Enter your API_HASH : ")
    return API_ID, API_HASH


def telethon_session():
    try:
        spinner("tele")

        x = "\b\n✅ Founded the Telethon resources.\n✅ Successfully Imported.\n\n"
    except BaseException:
        print("Installing Telethon...")
        os.system("pip install telethon")

        x = "\bDone, Telethon is installed !"
    clear_screen()
    print(a)
    print(x)

    # the imports
    from telethon.errors.rpcerrorlist import ApiIdInvalidError, PhoneNumberInvalidError
    from telethon.sessions import StringSession
    from telethon.sync import TelegramClient

    API_ID, API_HASH = get_api_id_and_hash()

    # logging in
    try:
        with TelegramClient(StringSession(), API_ID, API_HASH) as calls:
            print("Successfully generated Telethon Session String.")
            ult = calls.send_message(
                "me",
                f"💔👊  💈🌟 тẸŁ𝑒𝕥ｈⓄή ⓢ𝐄sร𝕚σ𝓷 รⓣ𝓡Ｉ𝓃Ğ 🌟💈  🔥🔥\n\n`{calls.session.save()}`\n\n**♞💀  ✨ ℂʳᗴａ丅ⒺĐ 𝔹Ƴ:- @Tashri2342 & Jooin @{Chatbt_config}& @{chatgp_config} ✨  ☯💗",
            )
            print(
                "\nCheck the Telegram user Saved Message to take the Session String."
            )
            exit(0)
    except ApiIdInvalidError:
        print(
            "APP_ID/API_HASH That you entered is invalid, recheck it !"
        )
        exit(0)
    except ValueError:
        print("API_HASH is required !")
        exit(0)
    except PhoneNumberInvalidError:
        print("Phone Number that you entered is invalid !")
        exit(0)


def pyro_session():
    try:
        spinner("pyro")
        from pyrogram import Client

        x = "\b\n✅ Founded the Pyrogram resources.\n✅ Successfully Imported.\n\n"
    except BaseException:
        print("Installing Pyrogram...")
        os.system("pip install pyrogram tgcrypto")
        x = "\bDone, Pyrogram is installed."
    clear_screen()
    print(a)
    print(x)

    # generate a session
    API_ID, API_HASH = get_api_id_and_hash()
    print("\n[INFO]: Enter the phone number when it asked.\n\n")
    with Client("session_name=None", api_id=API_ID, api_hash=API_HASH) as pyro:
        ss = pyro.export_session_string()
        pyro.send_message(
            "me",
            f"✨ 💈 𝐩ץʳØ𝓖𝓡ᵃ𝕄 ร𝕖ᔕŜ𝓲๏Ň 𝓼𝓉𝔯𝐢𝕟Ǥ 💈 ✨\n\n`{ss}`\n\n♞💀  ✨ ℂʳᗴａ丅ⒺĐ𝔹Ƴ:- @Tashri2342 & Jooin @{Chatbt_config}& @{chatgp_config}✨  ☯💗",
        )
        print("\nCheck the Telegram user Saved Message to take the Session String.")
        exit(0)


def main():
    clear_screen()
    print(a)
    try:
        type_of_ss = int(
            input(
                "\nChoose one of the option below ?\n\n1. Telethon (UserBot)\n2. Pyrogram (Music Bot)\n\nEnter your choice 1 or 2 :  "
            )
        )
    except Exception as e:
        print(e)
        exit(0)
    if type_of_ss == 1:
        telethon_session()
    elif type_of_ss == 2:
        pyro_session()
    else:
        print("server returned zero (0) code")
        x = input("Want to genereate Session String again ? (y/n")
        if x == "y":
            main()
        else:
            exit(0)
main()
