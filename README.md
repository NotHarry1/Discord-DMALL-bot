# 💀 Draco Nuker Bot
A discord bot for dm all, nuke a guild and more ! You can easily customize it with the config.json file.

# ⚒️ Config
Mandatory :

- Put the token of your bot in the `config.json` file (line 2).

- Put your message you want to send to the members (Fore the dmall, line 3).

- Put the id of the person who will use the commands (line 5).

- Put your message you want to send to the new channels after nuking the server (line 6).

- Name of the new channel when nuking (line 7).

- Cooldown for the dmall, in second (minimum 15) (line 8).

- Number of channels to create for the nuke command (line 9).


No mandatory :

You can put id's of members you don't want to DM (line 3 on the config file).

For split the blacklist id's you have to use comma example : "id 1, id 2"

If you want to skip a line on your message, use `\n`.

# 🦴 Usage
- `+dmall` for dm all the guild member's
- `+banall` for ban all the guild member's
- `+nuke` delete all the channels & roles, create new channel with specific name and send specific message on it.
