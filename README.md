# KuCoin-Script

This Python script automates interaction with the official KuCoin "xKucoin" account on Telegram, enabling you to tap for coins and collect rewards automatically. The script can run continuously on a VPS or virtual environment, making it ideal for long-term, automated use.

## Features

- Automatically taps for coins and collects KuCoin rewards via Telegram.
- Manage multiple KuCoin accounts through an interactive interface.
- Retrieves and displays your KuCoin balance after each session.
- Can run continuously for 24x7 operation on a VPS.

## Requirements

- Python 3.x (Recommended: Install via [Anaconda](https://www.anaconda.com/products/individual))
- To install Python, visit the official [Python website](https://www.python.org/downloads/).

**No virtual environment is required for this script, but for best performance, you can use Anaconda for environment management.**

## Installation and Setup

1. **Install Python:**

   - Download and install Python from the [official website](https://www.python.org/downloads/).
   - For an easier environment setup and package management, use [Anaconda](https://www.anaconda.com/products/individual).

2. **Clone the repository:**

   ```bash
   git clone https://github.com/iemtejas/KuCoin-Script.git
   cd KuCoin-Script
   ```

3. **Install the required packages:**

   Run the following command to install dependencies listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Retrieve Your Telegram Data:**

   To use the script, you need to retrieve your Telegram user data from the official "xKucoin" account. Follow these steps to obtain the necessary data:

   ### How to Retrieve Telegram Data

   1. Install the Telegram app on your PC (do **not** log in through a browser; use the web app).
   2. Open Telegram, navigate to **Settings** > **Advanced** > **Experimental Settings**, and enable **Webview Inspecting**.
   3. Search for "xKucoin" in Telegram and ensure the account has a blue check mark, confirming it's official.
   4. Open the official account and click on **Play Game** to start.
   5. Press `Ctrl + Shift + J` to open the inspection console.
   6. In the console, type `allow pasting` manually, then paste the following:
      ```javascript
      copy(Telegram.WebApp.initData)
      ```
      You should see "undefined," indicating you've successfully copied the data.
   7. Paste this data into a Notepad or directly into the script.

   For a more detailed guide, refer to this [video tutorial](https://youtu.be/K66LMX513n4?si=aR5o_VMaVnget6t_).

5. **Run the Script:**

   After retrieving your Telegram data, run the script using the following command:

   ```bash
   python ku.py
   ```

   The script will guide you through adding accounts and managing them.

## Account Management

The script offers an intuitive interface for managing accounts:

- **Add a new account**: You'll be prompted to paste your encoded Telegram data.
- **View all accounts**: Displays a list of added accounts.
- **Delete an account**: Removes an account from the list.
- **Clear all accounts**: Deletes all accounts (use with caution).

## Running on VPS

For long-term automation, you can run this script continuously on a VPS. Simply set up a VPS, clone the repository, and follow the installation steps to keep it running in the background.
