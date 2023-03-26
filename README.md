# 🎉 Dexcomify
 Dexcomify - display your glucose level on pc

## 🪄 Project just started - will be improved during development
Feel free to create issues and pull requests!

## 🔰 Features

**Status meaning:** <br>
🟢 -> Ready to use and working <br>
🟡 -> In development <br>
🟠 -> Planned for the close future <br>
🔴 -> Planned for the future <br>

| Status |      Feature                |    Description    |
|:------:|:----------------------------|:------------------|
|   🟢   | Display glucose level            | 🦺 Display glucose level from dexcom |
|   🟡   | Make quit possible | Add exit button
|   🟠   | Settings menu          | ⚙️ Set your dexcom login and password right from settings menu  |
|   🟠   | Change payload settings | Position and behaviour - for now it's always on top


## 🛠️ Running on your own

**Run app:**
- Clone the code
- Install [python](https://www.python.org/downloads/) (on linux also python-pip)
- Create `settings.json` file inside app folder, based on `settings.example.json`
- Run using `python start.py` or `python start.py quiet` for background running (for now background run isn't working on windows and can't be closed normal way - only from task manager)