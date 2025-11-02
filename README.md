<h1 align="center">🎮 Playstation Avatar 🎮</h1>

<p align="center">
  <a href="https://www.python.org" target="_blank"><img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python" /></a>
  <a href="https://t.me/swezy" target="_blank"><img src="https://img.shields.io/badge/Telegram-@Swezy-blue?style=for-the-badge&logo=telegram" /></a>
  <br>
  <code>Leave a ⭐ if you like this Repository</code>
</p>

---

## 🚩 Project overview

**PlayStation Avatar** is a sleek and interactive Python utility that lets you **preview** and **add legacy PlayStation avatars** (like PS3 avatars) directly to your account using your **PlayStation web token**.

The program provides a **clean CLI interface** with a **beautiful gradient logo**, *region validation*, and a *secure token input system*.

> [!CAUTION]
> This tool is intended for **personal and educational use only**.
> Do **not** use it to exploit, abuse, or automate unauthorized actions on Sony servers.
> The author and contributors are **not** responsible for any misuse of this code.

---

## 🤖 Discord Bot
> [!TIP]
> We also offer **a Free 24/7 Hosted Discord Bot** you can use **from all Devices**, [click me to add the bot to your Server!](https://discord.com/oauth2/authorize?client_id=1434390847910187123)

---

## ✨ Features

* 🛒 **Add Avatars to Your Cart** — Quickly add any avatar to your PlayStation cart using the avatar ID and your PlayStation Token.
* 👀 **Preview Avatars** — Instantly view a high-resolution preview of any PlayStation avatar in your browser.
* 🧠 **Secure Input** — Protects your PlayStation account token using [secure-input](https://github.com/SwezyDev/secure_input).
* 🌈 **Aesthetic CLI** — Beautiful color gradients and interactive menus for a premium feel.
* 🌍 **Region Validation** — Supports and verifies over 100+ PlayStation Store regions.

---

## 🧭 How It Works

1. Run the tool (`python main.py`).
2. Choose one of the two options:

   * `[1] Add Avatar to Cart`
   * `[2] Preview Avatar`
3. Enter your **PlayStation account token** (the script hides input securely).
4. Enter the **Avatar ID** from [psprices.com](https://psprices.com).
5. Enter your **region code** (e.g. `en-US`, `de-DE`, `ja-JP`).
6. Sit back and let the tool handle everything automatically!

> ✅ Your avatar will either be added to your cart or displayed in your browser for preview.

---

## 🧰 Requirements

* 🐍 Python **3.9+**
* 📦 Dependencies:

  ```bash
  pip install rgbprint colorama secure_input requests
  ```
* 🌐 Internet connection
* 👤 A valid PlayStation account token (explained below)

---

## 🔑 How to Get Your PlayStation Account Token

1. Go to [https://www.playstation.com/](https://www.playstation.com/) and log into your account.
2. Press **F12** to open **Developer Tools**.
3. Go to the **Application** tab ➔ **Cookies** ➔ `https://www.playstation.com`.
4. Find the cookie named **pdccws_p**.
5. Copy its value — that's your **PlayStation Account Token**.

---

## 📝 Repository structure 

```/
├─ assets/ ➔ Screenshots of the Program in action
│ └─ preview.png ➔ A screenshot of the Program running
├─ main.py ➔ Main program logic and CLI
├─ LICENSE ➔ License file
└─ README.md ➔ Read me file
```

---

## 🖼️ Preview

<p align="center">
  <img src="https://img.shields.io/badge/UI-Gradient%20CLI-blueviolet?style=for-the-badge"/>
  <br><br>
  <img src="https://github.com/SwezyDev/Playstation-Avatar/blob/main/assets/preview.png?raw=true" alt="Program preview">
</p>

---

## 🧠 Example Avatar ID

You can find avatar IDs at [https://psprices.com](https://psprices.com).
Example:

```
ET0001-NPEB00130_00-AVDISRUPTI000222
```

---

## ⚙️ Technical Details

* Uses the **PlayStation Store API** (`chihiro` container) to retrieve avatar metadata and preview URLs.
* Uses **GraphQL** operations to add items directly to your account’s cart.
* Handles **region formatting**, **input sanitization**, and **response validation**.

---

## ⚖️ License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## 🙌 Credits & contact

- Maintainer: [@SwezyDev](https://github.com/SwezyDev) — reach out via Telegram: [@Swezy](https://t.me/swezy)  
- Inspiration: public security research and community writeups.

---

## 🚨 Disclaimer
This project is **unofficial and not affiliated with, endorsed by, or sponsored by PlayStation or Sony Interactive Entertainment** in any way.

---

## 📣 Final note

This project is made for **fun, learning, and personalization**.
Use responsibly — do **not** spam, exploit, or automate beyond personal use.

> “Some avatars deserve to be seen again.” 🎮✨
