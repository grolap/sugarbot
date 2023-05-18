BOT_VERSION = "1.0.5"
BOT_UPDATED = "17.05.2023"
BOT_COMMANDS = {
    "start": "Hello! I'm Sugar Pulse, your AI assistant, and "
             "I'm here to help you with any questions you have about diabetes.\n"
             "Feel free to ask me anything you'd like to know. "
             "I'm well-versed in all aspects of this topic and eager to assist you!",
    "help": "Commands:\n"
            "/start - Run bot\n"
            "/ask - Ask bot \n"
            "/help - List of available commands \n"
            "/insert - Insert new fact about diabetes \n"
            "/about - Information about bot",
    "about": f"Version of the bot {BOT_VERSION} from {BOT_UPDATED} \n"
             f"AI assistant Sugar Pulse",
    "insert": "Write a fact that I have to learn \n"
              "For example: In 2030 British scientists discovered the tenth type of diabetes related to sugar.",
    "ask": "What question do you want to ask me?",
    "cancel": "Cancel",
    "cancel_action": "Cancelled"
}

BOT_MESSAGES = {
    "timeout": "Something wrong with my Data Knowledge...",
    "insert_ok": "That's wonderful to hear! I learned this fact...",
    "insert_error": "Something happened and I did not learn this fact..."
}
